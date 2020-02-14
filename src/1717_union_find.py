import sys
sysInput = sys.stdin.readline


def find(parents, x):
    if x == parents[x]:
        return x
    parents[x] = find(parents, parents[x])
    return parents[x]


def union(parents, x, y):
    x = find(parents, x)
    y = find(parents, y)
    if x > y:
        parents[x] = y
    else:
        parents[y] = x


def is_equal_parent(parents, x, y):
    x = find(parents, x)
    y = find(parents, y)
    if x == y:
        return True
    return False


def solution():
    N, M = map(int, sysInput().split())
    parents = [x for x in range(N + 1)]
    for _ in range(M):
        operator, a, b = map(int, sysInput().split())
        if operator == 1:
            if is_equal_parent(parents, a, b):
                print("YES")
            else:
                print("NO")
        elif operator == 0:
            union(parents, a, b)


solution()
