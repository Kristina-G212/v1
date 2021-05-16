import itertools
res = 0
n = int(input())
a = []
for i in range(n):
    a.append(i)

per = itertools.permutations(a)

b = []

for j in per:
    res += 1
    b.append(j)

print(res)
for t in b:
    print(t)
