def count(n):
    count = 0
    while (n != 1):
        if (n % 2 == 0):
            n /= 2
        else:
            n -= 1
            n /= 2
        count += 1
    return count

def solution(num_list):
    answer = 0
    for n in num_list:
        answer += count(n)
    return answer