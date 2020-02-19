# https://www.acmicpc.net/problem/1197


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
    def __init__(self, a, b, cost):
        self.a = a
        self.b = b
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost


def solution():
    answer = 0
    V, E = map(int, input().split())
    parents = [x for x in range(V + 1)]
    edges = []

    for _ in range(E):
        a, b, c = map(int, input().split())
        edges.append(Edge(a, b, c))

    edges.sort()
    for edge in edges:
        if not is_equal_parents(parents, edge.a, edge.b):
            answer += edge.cost
            union(parents, edge.a, edge.b)
    print(answer)


solution()
