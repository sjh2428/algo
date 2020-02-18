# https://www.acmicpc.net/problem/1261

import sys
import heapq as hq

sysInput = sys.stdin.readline
INF = 1e9


class Edge:
    def __init__(self, y, x, wall):
        self.y = y
        self.x = x
        self.wall = wall

    def __lt__(self, otherEdge):
        return self.wall < otherEdge.wall


def dijkstra(N, M, d, miro):
    Y, X = 0, 1
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    h = []
    d[0][0] = 0
    hq.heappush(h, Edge(0, 0, 0))
    while len(h) != 0:
        now_y = h[0].y
        now_x = h[0].x
        now_wall = h[0].wall
        hq.heappop(h)
        if d[now_y][now_x] < now_wall:
            continue

        for direction in directions:
            next_y = now_y + direction[Y]
            next_x = now_x + direction[X]
            if can_i_go(next_y, next_x, N, M, miro):
                next_wall = miro[next_y][next_x] + now_wall
                if d[next_y][next_x] > next_wall:
                    d[next_y][next_x] = next_wall
                    hq.heappush(h, Edge(next_y, next_x, next_wall))


def can_i_go(y, x, N, M, miro):
    return y >= 0 and y < N and x >= 0 and x < M


def string_to_char_array(string):
    return [int(char) for char in string if char != '\n']


def solution():
    M, N = map(int, sysInput().split())
    miro = []
    d = [[INF for _ in range(M)] for _ in range(N)]
    for _ in range(N):
        line = sysInput()
        miro.append(string_to_char_array(line))
    dijkstra(N, M, d, miro)
    print(d[N - 1][M - 1])


solution()
