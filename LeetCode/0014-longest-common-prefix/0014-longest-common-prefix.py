class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = []
        strs.sort(key=len)
        shortest = strs[0]

        for i, char in enumerate(shortest):
            for s in strs[1:]:
                if s[i] != char:
                    return "".join(answer)
            answer.append(char)

        return "".join(answer)

# 배열안에서 가장 짧은 길이를 기준으로 비교하면서 보면 되지 않을까?
# 정렬을 해서 제일 짧은 길이 추출
# 제일 짧은 길이의 문자열을 기준으로 다른 문자 배열을 순회하면서 원소 중복을 체크한다.
# 앞에서부터 모두 같으면 answer에 추가 아니면 그전 배열 반환
