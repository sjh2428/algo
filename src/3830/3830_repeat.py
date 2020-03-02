import sys

sys.setrecursionlimit(10**5)
sysInput = sys.stdin.readline


def find(parents, diff, x):
    if parents[x] == x:
        return x
    p = find(parents, diff, parents[x])
    diff[x] += diff[parents[x]]
    parents[x] = p
    return p


def union(parents, diff, x, y, w):
    parent_x = find(parents, diff, x)
    parent_y = find(parents, diff, y)
    if parent_x == parent_y:
        return

    diff[parent_y] = diff[x] + w - diff[y]
    parents[parent_y] = parent_x


def is_equal_parent(parents, diff, x, y):
    x = find(parents, diff, x)
    y = find(parents, diff, y)
    return x == y


def solution():
    while True:
        N, M = map(int, sysInput().split())
        if N == 0 and M == 0:
            break

        parents = [x for x in range(N + 1)]
        diff = [0 for _ in range(N + 1)]
        for _ in range(M):
            order = sysInput().split()
            TYPE, WEIGH, QUESTION = order[0], "!", "?"
            if TYPE == WEIGH:
                a, b, w = int(order[1]), int(order[2]), int(order[3])
                union(parents, diff, a, b, w)
            elif TYPE == QUESTION:
                a, b = int(order[1]), int(order[2])
                if is_equal_parent(parents, diff, a, b):
                    print(diff[b] - diff[a])
                else:
                    print("UNKNOWN")


solution()
