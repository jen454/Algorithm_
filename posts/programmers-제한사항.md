# [프로그래머스] 삼총사 (Python 풀이)

## 문제접근
https://school.programmers.co.kr/learn/courses/30/lessons/131705

학생들의 정수 번호가 담긴 배열 number가 주어지고, 그중 3명을 뽑아 더했을 때 0이 되는 조합의 개수를 구하는 문제이다.

number의 길이가 최대 13으로 작기 때문에 모든 조합을 다 확인해도 시간 안에 충분히 풀린다.

그래서 삼중 for문으로 가능한 모든 조합을 순회하면서 합이 0인 경우를 카운트하면 되지 않을까 생각했다.

첫 번째 for문은 전체 길이 - 2까지, 두 번째 for문은 첫 번째 +1부터 전체 길이 -1까지, 세 번째 for문은 두 번째 +1부터 전체 길이까지 돌리면 인덱스가 겹치지 않으면서 모든 조합을 한 번씩만 확인할 수 있다.

**-> 삼중 for문으로 모든 조합을 순회하며 합이 0인 경우를 카운트하는 방식으로 결정**

## 풀이

**1.** answer를 0으로 초기화한다.

**2.** 첫 번째 for문 i는 0부터 len(number)-2 이전까지 돈다.

**3.** 두 번째 for문 j는 i+1부터 len(number)-1 이전까지 돈다.

**4.** 세 번째 for문 k는 j+1부터 len(number)까지 돈다.

**5.** number[i], number[j], number[k]의 합이 0이면 answer를 1 증가시킨다.

**6.** 모든 조합을 확인한 뒤 answer를 반환한다.

## 전체코드
```python
def solution(number):
    answer = 0
    # 인덱스가 겹치지 않도록 i < j < k 순서로 모든 조합을 한 번씩 순회
    for i in range(len(number)-2):
        for j in range(i+1, len(number)-1):
            for k in range(j+1, len(number)):
                if (number[i]+number[j]+number[k] == 0):
                    answer += 1
    return answer
```

\#브루트포스 \#배열
