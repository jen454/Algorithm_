M,N = map(int,input().split())
def so(N):
    if N==1:
        return False
    else:
        for i in range(2,int(N**0.5)+1):
            if N%i == 0:
                return False
    return True
for i in range(M,N+1):
    if so(i)==True:
        print(i)