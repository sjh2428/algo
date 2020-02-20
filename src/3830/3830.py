# https://www.acmicpc.net/problem/3830

import sys
sys.setrecursionlimit(10**5)
sysInput = sys.stdin.readline


def find(parents, x, diff):
    if parents[x] == x:
        return x
    p = find(parents, parents[x], diff)
    diff[x] += diff[parents[x]]
    parents[x] = p
    return p


def is_equal_parent(parents, diff, a, b):
    return find(parents, a, diff) == find(parents, b, diff)


def union(parents, diff, a, b, w):
    parent_a = find(parents, a, diff)
    parent_b = find(parents, b, diff)
    if parent_a == parent_b:
        return
    parents[parent_b] = parent_a
    diff[parent_b] = diff[a] + w - diff[b]


def solution():
    while True:
        N, M = map(int, sysInput().split())
        if N == 0 and M == 0:
            break

        parents = [x for x in range(N + 1)]
        diff = [0 for _ in range(N + 1)]
        for _ in range(M):
            OP, A, B, W = 0, 1, 2, 3
            order = list(sysInput().split())
            if order[OP] == "!":
                union(parents, diff, int(order[A]), int(
                    order[B]), int(order[W]))
            else:
                if is_equal_parent(parents, diff, int(order[A]), int(order[B])):
                    print(diff[int(order[B])] - diff[int(order[A])])
                else:
                    print("UNKNOWN")


solution()
