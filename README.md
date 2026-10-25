# 빨간망토 차차 SFC 한글패치

슈퍼패미컴용 **Akazukin Cha Cha 일본판**을 한국어로 즐길 수 있는 비공식 팬 패치입니다. **v1.0.0**

**[한글패치 다운로드](https://github.com/enthhende/chacha-sfc-korean-patch/releases/tag/v1.0.0) · [패치 안내](https://enthhende.github.io/games/chacha/patch/) · [한국어 공략](https://enthhende.github.io/games/chacha/guide/)**

이야기 대사, 타이틀, 세이브 메뉴와 슬롯, 전투·소지품·상태 메뉴, 기술·아이템 이름과 설명을 한국어로 바꿨습니다.

## 가장 간단한 적용법 — 설치 없이 브라우저에서

1. **[다운로드 페이지에서 바로 적용](https://enthhende.github.io/games/chacha/patch/#browser-patch)**을 엽니다.
2. 헤더 없는 일본판 원본 `.sfc` 또는 `.smc` 파일을 선택합니다.
3. **한글 ROM 만들기 → 한글 ROM 저장**을 누릅니다.
4. 내려받은 `.sfc` 파일을 에뮬레이터에서 엽니다.

Windows·macOS·Linux에서 사용할 수 있으며 Python 설치나 명령어 입력이 필요 없습니다. ROM은 브라우저 안에서만 처리되고 서버로 전송되지 않습니다. 원본·패치·완성 ROM의 크기와 SHA-256을 자동 확인합니다.

## 오프라인 적용 — Windows 배치 파일 / macOS

릴리즈에서 **[chacha-sfc-korean-patch-v1.0.0-easy.zip](https://github.com/enthhende/chacha-sfc-korean-patch/releases/download/v1.0.0/chacha-sfc-korean-patch-v1.0.0-easy.zip)**을 받아 압축을 풉니다.

- **Windows:** `apply-patch.bat`을 더블클릭합니다. 브라우저 적용 화면이 열리면 원본 ROM을 선택하고 **한글 ROM 만들기 → 한글 ROM 저장**을 누릅니다. PowerShell 명령이나 Python 설치는 필요 없습니다.
- **macOS·Linux:** `apply-patch.html`을 브라우저에서 열고 같은 순서로 진행합니다. HTML 파일이 편집기로 열리면 ‘연결 프로그램’에서 브라우저를 선택하세요.

패치가 HTML 안에 들어 있어 압축을 푼 뒤에는 인터넷 연결 없이 적용할 수 있습니다. 파일을 브라우저 화면의 선택 상자에 끌어다 놓아도 됩니다.

## BPS / xdelta 프로그램으로 적용

SFC ROM에도 xdelta 패치를 적용할 수 있습니다. ZIP의 `patches/`에는 **BPS와 xdelta** 두 형식을 넣었습니다. 원하는 형식 하나만 일본판 원본에 적용하세요.

패치 프로그램에서 **원본 ROM → `.bps` 또는 `.xdelta` 패치 → 새 출력 `.sfc` 파일**을 지정합니다. 같은 원본에 두 패치를 차례로 적용하지 마세요. 둘 다 아래 표의 동일한 한글판을 만듭니다.

<details>
<summary>명령줄 적용법 (선택 사항)</summary>

xdelta3:

```sh
xdelta3 -d -s "원본파일.smc" "patches/chacha-sfc-korean-patch-v1.0.0.xdelta" "빨간망토 차차 한글판.sfc"
```

Python 3.9 이상 (동봉된 BPS 적용 도구):

```sh
python3 scripts/apply_patch.py --rom "원본파일.smc" --output "빨간망토 차차 한글판.sfc"
```

파일 이름은 자신의 경로에 맞게 바꾸고, 출력에는 새 파일 이름을 지정하세요.

</details>

## 지원 원본과 해시

| 파일 | 크기 | SHA-256 |
|---|---:|---|
| 일본판 원본 · copier header 없음 | 1,572,864바이트 | `f5e41c877ed95a66e171735dbf99f86fd972e6dd7687379ed550baa45cf08151` |
| 한글패치 BPS | 426,498바이트 | `cf08f012ad7ee9282762b8c7105c18b263ed4bef6e295c36ee58a6134cce6232` |
| 한글패치 xdelta | 409,389바이트 | `658f3a47a3b45e61a0350561e36b5aac062ea7b6dbb9a810d9ea1fe2e8f4a9f5` |
| 패치 후 한글판 ROM | 2,097,152바이트 | `fa31c546ea8ed8852f783fcb68d317c77a0316eac2c950d1de1561533819e8df` |

다른 리비전, 512바이트 헤더가 붙은 파일, 이미 수정된 ROM에는 적용할 수 없습니다. 배포 ZIP·BPS·xdelta의 해시는 릴리즈의 `SHA256SUMS.txt`, 압축 안 파일의 해시는 `SHA256SUMS`에서 확인할 수 있습니다.

## 플레이와 저장

- **슈퍼패미컴 실기에서는 확인하지 않았습니다.**
- 에뮬레이터는 Mesen Community Edition 2.2.1을 사용할 수 있습니다.
- 기존 저장파일은 먼저 백업하세요. 일반 저장(SRAM)은 새 ROM 파일 이름에 맞춰 에뮬레이터의 저장 폴더에 연결합니다.
- 다른 패치 버전이나 일본판에서 만든 강제저장·세이브스테이트는 사용하지 마세요. 새 게임 또는 일반 저장으로 시작하세요.

## 공략과 오류 제보

[한국어 공략](https://enthhende.github.io/games/chacha/guide/)에서 1~8화 진행과 기술·아이템을 찾아볼 수 있습니다. 공략의 [한글패치 배포란](https://enthhende.github.io/games/chacha/patch/)에서도 다운로드와 적용법을 확인할 수 있습니다.

문제가 있으면 [오류 제보](https://github.com/enthhende/chacha-sfc-korean-patch/issues)에 패치 버전, 에뮬레이터 이름·버전, 재현 순서와 화면을 남겨주세요. ROM 파일은 첨부하지 마세요.

## 제작·글꼴·재배포

- 번역·식자: **러브델릭(엔스헨데)**
- 글꼴: **DOSSaemmul / DOSPilgi** — leedheo, **Dalmoori(달무리)** — RanolP.
- 글꼴 출처와 표시용 수정 내역은 [CREDITS](CREDITS.md), 라이선스 고지는 [LICENSES](LICENSES/)와 [LICENSING](LICENSING.md)에 있습니다.

패치는 **출처와 버전을 표시하면 재배포할 수 있습니다.** 최신 버전과 적용 안내를 받을 수 있도록 **공식 배포 주소 공유를 권장합니다.**

게임 ROM은 배포물에 포함하지 않습니다. 게임과 캐릭터의 권리는 각 권리자에게 있으며 이 패치는 공식 제작사와 관계없는 팬 작업입니다.
