import sys
sys.setrecursionlimit(10**6)

dr = [1, -1, 0, 0, 1, 1, -1, -1]
dc = [0, 0, 1, -1, 1, -1, 1, -1]

def dfs(r, c, h, w, grid, visited):
    visited[r][c] = 1
    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < h and 0 <= nc < w and visited[nr][nc] == 0 and grid[nr][nc] == 1:
            dfs(nr, nc, h, w, grid, visited)
            
while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]
    island = 0
    
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1 and visited[i][j] == 0:
                dfs(i, j, h, w, grid, visited)
                island += 1

    print(island)