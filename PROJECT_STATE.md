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

- **ch01.md (1 머리말)**: 번역 및 `source-checked` 검수 완료 (`ko/ch01.md`). 제목은 사용자 요청에 따라 `한글(영어)` 병기 형식을 적용하고 영문 원본 앵커 ID를 보존함.
- **ch02.md (2 FreeRTOS 커널 배포판)**: 번역 및 `source-checked` 검수 완료 (`ko/ch02.md`). 디렉터리 트리, Listing 2.1 코드 템플릿, 표 1~4, 한글(영어) 병기 제목 및 영문 앵커 ID 적용 완료.
- **ch03.md (3 힙 메모리 관리)**: 번역 및 `source-checked` 검수 완료 (`ko/ch03.md`). heap_1~heap_5 상세 설명, C 코드 Listing 3.1~3.15, 한글(영어) 병기 제목 및 영문 앵커 ID 적용 완료. 그림 3.1~3.4는 `assets/image05.ko.png`~`image08.ko.png`로 연결하였으며 Codex 이미지 병행 작업 완료 후 시각적 표시 검수 예정 (`needs-image-check`).
- **ch04.md (4 태스크 관리)**: 번역 및 `source-checked` 검수 완료 (`ko/ch04.md`). task 생성(xTaskCreate), 우선순위, 상태 머신(Ready/Running/Blocked/Suspended), vTaskDelay, vTaskDelayUntil, idle task hook, vTaskPrioritySet, vTaskDelete, TLS, 3가지 스케줄링 알고리즘(선점형+시분할, 시분할 없는 선점형, 협력형), 코드 Listing 4.1~4.30 100% 보존 완료. 그림 4.1~4.22 자산 링크 연결 완료 (`needs-image-check`).
- **ch05.md (5 큐 관리)**: 번역 및 `source-checked` 검수 완료 (`ko/ch05.md`). 28개 헤딩 `한글(영어)` 병기, 32개 Listing 코드 100% 보존, Figure 5.1~5.7 자산 링크 매핑 완료 (`needs-image-check`).
- **ch06.md (6 인터럽트 관리)**: 번역 및 `source-checked` 검수 완료 (`ko/ch06.md`). 22개 헤딩 `한글(영어)` 병기, 16개 Listing 코드 100% 보존, Figure 6.1~6.10 자산 링크 매핑 완료, 각주 `[^10]`, `[^11]` 보존 완료 (`needs-image-check`).
- **ch07.md (7 소프트웨어 타이머 관리)**: 번역 및 `source-checked` 검수 완료 (`ko/ch07.md`). 25개 헤딩 `한글(영어)` 병기, 24개 Listing 코드 100% 보존, Figure 7.1~7.15 자산 링크 매핑 완료, 각주 `[^12]`~`[^22]` (11개) 보존 완료 (`needs-image-check`).
- **ch08.md (8 자원 관리)**: 번역 및 `source-checked` 검수 완료 (`ko/ch08.md`). 18개 헤딩 `한글(영어)` 병기, 21개 Listing 코드 100% 보존, Figure 8.1~8.8 자산 링크 매핑 완료, 각주 `[^23]` 보존 완료 (`needs-image-check`).
- **ch09.md (9 이벤트 그룹)**: 번역 및 `source-checked` 검수 완료 (`ko/ch09.md`). 16개 헤딩 `한글(영어)` 병기, 14개 Listing 코드 100% 보존, Figure 9.1~9.5 자산 링크 매핑 완료, 각주 `[^24]`~`[^26]` (3개) 보존 완료 (`needs-image-check`).
- **ch10.md (10 태스크 알림)**: 번역 및 `source-checked` 검수 완료 (`ko/ch10.md`). 20개 헤딩 `한글(영어)` 병기, 18개 Listing 코드 100% 보존, Figure 10.1~10.6 자산 링크 매핑 완료 (`needs-image-check`).
- **ch11.md (11 저전력 지원)**: 번역 및 `source-checked` 검수 완료 (`ko/ch11.md`). 11개 헤딩 `한글(영어)` 병기, 7개 Listing 코드 100% 보존 완료.
- **ch12.md (12 개발자 지원)**: 번역 및 `source-checked` 검수 완료 (`ko/ch12.md`). 20개 헤딩 `한글(영어)` 병기, 12개 Listing 코드 100% 보존, Figure 12.1~12.8 및 디버거 스크린샷 매핑 완료.
- **ch13.md (13 문제 해결)**: 번역 및 `source-checked` 검수 완료 (`ko/ch13.md`). 20개 헤딩 `한글(영어)` 병기, 3개 Listing 코드 100% 보존, Figure 13.1(image91) 매핑, 각주 `[^28]` 보존 완료.
- **부속 문서 5종 (Front/Back Matter)**: 번역 및 `source-checked` 검수 완료 (`ko/booktitle.md`, `ko/toc.md`, `ko/abbreviations.md`, `ko/copyright.md`, `ko/dedication.md`).
  - `ko/toc.md`: 585개 링크 100% 검증 (깨진 링크 0개), 273개 헤딩 및 312개 예제·그림·코드·표 항목 `한글(영어)` 병기 매핑 완료.
  - `ko/booktitle.md`: 표제, 부제, 저자, 버전 및 상표 각주 번역 완료.
  - `ko/abbreviations.md`: 17개 표준 약어 영한 대역 테이블 작성 완료.
  - `ko/copyright.md`: 저작권, 피드백 안내 및 AWS 로고 링크 완료.
  - `ko/dedication.md`: 헌사 번역 완료.
- **전체 완료 상태**: 본문 13개 챕터 및 부속 문서 5종(총 18개 문서) 100% 번역 및 원문 검증(`source-checked`) 완료.
