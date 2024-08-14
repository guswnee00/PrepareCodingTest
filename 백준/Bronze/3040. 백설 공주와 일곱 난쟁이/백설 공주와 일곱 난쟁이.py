import random

l = []
for i in range(0, 9):
    l.append(int(input()))

s = 0
while s != 100:
    r = random.sample(l, 7)
    s = sum(r)

for a in r:
    print(a)