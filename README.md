# FreeRTOS Kernel Book 한국어판

**비공식 한국어 번역 · Unofficial Korean translation**

Richard Barry와 The FreeRTOS Team의 *Mastering the FreeRTOS Real Time Kernel*을 한국어로 옮긴 저장소다. 공식 원본은 **[FreeRTOS/FreeRTOS-Kernel-Book](https://github.com/FreeRTOS/FreeRTOS-Kernel-Book)**이다. 이 프로젝트는 FreeRTOS 또는 AWS가 제공하거나 승인·검수한 공식 번역본이 아니다.

This is an **unofficial Korean translation** of the [FreeRTOS Kernel Book](https://github.com/FreeRTOS/FreeRTOS-Kernel-Book). It is not an official or endorsed FreeRTOS/AWS publication.

**[한국어 목차에서 읽기](ko/toc.md)** · [표제](ko/booktitle.md) · [약어](ko/abbreviations.md) · [영문 원본 목차](toc.md)

## 수록 내용과 검수 상태

본문 13장과 부속 문서 5종을 번역했다. 설명 도표 53개를 한글화했으며, 실행 로그·실제 도구 화면·로고 등 29개는 원본을 보존하고 한국어 캡션으로 연결했다. 본문에서 사용하는 그림 82개를 모두 연결했다.

Codex 검수에서 코드 문자열, 용어, 캡션, 목차 설명과 그림 링크를 수정했다. 전체 코드 블록 205개는 고정한 영문 원문과 동일하다. 검수 범위와 한계는 [검수 결과](ko/REVIEW.md), 원문의 오기·불일치는 [원문 대조 사항](ko/SOURCE_NOTES.md)을 참조한다. 사람의 최종 전수 교열과 예제 빌드·실보드 검증을 완료한 판본은 아니다.

| 장 | 한국어 본문 | 장 | 한국어 본문 |
| --- | --- | --- | --- |
| 1 | [머리말](ko/ch01.md) | 8 | [자원 관리](ko/ch08.md) |
| 2 | [커널 배포판](ko/ch02.md) | 9 | [이벤트 그룹](ko/ch09.md) |
| 3 | [힙 메모리 관리](ko/ch03.md) | 10 | [태스크 알림](ko/ch10.md) |
| 4 | [태스크 관리](ko/ch04.md) | 11 | [저전력 지원](ko/ch11.md) |
| 5 | [큐 관리](ko/ch05.md) | 12 | [개발자 지원](ko/ch12.md) |
| 6 | [소프트웨어 타이머 관리](ko/ch06.md) | 13 | [문제 해결](ko/ch13.md) |
| 7 | [인터럽트 관리](ko/ch07.md) | | |

## 정본 관리와 기여

한국어판의 정본은 **[yunju-baek/FreeRTOS-Kernel-Book-ko](https://github.com/yunju-baek/FreeRTOS-Kernel-Book-ko)의 `main`**이다. 이후 번역·그림·지침 수정은 이 저장소의 작업 branch와 Pull Request로 관리한다. 한국어판에 관한 제안은 이 저장소에 제출한다.

- [번역 지침](ko/STYLE_GUIDE.md), [용어집](ko/GLOSSARY.md), [작업 절차](ko/WORKFLOW.md)
- [기존 한국어 자료 조사](ko/RESEARCH.md), [그림 안내](ko/assets/README.md)
- [원문·번역 manifest](ko/translation-manifest.json), [그림 manifest](ko/assets/manifest.json)
- [작업자 안내](README.ko.md), [현재 상태](PROJECT_STATE.md)

번역 원문은 [`ba20b2f820926587d5ee20ce312b3789d63f795c`](https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/tree/ba20b2f820926587d5ee20ce312b3789d63f795c)로 고정했다. 루트의 영어 본문·그림·예제와 라이선스는 보존했다. 원래 저장소 소개는 [README.upstream.md](README.upstream.md)에 그대로 남겼다. `origin`은 한국어판, `upstream`은 공식 원본으로 구분한다.

```sh
git clone https://github.com/yunju-baek/FreeRTOS-Kernel-Book-ko.git
cd FreeRTOS-Kernel-Book-ko
git remote add upstream https://github.com/FreeRTOS/FreeRTOS-Kernel-Book.git
python3 tools/verify_translation.py
```

예제 소스도 사용할 때는 `git submodule update --init --recursive`를 실행한다. 문서 읽기에는 submodule 초기화가 필요하지 않다. 선택적인 로컬 HTML 검수본은 pandoc 설치 후 `python3 tools/render_review.py`로 만든다.

## 출처와 이용 조건

원저자: **Richard Barry and The FreeRTOS Team**. 원문의 저작권은 Amazon.com, Inc. 또는 그 계열사에 있다. 한국어판 관리: [yunju-baek](https://github.com/yunju-baek). 한국어 번역·교정과 설명 도표의 한글화는 원문에 대한 변경이며, 영어 원문과 구분해 `ko/`에 수록했다.

문서 및 한글화 그림은 원문과 동일한 **CC BY-SA 4.0**을 따른다. 문서 속 sample code와 accompanying examples는 원문의 **modified MIT** 조건을 유지한다. submodule 및 개별 자료의 별도 고지도 유지한다. 자세한 조건은 [LICENSE](LICENSE), [LICENSE-SUMMARY](LICENSE-SUMMARY), [LICENSE-SAMPLECODE](LICENSE-SAMPLECODE), [저작권 고지 번역](ko/copyright.md)을 참조한다. 상표와 로고의 권리는 각 권리자에게 있다.
