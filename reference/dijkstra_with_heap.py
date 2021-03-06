import heapq
import sys
sysInput = sys.stdin.readline


INF = 1000000000


class Edge:
    def __init__(self, destination, distance):
        self.destination = destination
        self.distance = distance

    def __lt__(self, otherEdge):
        return self.distance < otherEdge.distance


def dijkstra(start, edges, d):
    d[start] = 0
    hq = []
    heapq.heappush(hq, Edge(start, 0))
    while len(hq) != 0:
        current = hq[0].destination
        distance = hq[0].distance
        heapq.heappop(hq)
        if d[current] < distance:
            continue

        for i in range(len(edges[current])):
            next_des = edges[current][i].destination
            next_dis = distance + edges[current][i].distance
            if (next_dis < d[next_des]):
                d[next_des] = next_dis
                heapq.heappush(hq, Edge(next_des, next_dis))


def solution():
    # V - 정점의 갯수, E - 간선의 갯수
    V, E = map(int, sysInput().split())
    # K - 시작 정점의 번호
    K = int(sysInput())

    edges = [[] for _ in range(V + 1)]
    distances = [INF for _ in range(V + 1)]

    for _ in range(E):
        # u에서 v로 가는 가중치 w인 간선
        u, v, w = map(int, sysInput().split())
        edges[u].append(Edge(v, w))

    dijkstra(K, edges, distances)
    for i in range(1, len(distances)):
        if distances[i] == INF:
            print("INF")
        else:
            print(distances[i])


solution()
