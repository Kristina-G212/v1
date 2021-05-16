a = [[1, 2, 3, 5],
     [0, 2, 3, 4],
     [0, 1, 5, 7],
     [0, 1, 4, 5],
     [1, 5, 6],
     [0, 2, 3, 4, 6, 7],
     [4, 5, 7],
     [2, 5, 6]]

n = len(a)

inf = 10 ** 5

source = 0
target = 7

capacity = {(0, 1): 95, (1, 0): 0,
            (0, 2): 32, (2, 0): 0,
            (0, 3): 75, (3, 0): 0,
            (0, 5): 57, (5, 0): 0,
            (1, 3): 18, (3, 1): 0,
            (1, 4): 6, (4, 1): 0,
            (2, 1): 5, (1, 2): 0,
            (2, 5): 23, (5, 2): 0,
            (2, 7): 16, (7, 2): 0,
            (3, 4): 9, (4, 3): 0,
            (3, 5): 24, (5, 3): 0,
            (4, 6): 7, (6, 4): 0,
            (4, 5): 11, (5, 4): 0,
            (5, 6): 20, (6, 5): 0,
            (5, 7): 94, (7, 5): 0,
            (6, 7): 81, (7, 6): 0
            }

flow = {}
for (u, v) in capacity:
    flow[u, v] = 0

color = [0 for i in range(n)]

timer = 1


def get_capacity(u, v):
    return capacity[u, v] - flow[u, v]


def dfs(v, min_capacity):
    if v == target:
        return min_capacity

    color[v] = timer

    lst = a[v]
    for to in lst:
        if color[to] == timer:
            continue

        c = get_capacity(v, to)
        if c == 0:
            continue

        c = min(c, min_capacity)

        delta = dfs(to, c)
        if delta > 0:
            flow[v, to] += delta
            flow[to, v] -= delta
            return delta
    return 0


while dfs(source, inf) > 0:
    timer += 1

res = 0
for v in a[source]:
    res += flow[source, v]

print("Максимальный поток " + str(res))
print(flow)
