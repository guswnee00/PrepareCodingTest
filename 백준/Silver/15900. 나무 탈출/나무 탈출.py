import sys
sys.setrecursionlimit(1 << 30)

N = int(sys.stdin.readline().strip())

tree = [[] for i in range(N+1)]

for i in range(N-1):
    a, b = map(int, sys.stdin.readline().strip().split())
    tree[a].append(b)
    tree[b].append(a)
    
depth = [0] * (N + 1)

def dfs(cur, pre, cnt):
    depth[cur] = cnt
    for nxt in tree[cur]:
        if nxt == pre:
            continue
        dfs(nxt, cur, cnt + 1)

dfs(1, 0, 0)
d = 0
for i in range(2, N + 1):
    if len(tree[i]) == 1:
        d += depth[i]
        
if d % 2 == 1:
    print("Yes")
else:
    print("No")