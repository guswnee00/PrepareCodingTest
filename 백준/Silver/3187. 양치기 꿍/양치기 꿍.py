import sys
sys.setrecursionlimit(1 << 30)

R, C = map(int, sys.stdin.readline().split())
fence = []
for _ in range(R):
    fence.append(list(sys.stdin.readline().strip()))

visited = [[0] * C for _ in range(R)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]	

def dfs(r, c):
    global w, s
    visited[r][c] = 1
    if fence[r][c] == 'v':
        w += 1
    elif fence[r][c] == 'k':
        s += 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        
        if 0 <= nr < R and 0 <= nc < C and fence[nr][nc] != '#' and visited[nr][nc] == 0:
            dfs(nr, nc)
            
totalsheep = 0
totalwolf = 0

for i in range(R):
    for j in range(C):
        if fence[i][j] != '#' and visited[i][j] == 0:
            w = 0
            s = 0
            dfs(i, j)
            if w >= s:
                s = 0
            else:
                w = 0
            totalsheep += s
            totalwolf += w
            
print(totalsheep, totalwolf)