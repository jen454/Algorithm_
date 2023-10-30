while(1):
    result = True
    N=input()
    if int(N) != 0:
        for i in range(len(N)):
            if N[i] != N[len(N)-1-i]:
                result = False
                break
    else:
        break
    if result == True:
        print("yes")
    else:
        print("no")