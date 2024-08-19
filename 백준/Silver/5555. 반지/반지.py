import sys
target = sys.stdin.readline().strip()
N = int(sys.stdin.readline().strip())
rings = [sys.stdin.readline().strip() for i in range(N)]

cnt = 0
for ring in rings:
    if target in ring * 2:
        cnt += 1
        
print(cnt)