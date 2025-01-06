def solution(num_list):
    answer = 0
    odd = ''
    even = ''
    for n in num_list:
        if (n % 2 == 0):
            even += str(n)
        else:
            odd += str(n)
    answer = int(even) + int(odd)
    return answer