import sys
sys.setrecursionlimit(10 ** 6)

R, C = map(int, sys.stdin.readline().strip().split())
paper = []
for _ in range(R):
    paper.append(list(map(int, sys.stdin.readline().strip().split())))

visited = [[0] * C for _ in range(R)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def dfs(r, c):
    global paint
    visited[r][c] = 1
    if paper[r][c] == 1:
        paint += 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < R and 0 <= nc < C and paper[nr][nc] == 1 and visited[nr][nc] == 0:
            dfs(nr, nc)
        
totalpaint = 0
largepaint = 0
for i in range(R):
    for j in range(C):
        if paper[i][j] == 1 and visited[i][j] == 0:
            paint = 0
            dfs(i, j)
            largepaint = max(paint, largepaint)
            totalpaint += 1
            
print(totalpaint)
print(largepaint)
