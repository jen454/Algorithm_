def solution(names):
    answer = []
    for i in range(len(names)):
        if (i == 0 or i % 5 == 0):
            answer.append(names[i])
    return answer

# 0 1 2 3 4 5 6