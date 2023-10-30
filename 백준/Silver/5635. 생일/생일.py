n = int(input())
max_name = ""
min_name = ""
max_sum = -99999
min_sum = 99999
sum = 0
for i in range(n):
    name,dd,mm,yyyy = input().split()
    d = int(dd)
    m = (int(mm)-1)*31
    y = (int(yyyy)-1990)*365
    sum = y+m+d
    if max_sum < sum:
        max_sum = sum
        max_name = name
    elif min_sum > sum:
        min_sum = sum
        min_name = name
print(max_name)
print(min_name)
