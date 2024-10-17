import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    N = int(sys.stdin.readline().strip())
    Nlist = list(map(int, sys.stdin.readline().split()))
    print(min(Nlist), max(Nlist))
