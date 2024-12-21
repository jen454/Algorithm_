def solution(score):
    avg_arr = [sum(i)/2 for i in score] # 평균 배열
    s_avg = sorted(avg_arr, reverse=True) # 내림차순 정렬
    answer = [] # 등수 배열
    
    for i in avg_arr:
        answer.append(s_avg.index(i)+1) # index는 맨 앞에 위치한 요소의 인덱스 번호를 리턴
    
    return answer