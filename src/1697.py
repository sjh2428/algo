# https://www.acmicpc.net/problem/1697

from collections import deque


def bfs(N, K, MAX_VALUE, visited, distance):
    dq = deque()
    dq.append(N)
    visited[N] = True
    while len(dq) != 0:
        now = dq.popleft()
        for nxt in [now - 1, now + 1, now * 2]:
            if 0 <= nxt and nxt <= MAX_VALUE and visited[nxt] == False:
                visited[nxt] = True
                distance[nxt] = distance[now] + 1
                dq.append(nxt)


def solution():
    MAX_VALUE = 200000
    N, K = map(int, input().split())
    visited = [False for _ in range(MAX_VALUE + 1)]
    distance = [0 for _ in range(MAX_VALUE + 1)]
    bfs(N, K, MAX_VALUE, visited, distance)
    print(distance[K])


solution()
