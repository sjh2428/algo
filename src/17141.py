# https://www.acmicpc.net/problem/17141

from collections import deque
from itertools import combinations
from copy import deepcopy


def can_i_go(x, y, N):
    return 0 <= x < N and 0 <= y < N


def spread_virus(put_pos_combinations, not_put_virus_pos, m, v, N):
    for pos in not_put_virus_pos: # 현재 바이러스를 놓지 않을 pos에는 0 표시
        m[pos[0]][pos[1]] = 0
    for pos in put_pos_combinations: # 바이러스를 놓을 pos에 0/visited 표시
        m[pos[0]][pos[1]] = 0
        v[pos[0]][pos[1]] = True

    dq = deque(put_pos_combinations)
    directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    while len(dq) != 0:
        now = dq.popleft()
        for direction in directions:
            next_y = now[0] + direction[0]
            next_x = now[1] + direction[1]
            if can_i_go(next_y, next_x, N) and not v[next_y][next_x] and m[next_y][next_x] != 1:
                v[next_y][next_x] = True
                m[next_y][next_x] = m[now[0]][now[1]] - 1
                dq.append([next_y, next_x])

    max_time = 0
    for sero in range(N):
        for garo in range(N):
            if [sero, garo] in put_pos_combinations or m[sero][garo] == 1:
                continue
            elif m[sero][garo] == 0:
                return -1
            else:
                if m[sero][garo] < max_time:
                    max_time = m[sero][garo]
    return abs(max_time)


def solution():
    N, M = map(int, input().split())
    m = []
    v = []
    can_place_virus_pos = []
    answer = []

    for _ in range(N):
        temp = list(map(int, input().split()))
        can_place_virus_pos += [[len(m), i] for i, v in enumerate(temp) if v == 2]
        m.append(temp)
        v.append([False for _ in range(len(temp))])

    can_place_virus_pos_combinations = list(combinations(can_place_virus_pos, M))
    not_put_virus_pos = [[pos for pos in can_place_virus_pos if pos not in combination]
                         for combination in can_place_virus_pos_combinations]

    for i, combination in enumerate(can_place_virus_pos_combinations):
        answer.append(spread_virus(combination, not_put_virus_pos[i], deepcopy(m), deepcopy(v), N))

    answer = [x for x in answer if x != -1]
    if len(answer) > 0:
        print(min(answer))
    else:
        print(-1)


solution()
