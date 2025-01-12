def solution(my_string, indices):
    answer = ''
    for s in range(len(my_string)):
        if (s in indices):
            continue
        answer += my_string[s]
    return answer