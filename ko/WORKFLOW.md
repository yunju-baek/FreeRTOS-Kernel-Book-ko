# 한국어판 수정·검수 절차

정본은 [yunju-baek/FreeRTOS-Kernel-Book-ko](https://github.com/yunju-baek/FreeRTOS-Kernel-Book-ko)의 `main`이다. 이미 번역된 본문 13장과 부속 문서 5종을 이 기준에서 수정한다. 원문 갱신과 번역 교정은 별도 변경으로 관리한다.

## 1. 시작과 범위

1. `AGENTS.md`, `PROJECT_STATE.md`, `STYLE_GUIDE.md`, `GLOSSARY.md`, `SOURCE_NOTES.md`를 읽는다.
2. Git 상태와 작업 branch를 확인한다. 미커밋 변경이 있으면 보존하고 작업을 겹치지 않는다.
3. `origin/main`을 fetch한 뒤 해당 기준에서 `review/<범위>` 또는 `translate/<범위>` branch를 만든다. 사용 중인 다른 worktree의 branch는 바꾸지 않는다.
4. `translation-manifest.json`의 원문 commit·blob을 확인한다. `upstream`을 fetch했다는 이유로 기준 commit을 자동 갱신하지 않는다.

## 2. 편집

원문 파일은 그대로 두고 `ko/`의 대응 파일만 수정한다. 코드·주석·문자열·로그와 기술 조건·단위·숫자를 보존한다. 원문 밖의 설명은 `[옮긴이 주]`로 구분한다. 원문 오류를 바로잡을 때는 `SOURCE_NOTES.md`에 원래 표현과 판단 근거를 함께 적는다.

그림은 `assets/manifest.json`의 검수된 `target_path`를 사용한다. 그림 변경은 원본 대조와 hash·검수 기록을 포함한다. 설명 도표의 한국어 문구를 검수하며, 실행 로그·실제 화면·로고의 원본 문자열을 임의 번역하지 않는다.

## 3. 검수

```sh
python3 tools/verify_translation.py --report publish/translation-validation.json
```

저장소 루트에서 실행한다. 원문 249개 파일의 보존, manifest의 원문 blob, 코드 블록, 제목 구조·번호, caption·각주·anchor, 로컬 링크, 그림 매핑과 hash를 검사한다. 원문 README는 `README.upstream.md`와 대조한다. 이 검사는 번역 의미, 외부 URL의 현재 응답, 예제 실행을 보증하지 않는다.

내용 검수에서는 조건·예외·부정·수치·단위·우선순위 방향·호출 문맥을 원문과 대조한다. 문체 검수에서는 한다체, 객체명, 첫 병기와 불필요한 직역을 확인한다. 표·코드·그림을 포함한 실제 표시도 확인한다.

선택적인 HTML 검수본은 pandoc 설치 후 다음 명령으로 생성한다. 결과는 `publish/review/`에 저장되며 Git에서 제외한다.

```sh
python3 tools/render_review.py
python3 -m http.server 8765 --bind 127.0.0.1
```

`http://127.0.0.1:8765/publish/review/toc.html`을 연다. PDF·예제 빌드·실보드 실행은 요청과 실제 수행 범위에 따라 별도로 기록한다.

## 4. 기록과 반영

- manifest의 review에는 검토자·종류·날짜·실제 범위·결과·미해결 사항을 기록한다. 과거 검수 기록을 현재 검수 결과로 오인하지 않게 한다.
- 상태는 `not-started → draft → source-checked → language-reviewed → release-ready`다. 부분 교정이나 자동 검사만으로 다음 단계 전체를 완료했다고 표시하지 않는다.
- 관련 파일만 명시적으로 stage하고 commit한 뒤 `origin`의 작업 branch로 push한다. 한국어판 저장소에 PR을 만든다. 사용자 승인 또는 저장소의 명시적 병합 규칙에 따라 `main`에 반영한다.
- 최초 공개 이후에도 원문 대조 사항은 유지한다. 사람의 전수 교열, 예제 실행, 원저자 확인 결과가 생기면 그 사실만 추가한다.

## 후속 작업 지시문

```text
FreeRTOS-Kernel-Book-ko의 AGENTS.md와 PROJECT_STATE.md를 읽는다.
ko/STYLE_GUIDE.md, ko/GLOSSARY.md, ko/WORKFLOW.md를 적용한다.
origin/main에서 작업 branch를 만든다.
대상: <파일·절과 수정 목적>
원문 기준은 ko/translation-manifest.json을 따른다.
영문 원본·코드·로그를 보존하고 ko/만 수정한다.
원문 오류는 ko/SOURCE_NOTES.md와 본문의 옮긴이 주로 구분한다.
구조 검사와 내용·표시 검수를 수행하고 실제 범위만 기록한다.
수정 파일을 commit/push하고 한국어판 저장소의 PR 주소를 보고한다.
```
