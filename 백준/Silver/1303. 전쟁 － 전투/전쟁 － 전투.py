N, M = map(int, input().split())
war = []
for i in range(M):  
    war.append(list(input()))

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

white = 0
blue = 0

def dfs(r, c, cnt, color):
    war[r][c] = 'X'  
    for j in range(4):
        nr = r + dr[j]
        nc = c + dc[j]
        if 0 <= nr < M and 0 <= nc < N and war[nr][nc] == color:
            cnt = dfs(nr, nc, cnt + 1, color)
    return cnt

for k in range(M):  
    for l in range(N):  
        if war[k][l] == 'W':
            white += (dfs(k, l, 1, 'W')) ** 2
        elif war[k][l] == 'B':
            blue += (dfs(k, l, 1, 'B')) ** 2

print(white, blue)