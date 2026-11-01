# 한국어판 작업자 안내

독자는 [저장소 첫 화면](README.md)과 [한국어 목차](ko/toc.md)에서 시작한다. 이 문서는 번역·교정 작업자를 위한 안내다.

정본 원격은 `origin` → `https://github.com/yunju-baek/FreeRTOS-Kernel-Book-ko.git`, 정본 branch는 `main`이다. 공식 영문 원격은 `upstream` → `https://github.com/FreeRTOS/FreeRTOS-Kernel-Book.git`이다. 한국어판은 비공식 번역이며 공식 원본 저장소에 한국어 변경을 직접 push하지 않는다.

| 문서 | 용도 |
| --- | --- |
| [AGENTS.md](AGENTS.md) | 후속 작업의 규칙 |
| [현재 상태](PROJECT_STATE.md) | 완료 범위와 남은 검토 |
| [번역 지침](ko/STYLE_GUIDE.md) | 영어 유지, 한다체, 기술 의미 보존 |
| [용어집](ko/GLOSSARY.md) | 대표 표기와 첫 등장 풀이 |
| [작업 절차](ko/WORKFLOW.md) | branch·검수·PR 절차 |
| [검수 결과](ko/REVIEW.md) | 검수에서 수정한 내용과 실제 검사 범위 |
| [원문 대조 사항](ko/SOURCE_NOTES.md) | 원문 오기·불일치와 처리 방법 |
| [한국어 자료 조사](ko/RESEARCH.md) | 기존 발췌·해설 자료 조사 |
| [번역 manifest](ko/translation-manifest.json) | 기준 commit·blob·파일별 상태 |
| [그림 manifest](ko/assets/manifest.json) | 원본·번역 그림의 경로·hash·검수 |
| [병행 작업 안내](ko/IMAGE_HANDOFF.md) | worktree 사용과 그림 통합 규칙 |

한국어 정본은 `ko/`의 Markdown이다. 영문 본문과 `media/`, `examples/`, 원문 라이선스를 보존한다. 공개 저장소 소개를 위한 루트 `README.md`만 한국어판 안내로 교체했고, 원래 내용은 `README.upstream.md`로 보존했다. 원문 기준은 `ba20b2f820926587d5ee20ce312b3789d63f795c`이다.

검사는 `python3 tools/verify_translation.py --report publish/translation-validation.json`으로 재실행한다. 이 검사는 원문·코드·구조·경로 대응을 확인하며 문장의 정확성이나 예제 실행을 대신하지 않는다. 선택적 HTML 검수본은 `tools/render_review.py`로 생성한다.
