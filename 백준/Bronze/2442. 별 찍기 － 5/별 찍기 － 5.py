N = int(input())
for i in range(N):
    print(" "*(N-1-i),end="")
    print("*"*(i*2+1))