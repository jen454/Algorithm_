from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    deq = deque()
    
    for i in range(len(progresses)):
        value = math.ceil((100 - progresses[i]) / speeds[i])
        deq.append(value)
    
    current = deq.popleft()
    count = 1
    
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

# 앞에 있는 거를 뒤에 보다 먼저 꺼내야 함 -> fifo -> 큐 -> deque 사용하자.
# 앞에 원소가 배포 가능일때, 뒤에 배포 가능한 원소들 범위를 어떻게 잡지?
# 100-93=7 100-30=70, 100-55=45 / 7, 3, 9 -> (7,3) , 9
# 5 10 1 1 20 1 / 5, 10, 1, 1, 20, 1 -> 5 , (10,1,1) , (20,1)
# 규칙을 다음과 같이 정리해봤다.
# progress 각 원소를 100에서 뺸다.
# speeds로 나눈다.
# 계산된 원소를 큐에 저장한다.
# 큐를 순회하면서 맨 앞 원소부터 맨 앞 원소와 비교했을때 큰 원소 전까지 카운트 하고 answer 추가 및 popleft
