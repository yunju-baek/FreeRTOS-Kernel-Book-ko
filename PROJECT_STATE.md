# FreeRTOS-Kernel-Book-ko 현재 상태

갱신일: 2026-11-01

## 완료한 준비

- 공식 `FreeRTOS/FreeRTOS-Kernel-Book`을 이 이름으로 직접 full clone했다.
- 원문 기준은 `ba20b2f820926587d5ee20ce312b3789d63f795c`이다. Git 이력과 예제의 재귀 submodule 3개를 확보했다.
- 원격 영문 저장소 이름은 `upstream`, 준비 branch는 `docs/ko-translation-setup`이다.
- `README.ko.md`, `AGENTS.md`, `ko/STYLE_GUIDE.md`, `ko/GLOSSARY.md`, `ko/RESEARCH.md`, `ko/WORKFLOW.md`에 후속 번역 기준을 정리했다.
- `ko/translation-manifest.json`에 본문 13장·부속 문서 5개의 원문 blob과 미착수 상태를 기록했다. 본문 번역은 별도 작업이다.

## 그림 준비

`media/` 원본 86개 중 본문·표제·저작권에서 참조하는 이미지는 82개다. 설명 도표 52개는 한글화 대상이다. 실행 로그·도구 화면 27개, 로고 2개, 숫자 전용 도표 1개는 원본 문자열·값을 보존하고 한국어 설명으로 연결한다. 미사용 원본 4개는 보존한다.

Codex에서 `ko/assets/`에 한국어 그림을 준비하고 있다. 파일별 경로·진행·검수 상태는 `ko/assets/manifest.json`이 기준이다. 생성·검수하지 않은 그림을 준비 완료로 취급하지 않는다.

## 병행 작업 규칙

- 그림 작업자는 `ko/assets/`와 그림 관련 지침을 맡는다.
- 본문 작업자는 별도 Git worktree에서 `ko/chNN.md` 등 번역 본문과 본문 manifest를 맡는다. 원래 작업공간의 branch를 checkout하지 않는다.
- 그림이 준비 중이어도 manifest의 예정 경로로 본문 번역을 진행할 수 있다. 해당 그림의 표시 검수는 보류하고 작업 종료 시 미해결 항목으로 적는다.
- 서로의 파일을 수정하지 않는다. 이미지 반영은 그림 commit을 확인한 뒤 별도 통합 단계에서 수행한다. 작업 시작 방법은 `ko/WORKFLOW.md`를 따른다.

## 검증 경계와 다음 시작점

영문 원본·코드·라이선스는 보존한다. 예제 빌드·실행, 하드웨어 실행, PDF·웹 배포는 수행하지 않았다. 한국어판용 GitHub 원격은 아직 생성하지 않았다.

- **ch01.md (1 머리말)**: 번역 및 `source-checked` 검수 완료 (`ko/ch01.md`). 제목은 사용자 요청에 따라 `한글(영어)` 병기 형식을 적용하고 영문 원본 앵커 ID를 보존함.
- **다음 시작점**: `ch02.md` (2 The FreeRTOS Kernel Distribution) 번역 착수.
