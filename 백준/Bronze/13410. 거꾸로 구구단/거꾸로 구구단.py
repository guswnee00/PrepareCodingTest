N, K = map(int, input().split())
goo = []

for i in range(1, K+1):
    goo.append(int(str(i*N)[::-1]))

print(max(goo))