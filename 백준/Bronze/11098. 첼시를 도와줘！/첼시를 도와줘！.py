n = int(input())

for i in range(n):
    p = int(input())
    max_price = 0
    max_name = ""
    for j in range(p):
        c, name = input().split()
        if int(c) > max_price:
            max_price = int(c)
            max_name = name

    print(max_name)