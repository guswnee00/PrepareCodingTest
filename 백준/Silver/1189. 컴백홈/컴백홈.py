R, C, K = map(int, input().split())
road = []
for i in range(R):
    road.append(list(input().rstrip()))
    
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

answer = 0

def dfs(r, c, distance):
    global answer
    if distance == K and r == 0 and c == C-1:
        answer += 1
    else:
        road[r][c] = 'T'
        for j in range(4):
            nr = r + dr[j]
            nc = c + dc[j]
            if 0 <= nr < R and 0 <= nc < C and road[nr][nc] == '.':
                road[nr][nc] = 'T'
                dfs(nr, nc, distance+1)
                road[nr][nc] = '.'

dfs(R-1, 0, 1)
print(answer)
