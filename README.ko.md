# FreeRTOS-Kernel-Book-ko

[FreeRTOS/FreeRTOS-Kernel-Book](https://github.com/FreeRTOS/FreeRTOS-Kernel-Book)을 직접 clone한 비공식 한국어판 작업 저장소다. 원저는 Richard Barry와 The FreeRTOS Team의 *Mastering the FreeRTOS Real Time Kernel*이다.

현재 범위는 번역 지침 정리와 한국어 그림 asset 준비다. 본문 번역은 별도 작업 요청에서 지정한 범위에 한해 진행한다.

## 시작할 때 읽을 문서

| 문서 | 용도 |
| --- | --- |
| [AGENTS.md](AGENTS.md) | 후속 작업자가 따라야 할 규칙 |
| [현재 상태](PROJECT_STATE.md) | 완료 범위와 다음 시작점 |
| [번역 지침](ko/STYLE_GUIDE.md) | 영어 유지, 한다체, 의미·코드·그림 보존 |
| [용어집](ko/GLOSSARY.md) | 객체명과 운영체제 개념의 대표 표기 |
| [한국어 자료 조사](ko/RESEARCH.md) | 기존 한국어 해설의 출처·성격·주의점 |
| [작업 절차와 요청 양식](ko/WORKFLOW.md) | 장·절별 작업 시작과 검수 방법 |
| [원문과 번역 상태](ko/translation-manifest.json) | 원문 commit·blob, submodule, 파일별 상태 |
| [그림 asset 안내](ko/assets/README.md) | 그림 한글화 기준, 원본 대응과 검수 |
| [병행 번역 인계](ko/IMAGE_HANDOFF.md) | 별도 worktree에서 번역을 시작하는 지시문과 그림 통합 방법 |
| [그림 비교 페이지](ko/assets/index.html) | 원본과 한글화 도표 53개의 비교 |

## 원문과 작업본

- 공식 원격: `upstream` → `https://github.com/FreeRTOS/FreeRTOS-Kernel-Book.git`
- 원문 기준: `ba20b2f820926587d5ee20ce312b3789d63f795c`
- 로컬 이름: `FreeRTOS-Kernel-Book-ko`
- `main`: clone 시점의 공식 영문 기준선
- 준비 branch: `docs/ko-translation-setup`
- 원본: 루트의 `ch01.md`–`ch13.md`, 부속 문서, `media/`, `examples/`
- 향후 한국어 본문: `ko/chNN.md` 등 원문에 대응하는 경로
- 한국어 그림: `ko/assets/`; 영어 원본은 `media/`에 보존

전체 Git 이력과 재귀 submodule을 clone했다. 기존 수집 ZIP을 새 저장소로 초기화한 것이 아니다. 예제 빌드·실행은 별도 검증 대상이다. 한국어판용 GitHub 원격은 아직 만들지 않았다.

## 편집 기준

본문은 한다체를 사용한다. task, queue, mutex 등 지정 객체명과 공식 상태명은 영어로 유지하고 장의 첫 등장에 한국어 풀이를 붙인다. API·매크로·파일·코드·로그는 원문 문자열을 보존한다. 조건·예외·부정·수치·단위·상태 전이는 문체보다 우선한다.

삽입 그림의 설명 문구도 한국어로 옮긴다. Codex에서 원본과 대조하며 별도 asset으로 만들고, 그림의 API·코드·로그와 실측 값은 보존한다. 번역 작업은 검수된 asset 대응표를 사용하며 임의로 원본 그림을 덮어쓰지 않는다.

## 출처와 라이선스

원문의 저작권·면책 고지와 [LICENSE](LICENSE), [LICENSE-SUMMARY](LICENSE-SUMMARY), [LICENSE-SAMPLECODE](LICENSE-SAMPLECODE)를 그대로 보존한다. 책의 문서는 CC BY-SA 4.0, sample code와 accompanying examples는 저장소에 명시된 modified MIT를 따른다. submodule은 각 저장소의 라이선스를 유지한다.

한국어 문서와 그림의 번역·변경 사실을 표시하고, 원문 URL·기준 commit·원저자·원문 및 개별 자료의 고지를 유지한다. 이 한국어판의 문서·그림 파생물은 원문과 같은 CC BY-SA 4.0으로 제공한다. 공식 FreeRTOS/AWS 번역 또는 공식 검수본으로 표시하지 않는다.
