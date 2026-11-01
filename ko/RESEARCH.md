# FreeRTOS Kernel Book 한국어 자료 조사

조사일: 2026-11-01 (Asia/Seoul)

대상: Richard Barry·The FreeRTOS Team의 *Mastering the FreeRTOS Real Time Kernel*

방법: 웹 검색, 작성자 게시물 열람, AWS 영문·한국어 문서 대조, GitHub API의 저장소·트리·브랜치·릴리스 확인

성격: 번역 준비용 조사. 타인의 번역문·그림을 수집해 합치는 작업은 수행하지 않았다.

현재 기준 문서: [번역 지침 v0.2](STYLE_GUIDE.md), [용어집 v0.2](GLOSSARY.md). 아래는 clone 전에 작성한 2026-11-01 조사 기록이다. 이후 공식 저장소를 `FreeRTOS-Kernel-Book-ko`로 직접 clone했으며, 현재 상태는 [PROJECT_STATE.md](../PROJECT_STATE.md)를 따른다.

## 1. 확인 결과

공식 Kernel Book 저장소의 현재 `main` 트리와 공개 릴리스에서 한국어판을 확인하지 못했다. 공개 검색에서도 장별 완역본이나 한국어 번역 저장소를 확인하지 못했다. 이는 이번 조사 범위의 결과이며, 모든 비공개 자료·포크·출판 기록에 한국어판이 없다는 뜻은 아니다.

공식 AWS 한국어 FreeRTOS 사용자 가이드는 존재한다. 커널북을 인용한 한국어 해설도 확인했다. 다만 한국어 해설, 영문 PDF 소개, 일반 FreeRTOS 교재를 커널북의 번역판으로 분류할 근거는 부족하다.

앞선 답변의 표현은 다음과 같이 바로잡는다.

| 앞선 주장 | 이번 조사에 근거한 표현 |
| --- | --- |
| 공식 한글판은 없다 | 확인한 공식 저장소·릴리스에서 Kernel Book 한국어판을 찾지 못했다 |
| 국내 정식 번역서는 없다 | 이 책의 국내 번역 출판은 확인하지 못했다. FreeRTOS를 다룬 한국어 저술과 구분한다 |
| 발췌번역이 널리 공유되어 있다 | 커널북 그림·페이지를 인용한 해설은 확인했다. 원문과 대응하는 발췌번역의 규모·범위는 확인하지 못했다 |
| 작업공간에 한글판이 이미 있다 | 기존 `_ko` 자료는 강의·실습 설명이다. 커널북 한국어판과 별개다 |

## 2. 공식 원본과 버전

| 항목 | 관찰 결과 |
| --- | --- |
| 저장소 | [FreeRTOS/FreeRTOS-Kernel-Book](https://github.com/FreeRTOS/FreeRTOS-Kernel-Book) |
| 조사 시 `main` commit | `ba20b2f820926587d5ee20ce312b3789d63f795c` |
| commit 시각 | 2026-04-03 21:24:44 UTC |
| commit 제목 | `Fix more typos (#112)` |
| 원문 범위 | `ch01.md`–`ch13.md`, 목차·표제·헌사·약어·저작권 문서, `media/`, `examples/` |
| 브랜치 목록 | `main`, `KeishiSonoda-patch-1`. 이름만으로 다른 브랜치의 언어를 판정하지 않았다 |
| 공개 릴리스 | `V1.1.0`, `V1.0`. 각 릴리스에 해당 영문 PDF 1개가 있다 |
| 예제 submodule | `examples/Win32-simulator-MSVC/FreeRTOS-Kernel` → `18ed8886fe3eed9dbe433a82cdc62ce5dc0315eb` |
| 로컬 기존 원본 | `FreeRTOS_강의자료_원천수집/raw/github/FreeRTOS-Kernel-Book-main/` |
| 로컬 대조 결과 | 루트 파일 26개의 Git blob SHA-1이 위 commit의 해당 파일과 모두 일치. 여기에는 13개 장과 라이선스·목차가 포함된다 |

조회 근거: [고정 commit](https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/commit/ba20b2f820926587d5ee20ce312b3789d63f795c), [전체 트리 API](https://api.github.com/repos/FreeRTOS/FreeRTOS-Kernel-Book/git/trees/ba20b2f820926587d5ee20ce312b3789d63f795c?recursive=1), [릴리스](https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/releases), [submodule 정의](https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f820926587d5ee20ce312b3789d63f795c/.gitmodules).

26개 파일의 일치는 기존 수집본을 지침 작성의 원문으로 사용할 수 있다는 근거다. 이미지 전체, 예제 실행 결과, submodule 내부 내용까지 검증한 결과는 아니다. 이 조사 기록 작성 시점에는 새 clone과 본문 번역을 수행하지 않았다. 번역 착수 때 최신 상태를 다시 확인하고 기준 commit을 고정한다. PDF `V1.1.0`의 페이지 번호와 현재 `main`의 장·예제 번호가 같다고 가정하지 않는다.

## 3. 한국어 참고자료

분류 기준은 원문 대응 관계다. “발췌번역 확인”에는 번역 대상의 원문과 범위가 필요하다. 이번에 직접 확인한 게시물은 다음처럼 구분한다.

| 자료·작성자·게시일 | 확인한 범위와 원문 관계 | 활용 판단 |
| --- | --- | --- |
| [Task의 스케줄링](https://etst.tistory.com/466), 레드의 노트·sm_amoled, 2025-11-19 | Kernel Book p.119, p.93을 그림 출처로 명시. 상태·선점·시분할과 자체 실험을 설명 | 커널북을 인용한 한국어 해설로 확인. 현재 책 4.7·4.12절과 주제가 대응한다. 문장별 발췌번역으로는 확인하지 못했다 |
| [Task의 생성과 관리](https://etst.tistory.com/463), 같은 작성자, 2025-11-15 | task 구조, 생성·관리, 코드 설명 | 같은 시리즈의 관련 해설. 현재 책 4.2–4.5절과 주제가 대응한다. Kernel Book 직접 번역 여부는 미확인 |
| [자원 관리 (2) — Mutex](https://etst.tistory.com/469), 같은 작성자, 2025-11-22 | mutex, binary semaphore, 우선순위 상속, 구현 코드 설명 | 현재 책 8.3절의 보조 읽기 후보. 자체 코드 분석과 책의 번역을 구분한다 |
| [Task State — BLOCKED vs. SUSPENDED](https://jinolab.tistory.com/288), 지노랩, 2025-06-21 | 상태 비교와 API·시간 예시 | 한국어 설명 방식 비교용. 아래의 구체적 오류 때문에 기술 기준으로 채택하지 않는다 |
| [FreeRTOS 소개](https://pslab.tistory.com/entry/FreeRTOS-소개), 희황, 2013-06-20 | task·queue·semaphore·메모리 설명. 본문에 ubinos 위키 링크가 남아 있다 | 오래된 한국어 설명의 용어 사례. 원저자·번역 경로가 확정되지 않아 원본 번역 자료로 분류하지 않는다 |
| [FreeRTOS 공식 문서](https://yogyui.tistory.com/entry/FreeRTOS-공식-문서), 요겨, 2022-01-31 | 2016년 Kernel Book과 V10.0.0 Reference Manual 영문 PDF 소개 | 자료 안내문으로 확인. 한국어 번역본은 아니다 |
| [작업 간 조정](https://docs.aws.amazon.com/ko_kr/freertos/latest/userguide/inter-task-coordination.html), AWS | queue·semaphore·mutex·notification·buffer에 관한 공식 한국어 설명 | 실제 한국어 용례를 비교하되 영문과 대조한다. Kernel Book과는 별도 문서다 |

위 표의 장·절 연결은 이번 조사에서 주제를 비교한 결과이며, 게시자가 해당 절을 번역했다고 주장한 내용이 아니다. 레드의 노트 [FreeRTOS 분류](https://etst.tistory.com/category/Embedded%20System/FreeRTOS)에는 관련 글 8편이 표시되어 있었으며, 이 중 위의 3편을 직접 읽었다.

검색으로 발견했지만 주요 근거에서 제외한 자료도 있다.

- Scribd의 [FreeRTOS 활용](https://www.scribd.com/document/842306702/FreeRTOS-%ED%99%9C%EC%9A%A9)은 검색 추출문에 Kernel Book 출처가 반복된다. 저작자 원게시처와 재게시 권한을 확인하지 못해 `needs-human-check`로 남긴다.
- [guileschool FreeRTOS 목록](https://guileschool.com/authors/freertos/)은 검색 결과에 나타났으나 본문 열람에 실패했다. 내용을 확인한 참고자료로 계산하지 않는다.
- [임베디드 운영체제 FreeRTOS기초의 서지](https://k-knowledge.kr/srch/read.jsp?id=283460746)는 류상문·정성윤을 집필 저자로 표시한다. 이 정보만으로 Barry의 Kernel Book 번역서라고 볼 수 없다. 화면의 날짜를 발행일로 단정하지 않는다.
- Velog 태그 목록과 강의 판매 페이지는 원문 대응을 확인할 수 없어 발췌번역 근거에서 제외했다.

## 4. 번역 기준에 반영할 관찰

### 4.1 공식 한국어 문서의 용례도 대조가 필요하다

AWS 한국어 페이지는 task를 ‘작업’, queue를 ‘대기열’, mutual exclusion을 ‘상호 제외’로 표현한다. 본 프로젝트는 기존 지침에 따라 객체명 `task`, `queue`, `mutex`를 영어로 유지하고, 개념 설명에는 ‘상호 배제’를 사용한다. 이는 프로젝트 편집 기준이며 AWS 용어 표준이라는 뜻은 아니다.

같은 AWS 페이지의 메시지 버퍼 설명에는 한국어 ‘32바이트 아키텍처’와 영문 `32-byte architecture`가 함께 나타난다. 한국어 번역만의 오류로 단정할 수 없으며, 원문에도 있는 단위 표현의 정오 검토 항목으로 남긴다(`check-against-source`). 원문이 의심스러울 때는 번역문만 고치는 대신 원문 위치·근거·수정 여부를 따로 기록한다. [한국어 페이지](https://docs.aws.amazon.com/ko_kr/freertos/latest/userguide/inter-task-coordination.html), [영문 페이지](https://docs.aws.amazon.com/freertos/latest/userguide/inter-task-coordination.html).

### 4.2 설명의 간결함과 기술 정확도를 따로 검토한다

지노랩 상태 비교 글에는 ‘타임아웃=0’을 무기한 대기와 연결하는 문구가 있다. 공식 Kernel Book 5.3절은 queue API의 대기값 0을 즉시 반환 조건으로 설명하며, `portMAX_DELAY`의 무기한 대기에는 `INCLUDE_vTaskSuspend = 1` 조건을 붙인다. 이 차이는 짧은 설명에서 설정 조건을 생략하면 의미가 뒤집힐 수 있음을 보여준다. [게시물](https://jinolab.tistory.com/288), [공식 원문 5장](https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f820926587d5ee20ce312b3789d63f795c/ch05.md).

같은 글의 `vTaskResumeFromISR()` 표기는 현재 책 4.7.2절의 `xTaskResumeFromISR()`와 다르다. API 이름은 자연어 교정·유추의 대상에서 제외하고 기준 원문과 글자 단위로 대조한다. [공식 원문 4장](https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f820926587d5ee20ce312b3789d63f795c/ch04.md).

### 4.3 문체와 원저자 내용을 분리한다

개인 학습 글의 구어체·비유·자체 실험은 이해를 도울 수 있다. 책의 번역에서는 설명문 ‘한다’체를 사용하고, 원문 밖의 해설은 `[옮긴이 주]`로 분리한다. 타인의 설명문을 이어 붙이는 대신 고정한 영문 원문에서 독립적으로 번역한다. 조사표의 링크는 비교·출처 추적용이다.

## 5. 라이선스와 번역본 표시

공식 저장소의 [LICENSE-SUMMARY](https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f820926587d5ee20ce312b3789d63f795c/LICENSE-SUMMARY)는 문서를 **CC BY-SA 4.0**, 문서 속 sample code와 accompanying examples를 **modified MIT**로 구분한다. 코드의 구체 조건은 [LICENSE-SAMPLECODE](https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f820926587d5ee20ce312b3789d63f795c/LICENSE-SAMPLECODE)에 있다. submodule의 커널 코드는 해당 저장소의 라이선스를 별도로 유지한다.

한국어 번역본에는 원저자·원문 URL·기준 commit·원문 라이선스·번역 및 변경 사실을 표시하고, CC BY-SA의 동일조건변경허락 조건을 반영한다. 원문 저작권·면책 고지를 보존하고 ‘비공식 한국어 번역’이라고 표시한다. 원본의 개별 그림·인용에 별도 고지가 있으면 함께 보존한다. [CC BY-SA 4.0 한국어 설명](https://creativecommons.org/licenses/by-sa/4.0/deed.ko).

## 6. 검색 범위와 한계

대표 검색어는 `FreeRTOS 커널북 한글 번역`, `"Mastering the FreeRTOS" 한글`, `"FreeRTOS" "번역"`, `"FreeRTOS" "Mastering" "태스크"`, Tistory·Velog 범위 검색, `FreeRTOS Korean book translation 한글`이다. GitHub 저장소 검색은 `FreeRTOS-Kernel-Book Korean fork:true`, `FreeRTOS 번역 fork:true`, `FreeRTOS 한글 fork:true`를 사용했으며 연결 도구가 반환한 일치 저장소는 0개였다. 이는 접근 가능한 검색 결과의 범위이며 모든 포크의 본문 전수조사가 아니다.

FreeRTOS 공식 책 웹페이지는 새 경로로 이동했으나 브라우징 도구에서 읽을 본문이 추출되지 않았다. 이 부분은 GitHub의 실제 Markdown·트리·릴리스로 교차 확인했다. 로그인·유료 서비스 내부, 비공개 커뮤니티, 모든 국내 출판 목록은 조사하지 않았다.

## 7. 조사 이후의 작업 기준

조사 이후 사용자의 지시에 따라 공식 저장소를 직접 clone하고 본문 13장·부속 문서 5종과 한글 그림을 통합했다. 이 문서의 검색 결과와 미확인 사항은 조사 당시의 기록이다. 이후 작업과 공개 정본의 현재 상태는 [저장소 안내](../README.md), [검수 결과](REVIEW.md), [작업 절차](WORKFLOW.md)를 따른다.
