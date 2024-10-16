import sys

slist = [i for i in range(1, 31)]

for i in range(28):
    n = int(sys.stdin.readline())
    slist.remove(n)
    
slist.sort()
for i in slist:
    print(i)