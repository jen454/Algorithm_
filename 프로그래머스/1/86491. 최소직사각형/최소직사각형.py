def solution(sizes):
    answer = 0
    list_w = []
    list_h = []
    for i in sizes:
        list_w.append(max(i[0],i[1]))
        list_h.append(min(i[0],i[1]))
    answer = max(list_w) * max(list_h)
    return answer

# 60 50  60 50 
# 30 70  70 30
# 60 30  60 30
# 80 40  80 40

# 10 7   7 10
# 12 3   3 12
# 8 15   8 15
# 14 7   7 14
# 5 15   5 15

# 14 4   14 4
# 19 6   19 6
# 6 16   16 6
# 18 7   18 7
# 7 11   11 7