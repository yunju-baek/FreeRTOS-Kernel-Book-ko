# 본문 번역과 그림 작업 병행

본문 번역용 작업 폴더를 별도 Git worktree로 준비했다. 같은 저장소의 이력을 공유하되 작업 파일과 branch가 분리되어 있다.

| 역할 | 작업 폴더 | branch | 담당 파일 |
| --- | --- | --- | --- |
| 그림·지침 | `FreeRTOS-Kernel-Book-ko/` | `docs/ko-translation-setup` | `ko/assets/`와 그림 관련 지침 |
| 본문 번역 | `FreeRTOS-Kernel-Book-ko-translate/` | `translate/korean-book` | `ko/chNN.md`, 한국어 부속 문서, `ko/translation-manifest.json` |

두 폴더는 `Cowork/FreeRTOS/` 아래에 있다. 본문 작업용 새 대화에서 아래 지시문을 사용한다. 이미 번역 중인 대화가 있다면 새 작업을 중복으로 시작하지 않고 같은 대화를 이어간다.

## 복사해서 사용할 지시문

```text
작업 폴더:
/Users/yunju/Library/Mobile Documents/com~apple~CloudDocs/Cowork/FreeRTOS/FreeRTOS-Kernel-Book-ko-translate

이 폴더의 AGENTS.md, README.ko.md, PROJECT_STATE.md를 먼저 읽는다.
ko/STYLE_GUIDE.md, ko/GLOSSARY.md, ko/WORKFLOW.md에 따라
공식 Kernel Book 본문 13장과 부속 문서 5개를 한국어로 번역한다.
이미 번역한 파일은 상태와 원문 대조 결과를 확인하고 이어서 작업한다.
원문 및 출력 파일 목록은 ko/translation-manifest.json을 따른다.

한다체를 쓰고 지정된 영문 객체명·API·식별자·코드·주석·로그는 보존한다.
조건·예외·부정·수치·단위·그림·예제 번호를 빠뜨리지 않는다.
공식 영문 파일과 media/, examples/는 수정하지 않는다.

그림은 다른 대화에서 준비하므로 ko/assets/를 수정하거나 재생성하지 않는다.
같은 상위 폴더의 FreeRTOS-Kernel-Book-ko/ko/assets/manifest.json을
읽기 전용으로 확인하고 target_path에 맞춰 본문 링크를 작성한다.
경로는 저장소 루트 기준이다. ko/chNN.md에서 ko/assets/foo.ko.png는
assets/foo.ko.png로, media/foo.jpg는 ../media/foo.jpg로 연결한다.
현재 worktree에 없는 그림의 표시 검수는 통합 후 할 항목으로 남긴다.

현재 branch translate/korean-book에서 작업한다.
다른 worktree의 branch를 checkout하거나 이미지 branch를 임의로 merge하지 않는다.
장별 원문 대조·한국어 검토를 수행하고 실제 상태를 본문 manifest에 기록한다.
번역 파일과 본문 상태만 명시적으로 stage하여 장별로 commit한다.
미해결 사항과 마지막 commit을 보고한다. 사람 검토 또는 배포 완료로 표시하지 않는다.
```

## 그림 반영 시 확인할 사항

준비 commit `29efc96` 이후 그림 53개와 원본 동일 사본 1개를 준비했다. 사용 위치 82개 모두 결과 경로가 있으며, 실제 파일별 검수 상태는 최신 asset manifest를 따른다. 초기 분류에서 바뀐 경로는 다음과 같다.

| 원본 | 최신 target_path | 이유 |
| --- | --- | --- |
| `media/image72.png` | `ko/assets/image72.ko.png` | event group 값과 bit 표제 한글화 |
| `media/image91.png` | `ko/assets/image91.ko.png` | 인터럽트 우선순위 설명 도표 한글화 |
| `media/image36.png` | `ko/assets/image36.ko.png` | 기존 예정 경로 유지. 원본과 byte가 같은 사본 |

나머지 원본 유지 그림은 [한국어 설명 목록](assets/PRESERVED_IMAGES.ko.md)을 참조한다. 원문 확인 항목인 그림 8.3의 semaphore 표현과 그림 10.3의 예제 번호를 조용히 고치지 않는다.

본문 작업 종료 뒤 별도 통합 branch/worktree에서 본문 branch와 그림 branch의 확정 commit을 합친다. `PROJECT_STATE.md`는 양쪽의 실제 완료 범위를 반영해 충돌을 해결한다. `ko/translation-manifest.json`은 본문 작업의 최신 결과를 유지하고, `ko/assets/manifest.json`은 그림 작업의 최신 결과를 유지한다. 이후 본문 이미지 링크 전수 검사, caption·alt·번호 대조와 실제 렌더링 검사를 진행한다. 작업 중인 본문 worktree에는 이 단계에서 손대지 않는다.
