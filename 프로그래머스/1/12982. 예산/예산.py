def solution(d, budget):
    answer = 0
    d.sort()
    
    for i in d:
        if (i <= budget):
            answer += 1
            budget -= i
    return answer

# 최대한 많이 줘야하니깐 d 배열을 오름차순 정렬하고 앞에서부터 예산에서 빼보면 될듯