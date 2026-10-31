# 한국어판 작업 절차

이 문서는 별도 번역 작업을 시작할 때 사용한다. 본문 번역 요청이 있기 전에는 지침·원문·asset 준비 상태를 유지한다.

## 1. 작업 입력

- 원문: `translation-manifest.json`에 기록한 commit의 해당 파일과 blob
- 범위: 장 전체 또는 정확한 절 번호·시작/끝 문단
- 출력: 대응하는 `ko/chNN.md` 등
- 기준: `STYLE_GUIDE.md`와 `GLOSSARY.md`의 버전
- 문맥: 앞뒤 문단, 해당 장에서 이미 풀이를 병기한 용어
- 그림: `assets/manifest.json`의 원본–한국어 asset 대응과 검수 상태

초기 표본 후보는 4.7절 상태 설명과 5.3절 API 설명이다. 사용자가 다른 범위를 지정하면 그 범위를 따른다. 표본 번역이 장 전체 완료를 뜻하지 않는다.

## 2. 준비와 작성

1. `git status`, 현재 branch, 원문 commit과 blob을 확인한다. 준비 지침이 들어 있는 branch에서 `translate/ch04-states`처럼 범위를 드러내는 branch를 만든다.
2. 해당 원문을 읽고 용어·코드·조건·번호·그림의 대응을 확인한다. 원문 파일을 수정하지 않는다.
3. 지정한 범위만 한국어로 옮긴다. 미번역 절을 빈 제목으로 채우거나 완성된 장처럼 보이게 하지 않는다.
4. 원문 밖의 설명은 `[옮긴이 주]`로 분리하고 출처를 단다. 의심 항목에는 원문 위치와 판단 근거를 남긴다.
5. 그림은 검수된 한국어 asset을 연결한다. 코드·로그·실제 화면이 보존된 경우 대응 한국어 설명을 함께 사용한다. caption·alt·그림 번호도 대조한다.

## 3. 검수와 기록

1. 구조·내용: 문단·조건·예외·부정·비교·수치·단위·예제 번호를 원문과 대조한다.
2. 코드: fenced/indented/HTML 코드, API·설정·형·파일명·로그를 글자 단위로 대조한다. 코드 주석도 보존한다.
3. 문체: 한다체, 대표 용어, 첫 병기, 주체·동작·시점을 검토한다.
4. 그림: 번역 문구, 유지할 문자열, 도형·화살표·축·시간·값의 대응을 원본과 직접 비교한다. 생성 도구의 성공 응답만으로 통과시키지 않는다.
5. 연결·표시: 상대 경로, 영문 anchor, 목차, 이미지 비율, 표·코드의 실제 렌더링을 확인한다.
6. 상태: manifest의 `status`, `translated_sections`, `translated_at`, `reviews`를 실제 결과에 맞춰 갱신한다. review 항목에는 `stage`, `reviewer`, `reviewer_kind`, `date`, `scope`, `result`, `unresolved`를 기록한다.
7. 변경 목록: upstream 원본이 변하지 않았는지 확인하고 지정된 파생 파일만 commit한다. 현재 상태와 남은 검토를 `PROJECT_STATE.md`에 기록한다.

`draft`는 작성, `source-checked`는 원문 대조, `language-reviewed`는 한국어 검토, `release-ready`는 출처·라이선스·표시·미해결 사항까지 배포 요건을 확인한 상태다. 검토자가 Codex라면 `reviewer_kind: agent`로 기록한다. 사람의 검토가 필요한 항목은 `needs-human-check`로 남긴다.

원문 commit을 바꾸면 변경된 source blob에 대응하는 번역·그림을 다시 검토한다. 이전 검수 결과를 새 원문에 자동 적용하지 않는다.

## 4. 후속 작업 요청 양식

```text
FreeRTOS-Kernel-Book-ko의 AGENTS.md와 PROJECT_STATE.md를 먼저 읽는다.
ko/STYLE_GUIDE.md, ko/GLOSSARY.md, ko/WORKFLOW.md를 적용한다.

작업: 한국어 본문 번역
원문 commit: ba20b2f820926587d5ee20ce312b3789d63f795c
대상 파일: <chNN.md>
대상 범위: <장 전체 또는 정확한 절·문단 범위>
출력 파일: <ko/chNN.md>

영문 원본과 코드를 보존한다. 지정한 범위만 번역하고 문체를 이유로
조건·예외·부정·수치·단위를 생략하지 않는다. 그림은 ko/assets의 검수된
대응 asset을 사용하고 caption·alt와 원문 번호를 대조한다.
원문 대조·한국어 검토·링크·그림 검사를 수행하고 실제 검토자를 기록한다.
불확실한 항목은 위치·근거와 함께 별도로 보고한다.
manifest와 PROJECT_STATE.md에 실제 완료 범위 및 미해결 사항을 기록한다.
```

## 5. 원문 보존 확인

다음은 원문에 대한 수정·삭제·이름 변경·형 변경을 확인하는 읽기 전용 검사다. 한국어 준비 파일처럼 새로 추가한 파일은 결과에서 제외한다.

```sh
git diff --name-status --diff-filter=CDMRTUXB ba20b2f820926587d5ee20ce312b3789d63f795c -- .
git submodule status --recursive
git submodule foreach --recursive 'git status --porcelain'
```

첫 명령이 비어 있고 submodule이 기록된 commit에서 clean하더라도 번역 내용·그림의 정확성과 예제 실행을 검증한 것은 아니다. 각 검수 결과를 따로 기록한다.
