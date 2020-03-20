# https://www.acmicpc.net/problem/2178

from collections import deque


def can_i_go(x, y, N, M, miro):
    return x >= 0 and y >= 0 and x < M and y < N and miro[y][x] == 1


def bfs(x, y, N, M, miro, visited):
    dq = deque()
    dq.append([x, y, 1])
    visited[y][x] = True
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    while len(dq):
        now = dq.popleft()
        for direction in directions:
            next_x = now[0] + direction[0]
            next_y = now[1] + direction[1]
            next_len = now[2] + 1
            if can_i_go(next_x, next_y, N, M, miro) and not visited[next_y][next_x]:
                if next_x == M - 1 and next_y == N - 1:
                    return next_len
                visited[next_y][next_x] = True
                dq.append([next_x, next_y, next_len])


def string_to_integer_array(string):
    return [int(char) for char in string if char != '\n']


def solution():
    N, M = map(int, input().split())
    visited = [[False for _ in range(M)] for __ in range(N)]
    miro = []
    for _ in range(N):
        row = input()
        miro.append(string_to_integer_array(row))
    print(bfs(0, 0, N, M, miro, visited))


solution()
