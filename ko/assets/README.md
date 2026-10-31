# 한국어 그림 asset

공식 원본 `../../media/`를 보존하고, 삽입 도표의 설명 문구를 Codex에서 한국어로 옮긴 파생 이미지다. [manifest.json](manifest.json)에 원본–결과 경로, 원본 hash, 사용 위치, 처리 방식, 생성 지시문과 검수 결과를 기록한다.

## 표기와 보존

- 설명 문구는 한국어로 옮기고 [용어집](../GLOSSARY.md)을 따른다. task·queue·mutex·stack 같은 지정 객체명과 Running·Ready·Blocked 등 공식 상태명은 영어를 유지한다.
- API·매크로·변수·파일명·코드·로그·실측 값·비트·주소·단위는 보존한다. 원문의 수치가 의심스러워도 조용히 바꾸지 않는다.
- 도형 개수, 연결, 화살표 방향, 시간 순서, 눈금·막대·영역의 상대 관계와 색상 의미를 유지한다. 비율을 강제로 늘이거나 찌그러뜨리지 않는다.
- 원본 UI·실행 로그·로고는 직접 번역해 실제 화면처럼 만들지 않는다. 원본을 유지하고 한국어 caption·설명으로 읽기를 돕는다.
- 파일명 속 번호와 본문 caption이 다르면 본문 caption을 기준으로 연결하고 차이를 기록한다. 예: `figure_4.11_example_4.6_execution_pattern.png`의 본문 번호는 그림 4.12다.

## manifest 상태

| 상태 | 의미 | 본문 처리 |
| --- | --- | --- |
| `pending` | 한글화 예정, 결과 파일 없음 | 예정 경로를 사용하되 그림 표시 검수는 보류 |
| `generated` | 결과 생성, 검수 전 | 완료 그림으로 사용하지 않음 |
| `agent-checked` | Codex가 원본과 문구·구조를 직접 대조 | 번역 초안에 연결 가능, 사람 검토로 표시하지 않음 |
| `needs-revision` | 문구·구조 등의 수정 필요 | 완료 그림으로 사용하지 않음 |
| `preserve-original` | 로그·UI·로고·숫자 등 원본 유지 대상 | 원본 경로와 한국어 caption·설명 사용 |
| `not-used` | 현재 책에서 참조하지 않는 원본 | 보존만 함 |

`target_path`는 저장소 루트 기준이다. 예를 들어 `ko/ch04.md`에서는 `ko/assets/foo.ko.png`를 `assets/foo.ko.png`로, `media/foo.jpg`를 `../media/foo.jpg`로 연결한다.

## 병행 본문 작업

그림 담당 Codex가 이 폴더를 소유한다. 본문 작업자는 asset을 재생성하거나 이 manifest를 수정하지 않는다. 미완료 asset 때문에 본문 번역을 중단할 필요는 없으나, 해당 그림의 표시·한글화 검수를 완료했다고 기록하면 안 된다. 그림 commit을 받은 뒤 통합 worktree에서 연결과 실제 표시를 확인한다.

## 제작과 검수

원본을 먼저 보고 `imagegen`의 기본 내장 도구로 설명 도표를 편집한다. 생성 결과를 이 폴더로 복사한다. 프롬프트는 manifest에 보존한다. 출력의 한국어·원문 유지 문자열·구조·그림 비율을 원본과 대조하고 결과 hash와 검사 범위를 기록한다. 자동 생성 성공은 검수 통과가 아니다.

파생 그림은 원문의 CC BY-SA 4.0을 따른다. 원저자는 Richard Barry·The FreeRTOS Team이며, 원문은 `FreeRTOS/FreeRTOS-Kernel-Book` commit `ba20b2f820926587d5ee20ce312b3789d63f795c`이다. 개별 그림·인용의 고지도 유지한다. 한글화는 비공식 번역·변경 작업이다.
