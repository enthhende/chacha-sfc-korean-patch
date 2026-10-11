#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Apply the published Cha Cha BPS patch with exact SHA-256 admission."""
from __future__ import annotations
import argparse
import ctypes
import errno
import hashlib
import json
import os
from pathlib import Path
import struct
import sys
import tempfile
import zlib


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def apply_bps(source, patch, target_limit=0x200000):
    require(len(patch) >= 19 and patch[:4] == b'BPS1', '올바른 BPS1 패치가 아닙니다.')
    source_crc, target_crc, patch_crc = struct.unpack('<III', patch[-12:])
    require(zlib.crc32(patch[:-4]) == patch_crc, '패치 CRC32가 일치하지 않습니다.')
    require(zlib.crc32(source) == source_crc, '원본 CRC32가 일치하지 않습니다.')
    end = len(patch) - 12
    cursor = 4

    def number():
        nonlocal cursor
        value, shift = 0, 1
        for _ in range(10):
            require(cursor < end, 'BPS 숫자 데이터가 잘렸습니다.')
            byte = patch[cursor]
            cursor += 1
            value += (byte & 127) * shift
            require(value < 1 << 64, 'BPS 숫자가 범위를 벗어났습니다.')
            if byte & 128:
                return value
            shift <<= 7
            value += shift
        raise ValueError('BPS 숫자가 너무 깁니다.')

    source_size, target_size, metadata_size = number(), number(), number()
    require(source_size == len(source), 'BPS 원본 크기가 일치하지 않습니다.')
    require(0 < target_size <= target_limit, 'BPS 출력 크기가 허용 범위를 벗어났습니다.')
    require(metadata_size <= end - cursor, 'BPS 메타데이터가 잘렸습니다.')
    cursor += metadata_size
    output = bytearray()
    source_relative = target_relative = 0
    while len(output) < target_size:
        code = number()
        action, length = code & 3, (code >> 2) + 1
        require(length <= target_size - len(output), 'BPS 쓰기가 출력 범위를 벗어났습니다.')
        if action == 0:
            start = len(output)
            require(start + length <= len(source), 'BPS SourceRead가 원본 범위를 벗어났습니다.')
            output.extend(source[start:start + length])
        elif action == 1:
            require(length <= end - cursor, 'BPS TargetRead가 잘렸습니다.')
            output.extend(patch[cursor:cursor + length])
            cursor += length
        else:
            encoded = number()
            delta = -(encoded >> 1) if encoded & 1 else encoded >> 1
            if action == 2:
                source_relative += delta
                require(0 <= source_relative and source_relative + length <= len(source),
                        'BPS SourceCopy가 원본 범위를 벗어났습니다.')
                output.extend(source[source_relative:source_relative + length])
                source_relative += length
            else:
                target_relative += delta
                require(0 <= target_relative < len(output), 'BPS TargetCopy가 미생성 데이터를 참조합니다.')
                for _ in range(length):
                    output.append(output[target_relative])
                    target_relative += 1
    require(cursor == end, 'BPS 동작 뒤에 불필요한 데이터가 있습니다.')
    require(zlib.crc32(output) == target_crc, '출력 CRC32가 일치하지 않습니다.')
    return bytes(output)


def _publish_exclusive(source, destination):
    """Atomic no-replace publication on macOS, Linux and Windows."""
    if os.name == 'nt':
        os.rename(source, destination)  # Windows rename rejects an existing target.
        return
    libc = ctypes.CDLL(None, use_errno=True)
    if sys.platform == 'darwin':
        rename = libc.renamex_np
        rename.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_uint]
        rename.restype = ctypes.c_int
        result = rename(os.fsencode(source), os.fsencode(destination), 4)  # RENAME_EXCL
    elif sys.platform.startswith('linux') and hasattr(libc, 'renameat2'):
        rename = libc.renameat2
        rename.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p, ctypes.c_uint]
        rename.restype = ctypes.c_int
        result = rename(-100, os.fsencode(source), -100, os.fsencode(destination), 1)  # NOREPLACE
    else:
        os.link(source, destination)
        return
    if result != 0:
        code = ctypes.get_errno()
        raise OSError(code, os.strerror(code), str(destination))


def publish_no_replace(source, destination):
    """Prefer exclusive rename; trusted-host fallback runs under our output lock."""
    try:
        _publish_exclusive(source, destination)
    except OSError as error:
        if error.errno not in {errno.ENOTSUP, errno.EOPNOTSUPP, errno.ENOSYS, errno.EINVAL}:
            raise
        # exFAT lacks exclusive rename and hard links. Cooperating CLI writers
        # are serialized by write_new; an unrelated racing writer is excluded
        # by the normal, non-malicious same-user host model.
        require(not destination.exists() and not destination.is_symlink(),
                '출력 파일이 이미 있습니다. 새 파일 이름을 지정해 주세요.')
        os.rename(source, destination)


def write_new(path, data):
    require(not path.exists() and not path.is_symlink(), '출력 파일이 이미 있습니다. 새 파일 이름을 지정해 주세요.')
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    lock = path.with_name('.' + path.name + '.chacha-lock')
    # Exclusive reservation serializes our CLI, without exposing a partial ROM.
    descriptor = os.open(lock, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    os.close(descriptor)
    try:
        require(not path.exists() and not path.is_symlink(),
                '출력 파일이 이미 있습니다. 새 파일 이름을 지정해 주세요.')
        with tempfile.NamedTemporaryFile(dir=path.parent, prefix='.chacha-patch-', delete=False) as f:
            temporary = Path(f.name)
            f.write(data)
            f.flush()
            os.fsync(f.fileno())
        publish_no_replace(temporary, path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
        lock.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description='정확한 일본판 원본에 차차 한글 패치를 적용합니다. 원본은 변경하지 않습니다.')
    root = Path(__file__).resolve().parents[1]
    parser.add_argument('--rom', type=Path, required=True, help='헤더 없는 일본판 원본 SFC/SMC')
    parser.add_argument('--output', type=Path, required=True, help='새 한글 ROM 파일 경로')
    parser.add_argument('--manifest', type=Path, default=root / 'release.json')
    args = parser.parse_args()
    try:
        manifest = json.loads(args.manifest.read_text(encoding='utf-8'))
        require(manifest['schema'] == 'chacha.public-release-manifest/v1', '지원하지 않는 manifest입니다.')
        base = args.manifest.resolve().parent
        relative_patch = Path(manifest['patch']['file'])
        require(not relative_patch.is_absolute() and '..' not in relative_patch.parts, '잘못된 패치 파일 경로입니다.')
        patch_path = base / relative_patch
        require(args.output.resolve() not in (args.rom.resolve(), patch_path.resolve(), args.manifest.resolve()),
                '원본/패치/manifest를 출력으로 지정할 수 없습니다.')
        require(not args.output.exists() and not args.output.is_symlink(), '출력 파일이 이미 있습니다. 새 파일 이름을 지정해 주세요.')
        source = args.rom.read_bytes()
        require(len(source) == manifest['source']['size'], '원본 크기가 다릅니다. 1,572,864바이트의 헤더 없는 일본판이 필요합니다.')
        require(sha256(source) == manifest['source']['sha256'], '지원 원본 SHA-256과 다릅니다. 다른 리비전/수정본은 사용할 수 없습니다.')
        patch = patch_path.read_bytes()
        require(len(patch) == manifest['patch']['size'] and sha256(patch) == manifest['patch']['sha256'],
                '배포 패치의 크기 또는 SHA-256이 일치하지 않습니다.')
        output = apply_bps(source, patch, manifest['target']['size'])
        require(len(output) == manifest['target']['size'] and sha256(output) == manifest['target']['sha256'],
                '완성 ROM이 선언된 최종본과 다릅니다.')
        write_new(args.output, output)
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(2, str(error) + '\n')
    print('완료: ' + str(args.output))
    print('SHA-256: ' + sha256(output))


if __name__ == '__main__':
    main()
