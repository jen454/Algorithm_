# 하나하나 조건문 X -> 교집합 사용하면 더 쉬움
def solution(lines):
    answer = 0
    sets = [set(range(min(l), max(l))) for l in lines]
    answer = len((sets[0] & sets[1]) | (sets[0] & sets[2]) | (sets[1] & sets[2]))
    return answer
