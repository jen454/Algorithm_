import math

# 소인수 분해 함수
def pf(n):
    arr = []
    x = 2
    while x <= n:
        if n % x == 0:
            if x not in arr:
                arr.append(x)
            n //= x
        else:
            x += 1
    return arr
    
def solution(a, b):
    answer = 0
    pf_arr = []
    # 최대공약수
    gcd = math.gcd(a,b)
    # 약분 분모
    den = b / gcd
    # 분모 소인수
    pf_arr = pf(den)
    if (pf_arr == [2] or pf_arr == [5] or pf_arr == [2,5] or den == 1):
        answer = 1
    else:
        answer = 2
    return answer