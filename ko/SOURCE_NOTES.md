# 원문 대조 사항과 번역 수정

기준일: 2026-11-01. 기준 원문은 [FreeRTOS/FreeRTOS-Kernel-Book의 ba20b2f](https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/tree/ba20b2f820926587d5ee20ce312b3789d63f795c)이다. 아래 항목은 Codex가 이 기준본에서 확인한 사항이며 공식 정오표가 아니다. 영어 본문과 코드 블록은 수정하지 않았다. 한국어 설명에서 바로잡은 내용은 본문에 `[옮긴이 주]`로 구분한다.

<a id="n01"></a>
## N01. Heap 통계 API와 자료형 이름

[3장 코드 3.9·3.10](../ch03.md#list3.9)의 캡션은 `vPortGetHeapStatus()`와 `HeapStatus_t()`라고 적혀 있지만, 바로 위 코드와 주변 설명은 `vPortGetHeapStats()`와 `HeapStats_t`를 사용한다. 한국어 캡션과 목차에는 코드의 이름을 사용했다.

<a id="n02"></a>
## N02. 정적 메모리 제공 함수의 이름

[3.4.2절](../ch03.md#342-static-internal-kernel-memory)의 설명에 `vApplicationGetTimeTaskMemory()`와 `vApplicationIdleTaskMemory()`가 나온다. 같은 절의 제목·코드 3.14·3.15에 따라 한국어 설명에는 `vApplicationGetTimerTaskMemory()`와 `vApplicationGetIdleTaskMemory()`를 사용했다.

<a id="n03"></a>
## N03. SMP idle task의 stack 크기 단위

[3.4.2.2절](../ch03.md#3422-vapplicationgetidletaskmemory)은 `configMINIMAL_STACK_SIZE`를 바이트로 설명한다. 같은 절의 코드 3.15는 `StackType_t uxIdleTaskStack[configMINIMAL_STACK_SIZE]`를 선언한다. 한국어 본문은 원문 단위를 보존하고 차이를 주석으로 표시했다. SMP 구현·버전별 대조가 남은 `check-against-source` 항목이다.

<a id="n04"></a>
## N04. 예제 4.2의 main 함수

[코드 4.9](../ch04.md#list4.9)의 원문 캡션은 “Example 2”라고 적혀 있다. 해당 절의 예제 번호에 맞춰 한국어판에는 “예제 4.2”로 표기했다.

<a id="n05"></a>
## N05. 아직 지정되지 않은 message buffer 장

[5.2.1절](../ch05.md#521-data-storage)의 각주 8은 message buffer 설명 위치를 “chapter TBD”로 남겨 두었다. 한국어판도 “TBD 장”을 유지하고 미완성 원문 참조임을 알렸다. 이 책에 없는 장 번호를 만들어 넣지 않았다.

<a id="n06"></a>
## N06. Timer callback의 코드 참조

[6.6.2절](../ch06.md#662-the-pvtimergettimerid-api-function)은 예제 6.2의 `prvTimerCallback()` 구현을 코드 6.9라고 가리킨다. 실제 구현은 코드 6.11이며, 코드 6.9는 `pvTimerGetTimerID()` 원형이다. 한국어판 참조는 6.11로 바로잡았다.

<a id="n07"></a>
## N07. Mutex 도표의 semaphore 표현

[그림 8.3](../ch08.md#fig8.3)의 5번 설명에는 semaphore라는 단어가 있으나 주변 설명은 mutex를 다룬다. 원문 도표와 한글화 도표 모두 해당 단어를 유지했다. 원저자 확인이 남은 `check-against-source` 항목이다.

<a id="n08"></a>
## N08. 그림 10.3의 예제 번호

[그림 10.3](../ch10.md#fig10.3)의 원문 캡션은 예제 7.1이라고 되어 있으나 해당 절의 task notification 예제 번호는 10.1이다. 원본 그림과 한국어 캡션은 원문 번호를 유지하고 주석으로 차이를 알렸다.

<a id="n09"></a>
## N09. Stack high-water mark 단위

[12.5.4절](../ch12.md#1254-the-uxtaskgetsystemstate-api-function)은 `usStackHighWaterMark`가 바이트 단위라고 설명한다. 그러나 이 책의 예제에 고정된 [커널 18ed888의 tasks.c](https://github.com/FreeRTOS/FreeRTOS-Kernel/blob/18ed8886fe3eed9dbe433a82cdc62ce5dc0315eb/tasks.c#L3926)는 `prvTaskCheckFreeStackSpace()`에서 여유 바이트 수를 `sizeof(StackType_t)`로 나누고, 그 값을 `usStackHighWaterMark`에 넣는다. 이 구현의 단위는 `StackType_t` 요소 수이다. 한국어판은 원문 문장을 보존하되 바로 아래에 구현과의 차이를 밝혔다.

책 본문의 API 설명과 동봉 예제 커널의 버전은 항상 일치한다고 가정하지 않는다. 예제 submodule은 V10.6.2이며, 책에는 SMP와 더 새로운 API에 대한 설명도 있다. 실제 적용 시 사용할 버전의 선언과 구현을 기준으로 단위를 확인한다.

<a id="n10"></a>
## N10. 절 번호 13.3.4 중복

[13장](../ch13.md)에서 stack 검사 방법 2와 방법 3의 절 번호가 모두 13.3.4이다. 번호를 보존하고 각각의 기존 anchor를 유지했다. 목차의 두 항목은 서로 다른 절로 연결된다.

<a id="n11"></a>
## N11. 최적화된 task 선택 설정 이름

[4.5.2절](../ch04.md#452-architecture-optimized-scheduler)의 `configUSE_PORT_optimized_TASK_SELECTION`은 동봉 커널의 실제 매크로와 다르다. [커널 FreeRTOS.h](https://github.com/FreeRTOS/FreeRTOS-Kernel/blob/18ed8886fe3eed9dbe433a82cdc62ce5dc0315eb/include/FreeRTOS.h#L940)에 따라 한국어 설명에는 `configUSE_PORT_OPTIMISED_TASK_SELECTION`을 사용했다.

<a id="n12"></a>
## N12. Heap 설명에서 task 생성 절 참조

[3.2.2절](../ch03.md#322-heap_2)은 `xTaskCreate()` 설명을 3.4절이라고 가리키지만 실제 task 생성 설명은 [4.4절](ch04.md#44-task-creation)이다. 한국어판에서 빠졌던 참조를 복원하면서 4.4절로 연결하고 원문의 차이를 밝혔다.

<a id="n13"></a>
## N13. TCP 연결 끊김의 코드 참조

[5.5절](../ch05.md#55-working-with-large-or-variable-sized-data)의 원문은 연결 끊김 의사 코드를 “Listing 59”로 가리키지만 실제 번호는 5.19이다. 한국어판에서는 5.19로 표기했다.

<a id="n14"></a>
## N14. Event group 동기화의 코드 참조

[9.4절](../ch09.md#94-task-synchronization-using-an-event-group)의 소켓 닫기 설명은 두 곳에서 코드 9.10을 가리키지만 실제 의사 코드는 9.11이다. 예제 9.2의 task 구현도 9.12가 아니라 9.13이다. 한국어판은 각각 실제 구현의 번호로 연결했다.

<a id="n15"></a>
## N15. 원문 Markdown 표시 오류

원문 예제 4.4·5.3 캡션에 남은 HTML 닫기 태그, 일부 여러 줄 캡션은 한국어판에서 정상적인 Markdown 캡션으로 정리했다. 원문의 번호와 의미, anchor는 유지했다. 원문 HTML anchor의 영문 `title` 속성은 출처 대조를 위해 보존했다.
