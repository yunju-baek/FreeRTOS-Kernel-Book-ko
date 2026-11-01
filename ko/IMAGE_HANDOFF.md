# 본문·그림 병행 작업과 통합 상태

2026-11-01에 본문 번역과 한글 그림을 통합했다. 현재 정본은 한국어판 저장소의 `main`이다. 이전 작업 폴더를 번역 전 상태로 되돌리거나 그림 준비를 다시 시작하지 않는다.

| 구분 | 이력·경로 |
| --- | --- |
| 한국어 정본 | `FreeRTOS-Kernel-Book-ko/`, `origin/main` |
| 기존 번역 worktree | `FreeRTOS-Kernel-Book-ko-translate/`, `review/korean-book-20261101` |
| 최초 번역 이력 | `translate/korean-book`, commit `6e6cc39` |
| 그림 준비 이력 | `docs/ko-translation-setup`, commit `509323e` |
| 최초 통합 | commit `d356e5a` |

본문 그림 참조 82개는 `assets/manifest.json`의 대응 경로를 사용한다. 한글화 도표 53개와 원본 유지 자료 29개를 구분한다. `image36.ko.png`는 원본과 byte가 같은 사본이며, 나머지 실행 로그·실제 화면·로고는 `../media/`를 참조한다. 수정 전 후보가 들어 있는 `assets/review/`는 본문에 사용하지 않는다.

후속 작업을 병행할 경우 두 작업자가 동일한 `origin/main` 기준에서 각기 다른 worktree·branch를 사용한다. 본문 담당자는 `ko/chNN.md`와 번역 manifest를, 그림 담당자는 `ko/assets/`와 asset manifest를 수정한다. 상대 작업 중인 branch를 임의 checkout하거나 merge하지 않는다.

통합할 때는 양쪽의 확정 commit을 확인하고, 본문 manifest와 그림 manifest의 실제 최신 상태를 각각 보존한다. 통합 후 `tools/verify_translation.py`, caption·alt·번호 대조, 원본과 번역 그림의 시각 대조 및 실제 표시 검수를 수행한다. 그림 준비 중 작성한 링크라도 파일이 실제 존재하고 검수를 통과하기 전에는 완료로 기록하지 않는다.
