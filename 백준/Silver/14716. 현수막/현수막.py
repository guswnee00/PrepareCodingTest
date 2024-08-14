import sys
sys.setrecursionlimit(10**6) 

M, N = map(int, input().split())
pc = [list(map(int, input().split())) for i in range(M)]
    
dr = [1, 1, 1, 0, 0, -1, -1, -1]
dc = [-1, 0, 1, -1, 1, 1, 0, -1]

answer = 0
    
def dfs(r, c):
    for j in range(8):
        nr = r + dr[j]
        nc = c + dc[j]
        if 0 <= nr < M and 0 <= nc < N and pc[nr][nc] == 1:
            pc[nr][nc] = 0
            dfs(nr, nc)
    return True

for x in range(M):
    for y in range(N):
        if pc[x][y] == 1:
            pc[x][y] = 0
            dfs(x, y)
            answer += 1

print(answer)
    