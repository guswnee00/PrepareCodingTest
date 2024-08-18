def solution(board, k):
    answer = 0
    R = len(board)
    C = len(board[0])
    for i in range(R):
        for j in range(C):
            if (i + j) <= k:
                answer += board[i][j]
    return answer
                
        