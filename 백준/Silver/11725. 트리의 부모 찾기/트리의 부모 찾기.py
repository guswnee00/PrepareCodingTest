import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline().strip())

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [0]*(N+1)

def dfs(node):
    for n in graph[node]:
        if visited[n] == 0:
            visited[n] = node
            dfs(n)
            
dfs(1)
    
    
for i in range(2, N+1):
    print(visited[i])