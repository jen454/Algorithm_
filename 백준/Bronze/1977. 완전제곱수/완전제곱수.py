import math

M = int(input())
N = int(input())
List = []

for i in range(M,N+1):
    if (i // math.sqrt(i) == math.sqrt(i)):
        List.append(i)

slist = sorted(List)

if len(List) == 0:
    print(-1)
else:
    print(sum(slist))
    print(slist[0])
