# FreeRTOS-Kernel-Book-ko 현재 상태

갱신일: 2026-11-01

## 완료한 준비

- 공식 `FreeRTOS/FreeRTOS-Kernel-Book`을 이 이름으로 직접 full clone했다.
- 원문 기준은 `ba20b2f820926587d5ee20ce312b3789d63f795c`이다. Git 이력과 예제의 재귀 submodule 3개를 확보했다.
- 원격 영문 저장소 이름은 `upstream`, 준비 branch는 `docs/ko-translation-setup`이다.
- `README.ko.md`, `AGENTS.md`, `ko/STYLE_GUIDE.md`, `ko/GLOSSARY.md`, `ko/RESEARCH.md`, `ko/WORKFLOW.md`에 후속 번역 기준을 정리했다.
- `ko/translation-manifest.json`에 본문 13장·부속 문서 5개의 원문 blob과 미착수 상태를 기록했다. 본문 번역은 별도 작업이다.

## 그림 준비

`media/` 원본 86개 중 본문·표제·저작권에서 참조하는 이미지는 82개다. 설명 도표 53개를 한글화하고 Codex가 원본과 직접 대조했다. 실행 로그·도구 화면 26개, 로고 2개, task 이름만 있는 도표 1개는 원본 문자열·값을 보존하고 한국어 설명으로 연결한다. 미사용 원본 4개도 보존했다.

결과는 `ko/assets/`의 한글화 PNG 53개와 원본 동일 사본 1개다. `ko/assets/index.html`은 원본·결과 비교 페이지이며, 원본을 유지하는 그림의 설명은 `ko/assets/PRESERVED_IMAGES.ko.md`에 있다. 파일별 경로·hash·프롬프트·검수 상태는 `ko/assets/manifest.json`이 기준이다. `review/`의 수정 전 후보는 본문에 사용하지 않는다.

원문 보존·파일 존재·hash와 Codex의 시각 대조를 확인했다. 본문과 합친 표시 검수와 사람의 최종 검토는 남아 있다. 그림 8.3의 원문 semaphore 표현과 그림 10.3의 원문 예제 번호는 원문 확인 항목으로 남겼다.

비교 페이지의 이미지·문서 경로 검사는 통과했다. 브라우저 도구의 `file://` 접근 정책에 따라 페이지 열기가 거부되어 화면 표시와 검색 동작은 브라우저에서 검수하지 못했다. 개별 그림의 원본·결과 대조와 구분한다.

## 병행 작업 규칙

- 그림 작업자는 `ko/assets/`와 그림 관련 지침을 맡는다.
- 본문용 worktree는 같은 상위 폴더의 `FreeRTOS-Kernel-Book-ko-translate/`, branch는 `translate/korean-book`이다. 시작 기준은 준비 commit `29efc96`이다. 이 준비 branch의 본문 manifest는 준비 시점의 상태이며, 병행 번역의 최신 진척은 본문 worktree에서 확인한다.
- 본문 작업자는 별도 Git worktree에서 `ko/chNN.md` 등 번역 본문과 본문 manifest를 맡는다. 원래 작업공간의 branch를 checkout하지 않는다.
- 그림이 준비 중이어도 manifest의 예정 경로로 본문 번역을 진행할 수 있다. 해당 그림의 표시 검수는 보류하고 작업 종료 시 미해결 항목으로 적는다.
- 서로의 파일을 수정하지 않는다. 이미지 반영은 그림 commit을 확인한 뒤 별도 통합 단계에서 수행한다. 작업 시작 방법은 `ko/WORKFLOW.md`를 따른다.
- 병행 작업 지시문과 경로 변경 사항은 `ko/IMAGE_HANDOFF.md`를 따른다. 본문 작업 중인 worktree에 임의로 merge하거나 branch를 바꾸지 않는다.

## 검증 경계와 다음 시작점

영문 원본·코드·라이선스는 보존한다. 예제 빌드·실행, 하드웨어 실행, PDF·웹 배포는 수행하지 않았다. 한국어판용 GitHub 원격은 아직 생성하지 않았다.

다음 본문 작업은 별도 요청에 지정된 범위를 번역하고 원문·문체·코드·링크·그림을 검수한다. `not-started → draft → source-checked → language-reviewed → release-ready`로 실제 상태를 기록한다. 원문 버전이 바뀌면 영향을 다시 대조한다.
