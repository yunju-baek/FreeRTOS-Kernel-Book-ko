# FreeRTOS Kernel Book 영문 용어·한국어 풀이집

버전: v0.3 · 갱신일: 2026-11-01

용도: [번역 지침](STYLE_GUIDE.md)의 대표 표기 목록. 공식 한국어 표준 용어집은 아니다.

기준: [고정한 Kernel Book 원문](https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/tree/ba20b2f820926587d5ee20ce312b3789d63f795c)과 기존 프로젝트의 영어 객체명 보존 원칙.

‘영문 유지’는 본문에서 영문을 사용하고 각 장 첫 등장에 한국어 풀이를 붙인다는 뜻이다. ‘한국어’는 한국어를 대표 표기로 쓰고 첫 등장에 영어를 병기한다. 표의 풀이는 번역 선택을 돕기 위한 것이며 API 명세를 대체하지 않는다. 객체명의 한글 표기는 검색·풀이용으로만 사용한다.

## 핵심 용어

| 영어 | 본문 대표 표기 | 첫 등장 풀이·검토 사항 | 방식 |
| --- | --- | --- | --- |
| real-time operating system | RTOS | 실시간 운영체제 | 영문 유지 |
| kernel | 커널 | kernel | 한국어 |
| task | task | 태스크, FreeRTOS의 실행 단위. 일반 업무를 뜻하는 ‘작업’과 구분 | 영문 유지 |
| task function | task 함수 | task가 실행하는 함수 | 영문 유지 |
| task handle | task 핸들 | task를 참조하는 핸들 | 영문 유지 |
| Task Control Block | TCB | Task Control Block, task 제어 블록 | 영문 유지 |
| thread | 스레드 | thread. 원문이 task와의 관계를 설명하면 그 구분 유지 | 한국어 |
| scheduler | scheduler | 스케줄러 | 영문 유지 |
| scheduling | 스케줄링 | scheduling | 한국어 |
| preemption | 선점 | preemption | 한국어 |
| preemptive scheduling | 선점형 스케줄링 | preemptive scheduling | 한국어 |
| cooperative scheduling | 협력형 스케줄링 | cooperative scheduling. ‘협동형’과 혼용하지 않음 | 한국어 |
| time slicing | 시분할 | time slicing. 활성화·우선순위 조건 유지 | 한국어 |
| round robin | 라운드 로빈 | round robin | 한국어 |
| context switch | 문맥 전환 | context switch. ‘문맥 교환’과 혼용하지 않음 | 한국어 |
| yield | 실행권을 양보하다 | yield. 실제 API는 그대로 유지 | 한국어 |
| priority | 우선순위 | priority | 한국어 |
| Running | Running 상태 | 실행 중인 상태 | 영문 유지 |
| Not Running | Not Running 상태 | 실행 중이 아닌 상태. 하위 상태를 뭉개지 않음 | 영문 유지 |
| Ready | Ready 상태 | 실행 가능한 상태 | 영문 유지 |
| Blocked | Blocked 상태 | 이벤트 또는 시간이 충족되기를 기다리는 상태 | 영문 유지 |
| Suspended | Suspended 상태 | 명시적으로 실행을 중지한 상태. Blocked와 구분 | 영문 유지 |
| block / blocking | Blocked 상태에서 대기하다 / blocking | 단순 정지나 busy wait와 구분 | 문맥별 |
| unblock | Blocked 상태에서 벗어나다 | 실행 가능 전환과 실제 실행 시작을 구분 | 한국어 |
| busy wait | 바쁜 대기 | busy wait. CPU를 사용하며 조건 확인 | 한국어 |
| tick | tick | 커널 시간 기준의 틱 | 영문 유지 |
| tick interrupt | tick interrupt | tick 인터럽트 | 영문 유지 |
| tick count | tick count | 누적 tick 값 | 영문 유지 |
| tick rate | tick rate | 초당 tick 수 | 영문 유지 |
| delay | 지연 | delay. 시간 대기 동작 | 한국어 |
| block time | 최대 대기 시간 | block time. 해당 API의 단위 확인 | 한국어 |
| timeout | 시간 초과 | timeout. 값이면 ‘대기 제한 시간’ | 문맥별 |
| deadline | 마감 시한 | deadline | 한국어 |
| hard real-time | hard real-time | 경성 실시간 | 영문 유지 |
| soft real-time | soft real-time | 연성 실시간 | 영문 유지 |
| idle task | idle task | 유휴 task | 영문 유지 |
| hook function | hook 함수 | 특정 커널 동작에서 호출하는 함수 | 영문 유지 |
| callback function | callback 함수 | 콜백 함수 | 영문 유지 |
| stack | stack | 스택 | 영문 유지 |
| stack depth | stack 깊이 | stack depth. API별 단위 유지 | 영문 유지 |
| heap | heap | 힙 | 영문 유지 |
| static allocation | 정적 할당 | static allocation | 한국어 |
| dynamic allocation | 동적 할당 | dynamic allocation | 한국어 |
| fragmentation | 단편화 | fragmentation | 한국어 |
| stack overflow | stack overflow | 스택 범위 초과 | 영문 유지 |
| high-water mark | high-water mark | stack API에서는 최소 잔여 공간의 기록이라는 문맥 확인 | 영문 유지 |
| queue | queue | 큐. ‘대기열’로 일괄 치환하지 않음 | 영문 유지 |
| queue item | queue 항목 | queue item | 영문 유지 |
| queue set | queue set | 여러 queue·semaphore를 함께 기다리는 집합 | 영문 유지 |
| mailbox | mailbox | 메일박스 | 영문 유지 |
| enqueue / dequeue | queue에 넣다 / queue에서 꺼내다 | 실제 API의 앞·뒤 삽입 조건 유지 | 한국어 |
| peek | 제거하지 않고 읽다 | peek | 한국어 |
| pass by copy | 복사해서 전달하다 | pass by copy. 항목이 포인터인 경우를 구분 | 한국어 |
| pointer | 포인터 | pointer | 한국어 |
| interrupt | 인터럽트 | interrupt. ISR과 구분 | 한국어 |
| interrupt service routine | ISR | interrupt service routine, 인터럽트 서비스 루틴 | 영문 유지 |
| interrupt nesting | 인터럽트 중첩 | interrupt nesting | 한국어 |
| deferred interrupt processing | 인터럽트 처리의 지연 수행 | deferred interrupt processing. 후속 처리를 맡기는 문맥 유지 | 한국어 |
| critical section | critical section | 임계 구역. ‘임계 영역’과 혼용하지 않음 | 영문 유지 |
| suspend the scheduler | scheduler를 일시 중지하다 | task 하나의 Suspended 전환과 구분 | 영문 유지 |
| mutual exclusion | 상호 배제 | mutual exclusion. ‘상호 제외’와 혼용하지 않음 | 한국어 |
| synchronization | 동기화 | synchronization | 한국어 |
| semaphore | semaphore | 세마포어 | 영문 유지 |
| binary semaphore | binary semaphore | 이진 세마포어 | 영문 유지 |
| counting semaphore | counting semaphore | 계수 세마포어 | 영문 유지 |
| mutex | mutex | 뮤텍스 | 영문 유지 |
| recursive mutex | recursive mutex | 재귀 뮤텍스 | 영문 유지 |
| take / give (mutex) | 획득하다 / 반납하다 | 소유·반납 관계 유지 | 문맥별 |
| take / give (semaphore) | 획득하다 / 신호를 보내다 또는 반환하다 | 신호 동기화와 자원 계수 문맥 구분 | 문맥별 |
| priority inversion | 우선순위 역전 | priority inversion. ‘반전’과 혼용하지 않음 | 한국어 |
| priority inheritance | 우선순위 상속 | priority inheritance | 한국어 |
| deadlock | 교착 상태 | deadlock | 한국어 |
| starvation | 기아 상태 | starvation | 한국어 |
| race condition | 경쟁 상태 | race condition | 한국어 |
| reentrant | 재진입 가능한 | reentrant | 한국어 |
| thread-safe | 스레드 안전한 | thread-safe. 재진입 가능성과 별도로 검토 | 한국어 |
| gatekeeper task | gatekeeper task | 공유 자원 접근을 전담하는 task | 영문 유지 |
| timer command queue | timer command queue | 타이머 명령 큐 | 영문 유지 |
| software timer | software timer | 소프트웨어 타이머 | 영문 유지 |
| timer service task / daemon task | timer service task / daemon task | 타이머 서비스 task. 원문에서 두 이름의 관계를 설명 | 영문 유지 |
| one-shot timer | one-shot timer | 단발 타이머 | 영문 유지 |
| auto-reload timer | auto-reload timer | 자동 재장전 타이머 | 영문 유지 |
| event group | event group | 이벤트 그룹 | 영문 유지 |
| event bit | event bit | 이벤트 비트 | 영문 유지 |
| wait for any / wait for all | 하나 이상을 기다리다 / 모두를 기다리다 | 지정한 비트의 OR·AND 조건 유지 | 한국어 |
| barrier synchronization | 장벽 동기화 | barrier synchronization | 한국어 |
| task notification | task notification | task 알림 | 영문 유지 |
| notification value / state | notification 값 / 상태 | 값과 알림의 대기·수신 상태를 구분 | 영문 유지 |
| stream buffer | stream buffer | 스트림 버퍼. 관련 공식 문서와 연결할 때 사용 | 영문 유지 |
| message buffer | message buffer | 메시지 버퍼. 관련 공식 문서와 연결할 때 사용 | 영문 유지 |
| trigger level | trigger level | 수신 대기를 해제하는 기준량 | 영문 유지 |
| tickless idle | tickless idle | 유휴 중 주기적 tick을 억제하는 동작 | 영문 유지 |
| port | port | 특정 아키텍처·도구에 맞춘 이식 구현. I/O port와 구분 | 영문 유지 |
| run-time statistics | 실행 시간 통계 | run-time statistics | 한국어 |
| troubleshooting | 문제 해결 | troubleshooting | 한국어 |

## 보호할 문자열과 충돌 처리

`FreeRTOS`, `xTaskCreate()`, `vTaskDelay()`, `vTaskDelayUntil()`, `xTaskDelayUntil()`, `xTaskResumeFromISR()`, `xQueueReceive()`, `xSemaphoreTake()`, `portMAX_DELAY`, `pdMS_TO_TICKS()`, `pdPASS`, `pdFAIL`, `pdTRUE`, `pdFALSE`, `NULL`, `BaseType_t`, `TickType_t`, `StackType_t`, `TaskHandle_t`, `FreeRTOSConfig.h`, `heap_1.c`–`heap_5.c`와 그 밖의 원문 식별자를 보호한다. 이 목록은 예시이며 완전한 API 목록이 아니다.

`vTaskDelayUntil()`과 `xTaskDelayUntil()`처럼 서로 다른 이름은 해당 원문에 나온 형태를 그대로 사용한다. 최신 API를 안다는 이유로 자동 치환하지 않는다. 원문 오류가 의심되면 파일·절·문장·근거를 기록한다.

`task/태스크/작업`, `queue/큐/대기열`, `priority inversion/역전/반전`, `critical section/임계 구역/임계 영역`처럼 여러 표현이 발견되면 대표 표기 열을 따른다. 다른 자료를 인용하는 부분에서는 그 자료의 실제 표현을 보존한다.

새 용어는 원문 위치, 후보 표현, 선택 이유, 혼동할 개념을 기록해 추가한다. 뜻이 다른 두 용어를 하나로 합치지 않는다. 이미 번역한 장에 영향을 주는 변경은 용어집 버전을 올리고 적용 범위를 확인한다.

## 원문 대조 위치

- [1장 1.1.3](https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f820926587d5ee20ce312b3789d63f795c/ch01.md): task·thread 등 책의 용어 설명.
- [2장](https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f820926587d5ee20ce312b3789d63f795c/ch02.md), [3장](https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f820926587d5ee20ce312b3789d63f795c/ch03.md): port·식별자 규칙은 2장, 메모리 할당은 3장.
- [4장 4.7·4.12](https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f820926587d5ee20ce312b3789d63f795c/ch04.md): 상태·스케줄링.
- [5장 5.2·5.3·5.5](https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f820926587d5ee20ce312b3789d63f795c/ch05.md): queue의 저장·복사·대기.
- [6장](https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f820926587d5ee20ce312b3789d63f795c/ch06.md), [7장](https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f820926587d5ee20ce312b3789d63f795c/ch07.md), [8장](https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f820926587d5ee20ce312b3789d63f795c/ch08.md): timer·interrupt·자원 관리.
- [9장](https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f820926587d5ee20ce312b3789d63f795c/ch09.md), [10장](https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f820926587d5ee20ce312b3789d63f795c/ch10.md): event group·task notification.
- [11장](https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f820926587d5ee20ce312b3789d63f795c/ch11.md), [12장](https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f820926587d5ee20ce312b3789d63f795c/ch12.md), [13장](https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f820926587d5ee20ce312b3789d63f795c/ch13.md): 저전력·진단·문제 해결.
- [AWS 영문 사용자 가이드](https://docs.aws.amazon.com/freertos/latest/userguide/inter-task-coordination.html): stream/message buffer의 보조 용례. 현재 책의 13장 구성을 임의로 바꾸거나 새 장을 추가하는 근거로 사용하지 않는다.
