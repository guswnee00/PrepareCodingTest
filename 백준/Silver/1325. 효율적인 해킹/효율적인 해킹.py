import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[b].append(a)

d = deque()
ans = []
maxlink =0
for i in range(1, N + 1):
    visit = [False] * (N + 1)
    visit[i] = True
    d.append(i)
    count = 0
    while len(d):
        s = d.popleft()

        for j in graph[s]:

            if visit[j] == False:
                visit[j] = True
                count +=1
                d.append(j)
    if maxlink < count:
        maxlink = count
        ans = [i]
    elif maxlink == count:
        ans.append(i)


print(" ".join(map(str,ans)))