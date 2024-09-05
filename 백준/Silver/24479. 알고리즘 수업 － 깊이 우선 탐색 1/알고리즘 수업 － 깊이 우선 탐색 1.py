import sys
sys.setrecursionlimit(10 ** 6)

N, M, R = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    graph[i].sort()

visited = [0] * (N + 1)

def dfs(node):
    global cnt
    visited[node] = cnt
    for n in graph[node]:
        if visited[n] == 0: 
            cnt += 1
            dfs(n)

cnt = 1
dfs(R)

for i in range(1, N + 1):
    print(visited[i])