# 빨간망토 차차 SFC 한글패치 v1.0.0

이야기 대사와 타이틀·세이브·전투·소지품·상태 메뉴를 한국어로 바꾼 패치입니다.

**[한국어 공략](https://enthhende.github.io/games/chacha/guide/) · [패치 안내](https://enthhende.github.io/games/chacha/patch/)**

## 다운로드

`chacha-sfc-korean-patch-v1.0.0.zip`을 내려받아 압축을 풉니다. BPS 패치, 적용 도구, 사용법과 글꼴 라이선스 고지가 들어 있습니다.

헤더 없는 일본판 원본에 동봉 도구로 적용하세요. Python 3.9 이상이 필요합니다.

```sh
python3 scripts/apply_patch.py --rom "원본파일.smc" --output "빨간망토 차차 한글판.sfc"
```

| 파일 | 크기 | SHA-256 |
|---|---:|---|
| 일본판 원본 | 1,572,864바이트 | `f5e41c877ed95a66e171735dbf99f86fd972e6dd7687379ed550baa45cf08151` |
| BPS 패치 | 424,773바이트 | `8fc0e0980967acd31f54562f8786fc41b5c1fad028a42f78860774364a29465f` |
| 패치 후 ROM | 2,097,152바이트 | `a8edfb9b3df082783111ad0072f4dabb1ec400fb782e85ade666213203c3a8ee` |

- **슈퍼패미컴 실기에서는 확인하지 않았습니다.**
- 기존 저장은 백업하고, 다른 버전의 강제저장 대신 새 게임 또는 일반 저장으로 시작하세요.
- 제작: **러브델릭(엔스헨데)**
- 글꼴: DOSSaemmul / DOSPilgi(leedheo), Dalmoori(달무리, RanolP). 출처·라이선스 고지는 ZIP에 포함했습니다.
- 출처와 버전을 표시하면 패치 재배포를 허용합니다. **공식 배포 주소 공유를 권장합니다.**

게임 ROM은 포함하지 않습니다. 자세한 적용법은 [README](https://github.com/enthhende/chacha-sfc-korean-patch#readme), 오류 제보는 [Issues](https://github.com/enthhende/chacha-sfc-korean-patch/issues)를 이용하세요.
