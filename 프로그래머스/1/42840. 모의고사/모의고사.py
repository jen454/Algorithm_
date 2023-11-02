def solution(answers):
    answer = []
    
    list1 = [1,2,3,4,5]
    list2 = [2,1,2,3,2,4,2,5]
    list3 = [3,3,1,1,2,2,4,4,5,5]

    res = [0,0,0]

    for i in range(len(answers)):
        if (answers[i] == list1[i % 5]):
            res[0] += 1
        if (answers[i] == list2[i % 8]):
            res[1] += 1
        if (answers[i] == list3[i % 10]):
            res[2] += 1
        
    for i in range(len(res)):
        if (res[i] == max(res)):
            answer.append(i+1)
    return answer
