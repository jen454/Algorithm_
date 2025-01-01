def solution(babbling):
    answer = 0
    pb = ["aya", "ye", "woo", "ma"] # 가능한 발음
    for bab in babbling:
        count = 0
        for b in pb:
            if (bab.find(b) != -1):
                count += len(b)
        if (count == len(bab)):
            answer += 1
    return answer

# 가능한 발음이 한 번씩만 사용되어 있다는 점 활용
# 가능한 발음을 한 번 순회하여 조합에서 있다면 카운트 추가
# 최종 카운트가 단어 조합의 길이와 같다면 +1