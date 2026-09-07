# [프로그래머스] 더 맵게 (Python 풀이)

## 문제접근
https://school.programmers.co.kr/learn/courses/30/lessons/42626

모든 음식의 스코빌 지수를 K 이상으로 만들어야 하는 문제로, 가장 맵지 않은 두 음식을 계속 섞어서 새로운 음식을 만들어 나가야 한다.

섞는 공식은 `가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)`이고, 이 과정을 모든 음식이 K 이상이 될 때까지 반복해야 한다.

문제 구분이 힙(Heap)으로 되어 있어서, 우선순위 큐를 사용하기로 하고 heapq를 사용하기로 했다.

가장 작은 원소와 두 번째로 작은 원소를 매번 뽑아야 하므로, 가장 작은 원소가 인덱스 0에 오는 최소힙 구조가 이 문제에 그대로 들어맞는다고 판단했다.

반복 조건은 스코빌 배열의 첫 번째 값, 즉 가장 작은 값이 K보다 작은 동안으로 잡았다.

모든 음식을 K 이상으로 만들 수 없는 경우도 고려해야 하는데, 섞는 과정에서 원소가 하나씩 줄어들기 때문에 원소가 하나만 남았는데도 K보다 작다면 더 이상 섞을 수 없는 상황이므로 -1을 반환하도록 처리했다.


## 풀이

**1.** scoville 리스트를 heapq.heapify로 최소힙으로 만든다.

**2.** 힙의 최솟값(scoville[0])이 K보다 작은 동안 반복한다.

**3.** 반복 중 남은 원소가 1개뿐이면 더 이상 섞을 수 없는 상황이므로 -1을 반환한다.

**4.** 힙에서 가장 작은 값 first와 두 번째로 작은 값 second를 각각 pop한다.

**5.** `first + second * 2` 공식으로 새로운 스코빌 지수를 계산해 다시 힙에 push한다.

**6.** 섞을 때마다 answer를 1씩 증가시킨다.

**7.** 반복이 끝나면(모든 음식이 K 이상이 되면) answer를 반환한다.


## 전체코드
```python
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)  # 최소힙 구성: 가장 작은 값이 인덱스 0에 오도록

    while (scoville[0] < K):  # 가장 작은 스코빌 지수가 K 이상이 될 때까지 반복
        if (len(scoville) == 1):
            return -1  # 원소가 하나 남았는데도 K 미만이면 더 섞을 수 없음

        first = heapq.heappop(scoville)   # 가장 맵지 않은 음식
        second = heapq.heappop(scoville)  # 두 번째로 맵지 않은 음식
        newscov = first + second * 2      # 섞은 음식의 스코빌 지수 계산
        heapq.heappush(scoville, newscov)
        answer += 1

    return answer
```

\#힙 \#우선순위큐
