def solution(my_string, is_prefix):
    answer = 0
    arr = []
    for i in range(len(my_string)):
        arr.append(my_string[:i+1])
    if (is_prefix in arr):
        answer = 1
    return answer