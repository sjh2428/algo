# https://www.acmicpc.net/problem/2178

# BFS 주의점
# 방문 체크를 큐에 넣을 때 할 것
# for문 위에 방문 체크를 한다면 중복체크가 되므로

import sys
from queue import Queue


def can_i_go(y, x, N, M, miro):
    return y >= 0 and y < N and x >= 0 and x < M and miro[y][x] == 1


def bfs(N, M, miro, visited):
    Y, X, L = 0, 1, 2
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    q = Queue()
    q.put([0, 0, 1])

    while q.qsize() != 0:
        now = q.get()
        for direction in directions:
            next_y = now[Y] + direction[Y]
            next_x = now[X] + direction[X]
            next_length = now[L] + 1

            if can_i_go(next_y, next_x, N, M, miro) and not visited[next_y][next_x]:
                if next_y == N - 1 and next_x == M - 1:
                    return next_length
                visited[next_y][next_x] = True
                q.put([next_y, next_x, next_length])


def string_to_char_array(string):
    return [int(char) for char in string if char != '\n']


def solution():
    sysInput = sys.stdin.readline
    miro = []
    N, M = map(int, sysInput().split())
    visited = [[False for _ in range(M)] for _ in range(N)]
    for _ in range(N):
        line = sysInput()
        miro.append(string_to_char_array(line))
    print(bfs(N, M, miro, visited))


solution()
