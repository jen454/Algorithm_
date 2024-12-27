def solution(board):
    n = len(board)
    # 8방향 탐색
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    
    # 지뢰 설치
    boom = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                boom.append((i,j)) # 지뢰일때의 인덱스 append
                
    # 지뢰가 설치된 곳 주변에 폭탄 설치
    for x, y in boom:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                board[nx][ny] = 1

    # 폭탄이 설치되지 않은 곳만 카운팅
    answer = 0
    for x in range(n):
        for y in range(n):
            if board[x][y] == 0:
                answer += 1
    return answer