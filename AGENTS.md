# FreeRTOS-Kernel-Book-ko 작업 규칙

## 작업 시작

1. `README.ko.md`, `PROJECT_STATE.md`를 읽고 이번 요청의 범위를 확인한다.
2. `ko/STYLE_GUIDE.md`, `ko/GLOSSARY.md`, `ko/WORKFLOW.md`를 읽는다. 이 파일들이 번역의 현재 기준본이다.
3. `ko/translation-manifest.json`의 기준 commit·원문 blob과 실제 원문을 대조한다.
4. 그림을 다루면 `ko/assets/README.md`와 asset manifest를 읽고 원본을 직접 확인한다.

준비 작업과 본문 번역은 별도다. 저장소 준비 또는 그림 준비 요청만으로 본문 번역을 시작하지 않는다. 후속 번역 요청에 지정된 파일·절만 번역한다.

## 원문과 파생물

- 공식 원본은 `https://github.com/FreeRTOS/FreeRTOS-Kernel-Book`이다. 기존 ZIP·웹북·블로그를 원문 대신 사용하지 않는다.
- upstream에서 추적하는 영어 본문, 목차, 코드, 그림, 라이선스, submodule을 보존한다. 한국어판 공개 안내인 루트 `README.md`는 예외이며, 원래 소개는 `README.upstream.md`에 byte 단위로 보존한다.
- 한국어 본문은 `ko/`에 원문 파일명과 대응시켜 작성한다. 그림 한글화 결과는 `ko/assets/`에 둔다.
- `origin/main`은 한국어판 정본이다. `upstream`은 공식 영문 저장소이고, `upstream-baseline` branch와 manifest에 영문 기준선을 보존한다. 후속 변경은 `origin/main`에서 작업 branch를 만들고 한국어판 저장소에 PR로 제출한다.
- upstream 갱신은 번역과 별도 작업으로 진행한다. fetch만으로 manifest의 기준 commit을 바꾸지 않는다. 장별 변경과 기존 번역의 영향을 대조한 뒤 기준을 갱신한다.
- 사용자가 승인한 공개 정본은 `https://github.com/yunju-baek/FreeRTOS-Kernel-Book-ko`이다. 공식 upstream 기여는 별도 요청 범위이며, 한국어판 작업을 공식 저장소에 직접 push하거나 PR로 제출하지 않는다.

## 번역·그림 규칙

- 한다체, 영문 객체명과 첫 한국어 풀이, 용어집의 대표 표기를 따른다.
- 식별자·코드 블록·주석·문자열·로그는 그대로 유지한다. 설명은 코드 밖에 쓴다.
- 조건·예외·부정·수치·단위·상태 전이·호출 문맥을 보존한다. 원문에 없는 내용을 본문에 섞지 않는다.
- 삽입 그림도 한글화한다. Codex에서 원본을 보고 설명 문구를 번역한 파생 asset을 준비한다. 도형·화살표·축·시점·값·API·상태명은 보존한다.
- 실행 로그·실제 도구 화면·로고는 원문 증거를 보존한다. 한국어 설명을 분리하고 번역한 UI를 실제 제품 화면처럼 만들지 않는다.
- 원본과 파생 그림의 경로·hash·출처 위치·번역 문구·방법·검수 상태를 asset manifest에 기록한다. 미검수 또는 구조가 달라진 그림은 본문에 사용하지 않는다.
- 원문 오류 의심 사항은 위치·근거와 함께 `check-against-source`로 기록한다. 조용히 고치거나 불확실한 주장을 확정하지 않는다.
- 장·절·그림·예제 번호와 링크·anchor를 대조한다. 파일명에 들어 있는 번호보다 본문 caption의 번호를 우선한다.

## 상태와 검증

파일별 상태는 `not-started → draft → source-checked → language-reviewed → release-ready`다. 부분 번역은 `translated_sections`에 범위를 적고 장 전체 완료로 표시하지 않는다. 검토자의 종류와 실제 검토 범위를 기록하며 자동 검사로 사람 검토를 대신했다고 표시하지 않는다.

원문 보존, 코드·수치·조건 대응, 문체·용어, asset·링크·렌더링을 확인하고 변경 파일만 commit한다. `PROJECT_STATE.md`는 현재 결과와 다음 시작점으로 갱신한다. 예제 실행·실보드·PDF 검증은 실제 수행했을 때만 완료로 기록한다.

Codex·Claude의 세션·설정·인증 정보, 비밀키, 머신별 환경과 캐시는 저장소에 넣지 않는다. Python 환경과 `node_modules`는 iCloud 작업공간 밖에 둔다.
