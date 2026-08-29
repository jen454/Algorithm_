class Solution:
    def isValid(self, s: str) -> bool:
        answer = []

        for p in s:
            if p == ")" and len(answer) != 0 and answer[-1] == "(":
                answer.pop()
            elif p == "]" and len(answer) != 0 and answer[-1] == "[":
                answer.pop()
            elif p == "}" and len(answer) != 0 and answer[-1] == "{":
                answer.pop()
            else:
                answer.append(p)

        if len(answer) == 0:
            return True
        else:
            return False


# 스택 자료구조를 활용하면 될 것 같다.
# s를 순회하면서 괄호들을 배열에 담고, 닫힌 괄호일때는 배열의 마지막 원소를 확인해 쌍이 맞으면 배열에서 제거한다.
# 최종 배열이 비어있으면 true 아니면 false
