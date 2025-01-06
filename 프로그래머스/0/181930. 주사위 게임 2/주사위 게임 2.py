def solution(a, b, c):
    answer = 0
    if (a != b and a != c and b != c):
        answer = a + b + c
    elif (a == b == c):
        answer = (a + b + c) * (a*a + b*b + c*c) * (a*a*a + b*b*b + c*c*c)
    elif ((a == b and a !=c) or (a == c and a != b) or (b == c and a != b)):
        answer = (a + b + c) * (a*a + b*b + c*c)
    return answer