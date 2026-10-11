# 빨간망토 차차 SFC 한글패치 v1.0.0

이야기 대사와 타이틀·세이브·전투·소지품·상태 메뉴를 한국어로 바꾼 패치입니다.

**[한국어 공략](https://enthhende.github.io/games/chacha/guide/) · [패치 안내](https://enthhende.github.io/games/chacha/patch/)**

## 간단한 적용법

**[브라우저에서 한글패치 적용](https://enthhende.github.io/games/chacha/patch/apply/)** → 일본판 원본 선택 → **한글 ROM 만들기 → 한글 ROM 저장**. Windows·macOS·Linux에서 설치나 명령어 입력 없이 사용할 수 있습니다. ROM은 브라우저 안에서만 처리되며 서버로 전송되지 않습니다.

오프라인으로 쓰려면 **[chacha-sfc-korean-patch-v1.0.0-easy.zip](https://github.com/enthhende/chacha-sfc-korean-patch/releases/download/v1.0.0/chacha-sfc-korean-patch-v1.0.0-easy.zip)**을 받아 압축을 풉니다.

- **Windows:** `apply-patch.bat` 더블클릭 후 화면에서 원본을 선택합니다. PowerShell 명령이나 Python 설치는 필요 없습니다.
- **macOS·Linux:** `apply-patch.html`을 브라우저로 엽니다.
- BPS·xdelta 적용 프로그램을 쓰는 분은 `patches/`에서 한 형식만 골라 일본판 원본에 적용하세요. **xdelta도 SFC에 사용할 수 있습니다.**

두 패치 형식과 브라우저 적용 도구는 동일한 v1.0.0 한글 ROM을 만듭니다. 기존 BPS 파일과 게임 내용은 그대로입니다. `chacha-sfc-korean-patch-v1.0.0.zip`은 기존 BPS·Python 도구 패키지이며, 처음 받는 분은 **easy.zip**을 사용하세요.

| 파일 | 크기 | SHA-256 |
|---|---:|---|
| 일본판 원본 | 1,572,864바이트 | `f5e41c877ed95a66e171735dbf99f86fd972e6dd7687379ed550baa45cf08151` |
| BPS 패치 | 424,773바이트 | `8fc0e0980967acd31f54562f8786fc41b5c1fad028a42f78860774364a29465f` |
| xdelta 패치 | 406,548바이트 | `02828bc86e06ab3d2a82faf05b29363f72b74292cd638c89b4d43502242450dc` |
| 패치 후 ROM | 2,097,152바이트 | `a8edfb9b3df082783111ad0072f4dabb1ec400fb782e85ade666213203c3a8ee` |

- **슈퍼패미컴 실기에서는 확인하지 않았습니다.**
- 기존 저장은 백업하고, 다른 버전의 강제저장 대신 새 게임 또는 일반 저장으로 시작하세요.
- 제작: **러브델릭(엔스헨데)**
- 글꼴: DOSSaemmul / DOSPilgi(leedheo), Dalmoori(달무리, RanolP). 출처·라이선스 고지는 ZIP에 포함했습니다.
- 출처와 버전을 표시하면 패치 재배포를 허용합니다. **공식 배포 주소 공유를 권장합니다.**

게임 ROM은 포함하지 않습니다. 자세한 적용법은 [README](https://github.com/enthhende/chacha-sfc-korean-patch#readme), 오류 제보는 [Issues](https://github.com/enthhende/chacha-sfc-korean-patch/issues)를 이용하세요.
