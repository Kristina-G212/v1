start = 0

finish = 7

inf = 10 ** 5

a = [[(1, 2), (2, 6), (3, 7)],  # A - 0
     [(0, 2), (2, 3), (4, 7), (5, 15)],  # B - 1
     [(0, 6), (1, 3), (3, 4), (6, 3)],  # C - 2
     [(0, 7), (2, 4), (5, 9), (6, 4)],  # D - 3
     [(1, 7), (7, 7)],  # E - 4
     [(1, 15), (3, 9), (7, 9)],  # F - 5
     [(2, 3), (3, 4), (7, 6)],  # G - 6
     [(4, 7), (5, 9), (6, 6)]]  # H - 7

n = len(a)

v = [inf for i in range(n)]

v[start] = 0

color = [False for i in range(n)]


def visit(i):
    color[i] = True
    lst = a[i]
    for j in range(len(lst)):
        (p, w) = lst[j]
        if not color[p]:
            new_v = v[i] + w
            if new_v < v[p]:
                v[p] = new_v


while True:
    best = inf
    best_vertex = -1
    for j in range(n):
        if not color[j]:
            if v[j] < best:
                best = v[j]
                best_vertex = j

    if best_vertex == -1:
        break
    else:
        visit(best_vertex)

c = finish

path = [finish]

while c != start:
    l = a[c]
    for j in range(len(l)):
        (p, w) = l[j]
        if (v[c] - w) == v[p]:
            c = p
            path.append("->")
            path.append(p)
            break

path.reverse()

a1 = []

for A in a:
    a1.append(a.index(A))
print("Крачайший путь: ")

for t in zip(a1, v):
    print("к " + str(t[0]) + " вершине = " + str(t[1]))

print("Кратчайший путь до самой удаленной вершины: ")
for m in path:
    print(m, end="")
