N = int(input())
result = 0
def solution(n):
    re=[int(i) for i in str(n)]
    return sum(re)
for i in range(1,N+1):
    num = i + solution(i)
    if N == num:
        print(i)
        break
    if N == i:
        print(0)