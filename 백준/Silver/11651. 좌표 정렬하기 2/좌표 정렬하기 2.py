import sys
input = sys.stdin.readline
N = int(input())
xy = []
for i in range(N):
    xy.append(list(map(int,input().split())))
xy.sort(key = lambda x : (x[1],x[0]))
for i in xy:
    print(i[0], i[1])