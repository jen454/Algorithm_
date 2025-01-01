def inc(dot1, dot2):
    mol = dot2[0] - dot1[0]
    den = dot2[1] - dot1[1]
    return mol / den

def solution(dots):
    answer = 0
    if (inc(dots[0],dots[1]) == inc(dots[2],dots[3])):
        answer = 1
    elif (inc(dots[0],dots[2]) == inc(dots[1],dots[3])):
        answer = 1
    elif (inc(dots[0],dots[3]) == inc(dots[1],dots[2])):
        answer =1
    return answer

# 평행 조건은 f(b)-f(a) / b-a 가 같은 경우
# 0,1 ? 2,3 // 0,2 ? 1,3 // 0,3 ? 1,2