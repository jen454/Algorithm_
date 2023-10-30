N = int(input())
for i in range(N):
    print(" "*i,end="")
    print("*"*((N-1-i)*2+1))