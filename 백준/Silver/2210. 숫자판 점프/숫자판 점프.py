import sys
sys.setrecursionlimit(10 ** 6)

board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(5)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
nums = set()

def dfs(r, c, num):
    if len(num) == 6:
        nums.add(num)
        return
    
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < 5 and 0 <= nc < 5:
            dfs(nr, nc, num + str(board[nr][nc]))
            
for i in range(5):
    for j in range(5):
        dfs(i, j, str(board[i][j]))
        
print(len(nums))