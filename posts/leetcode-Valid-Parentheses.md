# [LeetCode] Valid Parentheses (Python 풀이)

## 문제접근
https://leetcode.com/problems/valid-parentheses/

이 문제는 '(', ')', '{', '}', '[', ']'로만 이루어진 문자열이 주어졌을 때, 여는 괄호와 닫는 괄호가 올바른 종류와 순서로 짝지어져 있는지 판별하는 문제다.

여는 괄호는 같은 종류의 괄호로 닫혀야 하고, 닫히는 순서도 올바른 순서를 지켜야 하며, 모든 닫는 괄호는 그에 대응하는 여는 괄호가 있어야 유효한 문자열로 판단한다.

스택 자료구조를 활용하면 될 것 같다는 생각으로 접근함.

s를 순회하면서 괄호들을 배열에 담고, 닫힌 괄호가 나올 때는 배열의 마지막 원소를 확인해 쌍이 맞으면 배열에서 제거하는 방식을 사용함.

최종적으로 배열이 비어있으면 true, 비어있지 않으면 false를 반환하도록 함.


## 풀이

**1.** 결과를 담을 배열 answer를 스택처럼 사용하기 위해 빈 배열로 초기화한다.

**2.** 문자열 s를 순회하면서 각 문자 p를 확인한다.

**3.** p가 ")"이고 answer가 비어있지 않으며 마지막 원소가 "("일 경우, 짝이 맞는 것이므로 answer에서 마지막 원소를 pop한다.

**4.** 같은 방식으로 "]"와 "[", "}"와 "{"의 짝도 각각 확인해 맞으면 pop한다.

**5.** 위 조건에 해당하지 않는 경우(여는 괄호이거나, 짝이 맞지 않는 닫는 괄호인 경우)에는 p를 answer에 그대로 추가한다.

**6.** 순회가 끝난 뒤 answer가 비어있으면 모든 괄호가 짝을 이룬 것이므로 true를, 남아있는 원소가 있으면 false를 반환한다.


## 전체코드
```python
class Solution:
    def isValid(self, s: str) -> bool:
        answer = []  # 스택 역할을 하는 배열

        for p in s:
            # 닫는 괄호가 나오면 스택 top과 짝이 맞는지 확인 후 pop
            if p == ")" and len(answer) != 0 and answer[-1] == "(":
                answer.pop()
            elif p == "]" and len(answer) != 0 and answer[-1] == "[":
                answer.pop()
            elif p == "}" and len(answer) != 0 and answer[-1] == "{":
                answer.pop()
            else:
                # 여는 괄호이거나 짝이 맞지 않는 닫는 괄호는 스택에 push
                answer.append(p)

        # 스택이 비어있으면 모든 괄호가 짝을 이룬 것
        if len(answer) == 0:
            return True
        else:
            return False
```

\#스택 \#문자열
