import sys

N = int(sys.stdin.readline())
cnt = 0
cows = [-1] * 11

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    if cows[a] == -1:
        cows[a] = b
    elif cows[a] != b:
        cows[a] = b
        cnt += 1
        
print(cnt)