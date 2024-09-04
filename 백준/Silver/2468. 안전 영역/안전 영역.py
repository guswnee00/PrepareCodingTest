import sys
sys.setrecursionlimit(10 ** 6)

N = int(sys.stdin.readline())
ground = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def dfs(r, c, h):
    visited[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and ground[nr][nc] > h:
            dfs(nr, nc, h)
        
min_h = min(map(min, ground))
max_h = max(map(max, ground))       
max_safe = 0

for h in range(min_h - 1, max_h):
    visited = [[0] * N for _ in range(N)]
    safe = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and ground[i][j] > h:
                dfs(i, j, h)
                safe += 1
    if safe > max_safe:
        max_safe = safe
    
print(max_safe)
        
