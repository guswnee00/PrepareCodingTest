import sys
sys.setrecursionlimit(10 ** 6)

N = int(sys.stdin.readline().strip())
house = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
visited = [[0] * N for _ in range(N)]

def dfs(r, c):
    global num_house
    visited[r][c] = 1
    num_house += 1
    
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and house[nr][nc] == 1:
            dfs(nr, nc)

houses = []

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 and house[i][j] == 1:
            num_house = 0
            dfs(i, j)
            houses.append(num_house)

houses.sort()
            
print(len(houses))
for h in houses:
    print(h)
    