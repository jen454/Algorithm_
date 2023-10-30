A = int(input())
if A % 5 == 0:
    print(A // 5)
else:
    count = 0
    while A > 0:
        A -= 3
        count += 1
        if A % 5 == 0:
            count += A // 5
            print(count)
            break
        elif A == 1 or A == 2:
            print(-1)
            break
        elif A == 0:
            print(count)
            break