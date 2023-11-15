def solution(s):
    answer = ''
    s = sorted(s)
    s.sort(reverse=True)
    s = ''.join(s)
    answer = s
    return answer