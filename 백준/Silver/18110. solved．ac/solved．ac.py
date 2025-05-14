import sys
import math

N = int(input()) # 난이도 의견 개수
if (N == 0):
    print(0)
else:
    L = sorted([int(sys.stdin.readline()) for _ in range(N)]) # 제출한 난이도 배열(정렬)
    E = math.floor(N * 0.15 + 0.5) # 제외할 개수
    R = L[E:N-E] if N >= 3 else L # 특정 값들 제외한 난이도 배열
    res = math.floor(sum(R) / len(R) + 0.5) # 절사평균 값
    print(res)