def solution(num, total):
    n = 0
    for i in range(1, num):
        n += i
    start = (total-n) // num
    answer = [i for i in range(start, start + num)]
    return answer

# 첫번째 항을 start라고 할 때 n항까지의 합은
# start + (start+1) + (start+2) + ... + (start+num-1)이므로
# total = num * start + (1+2+...+num)이다.