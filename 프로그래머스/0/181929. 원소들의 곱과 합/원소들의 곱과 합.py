def solution(num_list):
    answer = 0
    xsum = 1
    for n in num_list:
        xsum *= n
    if (xsum < sum(num_list) * sum(num_list)):
        answer = 1
    return answer