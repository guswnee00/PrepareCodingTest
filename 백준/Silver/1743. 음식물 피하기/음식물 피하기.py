import sys
sys.setrecursionlimit(1 << 30)

N, M, K = map(int, sys.stdin.readline().strip().split())
foods = [[0] * M for _ in range(N)]
for _ in range(K):
    r, c = map(int, sys.stdin.readline().strip().split())
    foods[r-1][c-1] = 1

visited = [[0] * M for _ in range(N)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def dfs(r, c):
    global food
    visited[r][c] = 1
    if foods[r][c] == 1:
        food += 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M and foods[nr][nc] == 1 and visited[nr][nc] == 0:
            dfs(nr, nc)
            
largefood = 0
for i in range(N):
    for j in range(M):
        if foods[i][j] == 1 and visited[i][j] == 0:
            food = 0
            dfs(i, j)
            largefood = max(food, largefood)
        
            
print(largefood)
