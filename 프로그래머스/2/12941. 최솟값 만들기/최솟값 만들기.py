def solution(A,B):
    answer = 0
    newA = sorted(A)
    newB = sorted(B, reverse=True)
    
    for i in range(len(A)):
        answer += newA[i] * newB[i]
    return answer

# 배열이 길이 만큼 반복, 중복 뽑기 x
# 최소가 될 수 있는 조합을 어떻게 찾을까?
# -> 작은 원소를 큰 원소랑 곱하는게 젤 작은 조합이 되지 않을까?
# -> A배열 오름차순 정렬, B배열 내림차순 정렬
# -> 배열 순회하면서 각 인덱스별 원소 곱셈 후 answer에 더하기
# 124 544 -> 1*5 2*4 4*4
# 12 43 -> 1*4 2*3