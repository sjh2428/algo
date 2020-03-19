# https://www.acmicpc.net/problem/4963

from collections import deque


def can_i_go(next_x, next_y, w, h):
    if next_x < 0 or next_y < 0 or next_y >= h or next_x >= w:
        return False
    return True


def bfs(y, x, m, w, h, directions, visited):
    q = deque()
    q.append([y, x])
    visited[y][x] = True
    while len(q) != 0:
        now = q.popleft()
        for direction in directions:
            next_y = now[0] + direction[0]
            next_x = now[1] + direction[1]
            if can_i_go(next_x, next_y, w, h) and not visited[next_y][next_x] and m[next_y][next_x] == 1:
                visited[next_y][next_x] = True
                q.append([next_y, next_x])


def solution():
    while True:
        ans = 0
        w, h = map(int, input().split())
        m = []
        visited = [[False for _ in range(w)] for __ in range(h)]
        directions = [[-1, 0], [-1, 1], [0, 1], [1, 1],
                      [1, 0], [1, -1], [0, -1], [-1, -1]]
        if w == 0 and h == 0:
            break
        for _ in range(h):
            rows = list(map(int, input().split()))
            m.append(rows)

        for y in range(h):
            for x in range(w):
                if not visited[y][x] and m[y][x] == 1:
                    bfs(y, x, m, w, h, directions, visited)
                    ans += 1

        print(ans)


solution()
