def solution(phone_book):
    dict = {}
    
    for i in phone_book:
        dict[i] = 1
    
    for i in phone_book:
        temp = ''
        for j in i:
            temp += j
            if temp in dict and temp != i:
                return False
    return True