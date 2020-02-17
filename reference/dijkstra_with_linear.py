INF = 1000000000
NODE_CNT = 6


# 가장 최소 거리를 가지는 정점을 반환(선형 탐색 - 결과적으로 n^2)
def getSmallIndex(visited, distance):
    minimum = INF
    idx = 0
    for i in range(NODE_CNT):
        if distance[i] < minimum and not visited[i]:
            minimum = distance[i]
            idx = i

    return idx


# 다익스트라를 수행하는 함수
def dijkstra(start, visited, distance, edges):
    for i in range(NODE_CNT):
        distance[i] = edges[start][i]

    visited[start] = True
    for i in range(NODE_CNT - 2):
        current = getSmallIndex(visited, distance)
        visited[current] = True
        for j in range(6):
            if not visited[j]:
                if distance[current] + edges[current][j] < distance[j]:
                    distance[j] = distance[current] + edges[current][j]


def solution():
    edges = [[0, 2, 5, 1, INF, INF],
             [2, 0, 3, 2, INF, INF],
             [5, 3, 0, 3, 1, 5],
             [1, 2, 3, 0, 1, INF],
             [INF, INF, 1, 1, 0, 2],
             [INF, INF, 5, INF, 2, 0]]
    visited = [False for _ in range(NODE_CNT)]
    distance = [INF for _ in range(NODE_CNT)]
    dijkstra(0, visited, distance, edges)

    for i in range(NODE_CNT):
        print(distance[i], "", end="")
    print()


solution()
