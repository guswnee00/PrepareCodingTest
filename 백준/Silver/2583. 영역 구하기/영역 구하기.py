import sys
sys.setrecursionlimit(10 ** 6)

M, N, K = map(int, sys.stdin.readline().strip().split())
paper = [[0] * N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            paper[j][i] = 1
            
visited = [[0] * N for _ in range(M)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def dfs(r, c):
    global area
    visited[r][c] = 1
    area += 1
        
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < M and 0 <= nc < N and paper[nr][nc] == 0 and visited[nr][nc] == 0:
            dfs(nr, nc)
areas = []         
for i in range(M):
    for j in range(N):
        if paper[i][j] == 0 and visited[i][j] == 0:
            area = 0
            dfs(i, j)
            areas.append(area)
            
print(len(areas))
print(*sorted(areas))