# [LeetCode] Valid Parentheses (Python 풀이)

## 문제접근
https://leetcode.com/problems/valid-parentheses/

이 문제는 '(', ')', '{', '}', '[', ']' 문자로만 이루어진 문자열이 주어졌을 때, 이 문자열이 유효한 괄호 문자열인지 판단하는 문제이다.

유효하다는 것은 여는 괄호가 같은 타입의 괄호로 닫혀야 하고, 여는 괄호가 올바른 순서로 닫혀야 하며, 모든 닫는 괄호는 대응하는 여는 괄호를 가지고 있어야 한다는 뜻이다.

가장 나중에 열린 괄호가 가장 먼저 닫혀야 한다는 조건을 보고 스택 자료구조를 활용하면 될 것 같다고 판단함.

문자열 s를 순회하면서 괄호들을 배열에 담고, 닫힌 괄호가 나왔을 때는 배열의 마지막 원소를 확인해서 쌍이 맞으면 배열에서 제거하는 방식으로 접근함.

이렇게 순회를 끝낸 후 최종 배열이 비어있으면 모든 괄호가 짝을 이뤄 제거된 것이므로 true, 비어있지 않으면 짝이 맞지 않는 괄호가 남아있는 것이므로 false를 반환하면 된다고 정리함.


## 풀이

**1.** 결과를 담을 배열 answer를 빈 리스트로 초기화한다.

**2.** 문자열 s를 한 글자씩 순회한다.

**3.** 현재 문자 p가 닫는 괄호(')', ']', '}')이고, answer가 비어있지 않으면서 answer의 마지막 원소가 그에 대응하는 여는 괄호일 경우 answer에서 마지막 원소를 pop한다.

**4.** 그 외의 경우, 즉 여는 괄호이거나 짝이 맞지 않는 닫는 괄호인 경우에는 p를 그대로 answer에 append한다.

**5.** 순회가 끝난 후 answer의 길이가 0이면 모든 괄호가 정상적으로 짝을 이뤄 제거된 것이므로 True를 반환한다.

**6.** answer에 원소가 남아있다면 짝이 맞지 않는 괄호가 존재하는 것이므로 False를 반환한다.


## 전체코드
```python
class Solution:
    def isValid(self, s: str) -> bool:
        answer = []

        for p in s:
            # 닫는 괄호가 나왔을 때 스택 top과 짝이 맞으면 pop
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


# 스택 자료구조를 활용하면 될 것 같다.
# s를 순회하면서 괄호들을 배열에 담고, 닫힌 괄호일때는 배열의 마지막 원소를 확인해 쌍이 맞으면 배열에서 제거한다.
# 최종 배열이 비어있으면 true 아니면 false

```

\#스택 \#문자열
