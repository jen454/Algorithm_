def solution(s):
    answer = True
    cnt = 0
    for word in s:
        if word == '(':
            cnt += 1
        else:
            cnt -= 1
        
        if cnt < 0: return False
    if cnt: return False
    return True