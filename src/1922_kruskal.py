# https://www.acmicpc.net/problem/1922

import sys
sysInput = sys.stdin.readline


def find(parents, x):
    if parents[x] == x:
        return x
    parents[x] = find(parents, parents[x])
    p = parents[x]
    return p


def union(parents, a, b):
    a = find(parents, a)
    b = find(parents, b)
    if a > b:
        parents[a] = b
    else:
        parents[b] = a


def is_equal_parents(parents, a, b):
    a = find(parents, a)
    b = find(parents, b)
    return a == b


class Edge:
    def __init__(self, a, b, costs):
        self.a = a
        self.b = b
        self.costs = costs

    def __lt__(self, other):
        return self.costs < other.costs


def solution():
    answer = 0
    N = int(sysInput())
    M = int(sysInput())
    edges = []
    for _ in range(M):
        a, b, c = map(int, sysInput().split())
        edges.append(Edge(a, b, c))

    parents = [x for x in range(N + 1)]
    edges.sort()

    for edge in edges:
        if not is_equal_parents(parents, edge.a, edge.b):
            answer += edge.costs
            union(parents, edge.a, edge.b)

    print(answer)


solution()
