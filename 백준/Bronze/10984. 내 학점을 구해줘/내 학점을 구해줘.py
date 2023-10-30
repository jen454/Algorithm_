T = int(input())
for i in range(T):
    N = int(input())
    total = 0
    sum = 0
    for j in range(N):
        c,g = input().split()
        C = int(c)
        G = float(g)
        total += C
        sum += C*G
    print(total,end=" ")
    print(round(sum/total,1))
