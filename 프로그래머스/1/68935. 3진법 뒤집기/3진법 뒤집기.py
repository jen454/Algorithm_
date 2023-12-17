def solution(n):
    answer = 0
    ans = ''.join(three(n))
    print(ans)
    answer = int(ans,3)
    return answer

def three(n):
    res = []
    while(True):
        if (n == 0): break
        res.append(str(n % 3))
        n //= 3
    return res