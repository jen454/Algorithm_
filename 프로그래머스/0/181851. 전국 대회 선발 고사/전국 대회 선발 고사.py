def solution(rank, attendance):
    real_rank = []
    for i in range(len(rank)):
        if (attendance[i] == 1):
            real_rank.append(rank[i])
    real_rank.sort()
    return (10000 * rank.index(real_rank[0])) + (100 * rank.index(real_rank[1])) + rank.index(real_rank[2])