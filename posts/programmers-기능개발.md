# [프로그래머스] 기능개발 (Python 풀이)

## 문제접근
https://school.programmers.co.kr/learn/courses/30/lessons/42586

각 기능은 진도가 100%가 되어야 배포할 수 있고, 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발을 마쳐도 앞의 기능이 배포될 때 함께 배포된다는 것이 이 문제의 핵심 규칙이다.

즉 앞선 작업이 완료되기 전까지는 뒤에 있는 작업이 아무리 빨리 끝나도 대기해야 한다는 뜻이므로, 순서를 유지하면서 앞에서부터 차례로 처리하는 구조가 필요하다고 판단했다.

**1. 앞에 있는 걸 먼저 꺼내야 하는데, 어떤 자료구조를 써야 하지?**

앞에 있는 작업을 뒤에 있는 작업보다 먼저 꺼내서 처리해야 하므로 FIFO 구조가 필요하다고 생각했다.

**-> deque를 사용해서 큐로 처리하기로 했다.**

**2. 앞 원소가 배포 가능할 때, 뒤에서 같이 배포될 원소의 범위는 어떻게 잡지?**

[93, 30, 55] / [1, 30, 5] 예시로 각 작업이 완료되기까지 남은 일수를 계산해보면 7, 3, 9가 나오는데, 이때 (7, 3)이 먼저 묶이고 9가 따로 배포된다.

[95, 90, 99, 99, 80, 99] / 전부 속도 1인 예시에서는 남은 일수가 5, 10, 1, 1, 20, 1이 되고, 5는 단독으로, (10, 1, 1)이 한 번에, (20, 1)이 한 번에 배포된다.

두 예시를 정리해보니 앞 원소보다 큰 값이 나오기 전까지는 같은 배포 묶음으로 처리하면 된다는 규칙을 찾을 수 있었다.

**-> progress를 100에서 빼고 speed로 나눠 남은 일수를 계산한 뒤 큐에 저장하고, 맨 앞 원소를 기준으로 그보다 큰 값이 나오기 전까지 카운트해서 answer에 추가하는 방식으로 풀기로 했다.**

## 풀이

**1.** progresses와 speeds를 순회하며 각 작업이 완료되기까지 남은 일수를 `math.ceil((100 - progress) / speed)`로 계산해 deque에 저장한다.

**2.** deque에서 첫 번째 값을 꺼내 현재 배포 기준일(current)로 삼고, 카운트를 1로 초기화한다.

**3.** deque가 빌 때까지 다음 값을 하나씩 꺼내면서, 그 값이 current보다 작거나 같으면 같은 배포 묶음이므로 카운트만 늘린다.

**4.** 꺼낸 값이 current보다 크면 새로운 배포 묶음이 시작되는 것이므로, 지금까지의 카운트를 answer에 추가하고 current와 카운트를 새 값 기준으로 갱신한다.

**5.** 순회가 끝나면 마지막으로 누적된 카운트를 answer에 추가하고 반환한다.

## 전체코드
```python
from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    deq = deque()
    
    # progress를 100에서 뺀 뒤 speed로 나눠 완료까지 남은 일수를 계산해 큐에 저장
    for i in range(len(progresses)):
        value = math.ceil((100 - progresses[i]) / speeds[i])
        deq.append(value)
    
    current = deq.popleft()
    count = 1
    
    # 맨 앞 원소(current)보다 큰 값이 나오기 전까지 같은 배포 묶음으로 카운트
    while deq:
        next = deq.popleft()
        
        if next <= current:
            count += 1
        else:
            answer.append(count)
            current = next
            count = 1
            
    answer.append(count)
            
    return answer
```

\#큐 \#자료구조 \#시뮬레이션
