import sys
sys.setrecursionlimit(10 ** 6)

n = int(sys.stdin.readline().strip())
p1, p2 = map(int, sys.stdin.readline().strip().split())
m = int(sys.stdin.readline().strip())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
found = False

for _ in range(m):
    x, y = map(int, sys.stdin.readline().strip().split())
    graph[x].append(y)
    graph[y].append(x)
    
def dfs(node, depth):
    global found
    visited[node] = 1
    if node == p2:
        print(depth)
        found = True
        return
    for n in graph[node]:
        if not visited[n]:
            dfs(n, depth + 1)
            
dfs(p1, 0)

if not found:
    print(-1)
    