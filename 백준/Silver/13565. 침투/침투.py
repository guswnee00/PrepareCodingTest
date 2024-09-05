import sys
sys.setrecursionlimit(10**6)

M, N = map(int, sys.stdin.readline().strip().split())  # M: 행, N: 열
fiber = [list(map(int, sys.stdin.readline().strip())) for _ in range(M)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
visited = [[0] * N for _ in range(M)]

def dfs(r, c):
    visited[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < M and 0 <= nc < N and visited[nr][nc] == 0 and fiber[nr][nc] == 0:
            dfs(nr, nc)

for i in range(N):
    if visited[0][i] == 0 and fiber[0][i] == 0:
        dfs(0, i)

if 1 in visited[M-1]:
    print("YES")
else:
    print("NO")