def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i,j in zip(participant, completion): # 매칭 되는게 없으면 포함하지 않는다.
        if (i != j):
            return i
    return participant[-1]