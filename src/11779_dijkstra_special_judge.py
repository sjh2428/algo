# https://www.acmicpc.net/problem/1916

import sys
import heapq as hq

sysInput = sys.stdin.readline
INF = 1e9


class Edge:
    def __init__(self, target, weight):
        self.target = target
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight


def dijkstra(start, d, edges, trace):
    h = []
    d[start] = 0
    hq.heappush(h, Edge(start, 0))
    while len(h) != 0:
        now = h[0].target
        now_weight = h[0].weight
        hq.heappop(h)
        if d[now] < now_weight:
            continue

        for edge in edges[now]:
            next_target = edge.target
            next_weight = edge.weight + now_weight
            if d[next_target] > next_weight:
                d[next_target] = next_weight
                trace[next_target] = now
                hq.heappush(h, Edge(next_target, next_weight))


def solution():
    N = int(sysInput())
    M = int(sysInput())
    edges = [[] for _ in range(N + 1)]
    d = [INF for _ in range(N + 1)]
    trace = [0 for _ in range(N + 1)]

    for _ in range(M):
        infos = list(map(int, sysInput().split()))
        FROM, TO, WEIGHT = 0, 1, 2
        edges[infos[FROM]].append(Edge(infos[TO], infos[WEIGHT]))

    start_city, end_city = map(int, sysInput().split())
    dijkstra(start_city, d, edges, trace)
    print(d[end_city])

    t = []
    t.append(end_city)
    prev = end_city
    while trace[prev] != 0:
        t.append(trace[prev])
        prev = trace[prev]
    print(len(t))
    for i in range(len(t) - 1, -1, -1):
        print(t[i], end=" ")
    print()


solution()
