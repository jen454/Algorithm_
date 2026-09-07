import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while (scoville[0] < K):
        if (len(scoville) == 1):
            return -1
        
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        newscov = first + second * 2
        heapq.heappush(scoville, newscov)
        answer += 1
    
    return answer

# 힙 카테고리 -> 우선순위 큐를 사용하자. heapq 사용하자.
# 지수 k 이상 될때까지 반복 -> 스코빌 첫번째 값이 K보다 작은 경우를 조건으로 while문 반복
# 최소힙 사용하자. 가장 작은 원소가 인덱스 0부터 오게, 작은 값을 뽑아내야 하기때문에
# 스코빌에서 제일 작은 값 두 개를 팝으로 뽑은 후 값 갱신 및 횟수 추가
# 모든 음식 스코빌 지수를 k 이상으로 만들 수 없는 경우는? -> 갱신마다 원소가 하나씩 줄어든다 -> 원소가 하나인데, K보다 작으면 -1