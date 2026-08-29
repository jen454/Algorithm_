# [프로그래머스] 삼총사 (Python 풀이)

## 문제접근

https://school.programmers.co.kr/learn/courses/30/lessons/131705

학생들의 정수 번호가 주어졌을 때, 그중 세 학생의 번호 합이 0이 되는 조합의 개수를 구하는 문제이다.

번호는 -1,000부터 1,000까지 있을 수 있고 중복된 값도 존재할 수 있으므로, 값 자체가 아니라 학생의 인덱스를 기준으로 조합을 세야 한다.

배열의 길이가 최대 13으로 작기 때문에 삼중 반복문으로 가능한 모든 조합을 다 돌면서 카운트를 세는 방식으로 접근했다.

첫번째 반복문은 전체 길이 - 2까지, 두번째 반복문은 첫번째 인덱스 + 1부터 전체 길이 - 1까지, 세번째 반복문은 두번째 인덱스 + 1부터 전체 길이까지 돌도록 구성해서 인덱스가 겹치지 않는 서로 다른 세 학생의 조합만 만들어지도록 했다.

각 조합에서 세 번호의 합이 0인지 확인하고, 0이면 카운트를 하나씩 늘려 최종 개수를 구한다.


## 풀이

**1.** answer를 0으로 초기화한다.

**2.** 첫번째 인덱스 i는 0부터 len(number)-2 전까지 순회한다.

**3.** 두번째 인덱스 j는 i+1부터 len(number)-1 전까지 순회한다.

**4.** 세번째 인덱스 k는 j+1부터 len(number)까지 순회한다.

**5.** number[i], number[j], number[k]의 합이 0이면 answer를 1 증가시킨다.

**6.** 삼중 반복문이 모두 끝나면 answer를 반환한다.


## 전체코드

```python
def solution(number):
    answer = 0
    # 인덱스 i < j < k 조합이 겹치지 않도록 삼중 반복문 범위를 설정
    # i: 0 ~ len-2, j: i+1 ~ len-1, k: j+1 ~ len
    for i in range(len(number)-2):
        for j in range(i+1, len(number)-1):
            for k in range(j+1, len(number)):
                if (number[i]+number[j]+number[k] == 0):
                    answer += 1
    return answer
```

\#브루트포스 \#배열 \#완전탐색
