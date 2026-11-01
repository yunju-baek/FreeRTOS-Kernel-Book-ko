# FreeRTOS Kernel Book 한국어판 현재 상태

갱신일: 2026-11-01

## 정본

- 공개 정본: `https://github.com/yunju-baek/FreeRTOS-Kernel-Book-ko`, `origin/main`
- 로컬 정본 폴더: `FreeRTOS-Kernel-Book-ko/`
- 공식 원문: `https://github.com/FreeRTOS/FreeRTOS-Kernel-Book`, remote `upstream`
- 영문 기준 commit: `ba20b2f820926587d5ee20ce312b3789d63f795c`; `upstream-baseline` branch와 manifest에 보존
- 한국어 정본: `ko/`의 Markdown과 검수된 `ko/assets/`
- 비공식 번역임을 루트 README와 한국어 표제에 표시했다. 원문 README는 `README.upstream.md`에 보존한다.

## 완료 범위

1. 본문 13장과 부속 문서 5종을 번역하고 한글화 그림을 통합했다. 6장은 software timer, 7장은 interrupt 관리다.
2. 원문과 다른 코드 블록 18개를 복구했다. 현재 205개 fenced code block 전체가 원문과 동일하다. 용어·caption·목차·alt·그림 경로와 발견한 기술 번역 오류를 교정했다.
3. 설명 도표 53개는 한글화 후 Codex가 원본과 시각 대조했다. 로그·도구 화면·로고 등 29개는 원본을 유지했다. 사용 위치 82개 모두 target 매핑과 hash를 확인했다. 원본 이미지 86개도 보존했다.
4. 원문 파일 249개, 번역 구조·caption 번호·각주·anchor·목차 585개 링크와 로컬 경로를 검사했다. `tools/verify_translation.py`와 `publish/translation-validation.json`에 재현 방법·결과가 있다.
5. pandoc HTML 검수본 20개(번역 18개와 검수·원문 대조 문서 2개)를 생성했다. 브라우저에서 이미지 82개 로드와 가로 넘침 없음, 대표 도표·표의 표시를 확인했다. HTML은 정본이 아니며 `publish/review/`에서 재생성한다.
6. 번역 지침은 v0.5, 용어집은 v0.4다. 1~4장의 상단 YAML front matter를 제거했다. 나머지 14개를 포함한 전체 18개 문서에 헤더가 없음을 확인했으며, 메타데이터는 manifest에서 관리한다. 같은 영어를 반복한 병기 26곳과 파일명 내부 풀이 1곳을 바로잡고, 캡션 313개의 영어 종류·번호를 제거했다. 원문 오기·불일치 15개는 `ko/SOURCE_NOTES.md`, 상세 검수 범위는 `ko/REVIEW.md`에 기록했다.

## 보존한 작업 이력

- 최초 번역: `translate/korean-book`, `6e6cc39`
- 그림 준비: `docs/ko-translation-setup`, `509323e`
- 통합·검수 worktree: `FreeRTOS-Kernel-Book-ko-translate/`, `review/korean-book-20261101`
- 기존 번역·그림 이력은 merge 이력으로 보존한다. 현재 정본 작업은 `origin/main`에서 새 branch를 만들어 진행한다.

## 검증 경계와 다음 작업

현재 파일 상태는 `source-checked`이다. 기술 조건 중심 대조와 용어·caption 교정은 했지만, 사람의 최종 전수 교열·예제 빌드·실행·실보드·PDF 검증은 수행하지 않았다. 공개와 `release-ready` 판정은 구분한다.

N03(SMP idle stack 단위)과 N07(mutex 도표의 semaphore 표현)은 `check-against-source`로 남긴다. N09(stack high-water mark)는 동봉 커널과 원문 단위의 차이를 확인해 주석으로 설명했다. 후속 교정은 이 항목과 장별 문장 검토에서 시작한다.

이후 변경은 한국어판 저장소의 작업 branch와 PR로 관리한다. 공식 영문 파일·코드·로그·라이선스를 보존하고 번역 원문 기준을 임의 갱신하지 않는다. `ko/WORKFLOW.md`를 따른다.
