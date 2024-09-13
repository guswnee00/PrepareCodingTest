import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [0] * (N+1)
component = 0

def dfs(node):
    visited[node] = 1
    for n in graph[node]:
        if visited[n] == 0:
            dfs(n)
            
for i in range(1, N+1):
    if visited[i] == 0:
        dfs(i)
        component += 1
        
print(component)