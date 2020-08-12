# https://www.acmicpc.net/problem/17142

from collections import deque
from itertools import combinations
from copy import deepcopy


def can_i_go(x, y, N):
    return 0 <= x < N and 0 <= y < N


def spread_virus(put_pos_combinations, m, N):
    v = [[False] * N for _ in range(N)]

    for pos in put_pos_combinations: # 바이러스를 놓을 pos에 0/visited 표시
        m[pos[0]][pos[1]] = 0
        v[pos[0]][pos[1]] = True

    max_val = 0
    v_cnt = len(put_pos_combinations)
    dq = deque(put_pos_combinations)
    directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    activated_viruses = {}
    while len(dq) != 0:
        now = dq.popleft()
        for direction in directions:
            next_y = now[0] + direction[0]
            next_x = now[1] + direction[1]
            if can_i_go(next_y, next_x, N) and not v[next_y][next_x] and m[next_y][next_x] != 1:
                v[next_y][next_x] = True
                v_cnt += 1
                if m[next_y][next_x] == 2:
                    activated_viruses[f'[{next_y}, {next_x}]'] = True
                    m[next_y][next_x] = m[now[0]][now[1]] - 1
                else: # 비활성화 바이러스가 아니라면
                    m[next_y][next_x] = m[now[0]][now[1]] - 1 # 거리를 갱신해주고
                    max_val = min(max_val, m[next_y][next_x]) # 최대값 갱신
                dq.append([next_y, next_x])

    if N*N - list(sum(m, [])).count(1) != v_cnt:
        return -1
    return abs(max_val)


def solution():
    N, M = map(int, input().split())
    m, can_place_virus_pos = [], []

    for _ in range(N):
        temp = list(map(int, input().split()))
        can_place_virus_pos += [[len(m), i] for i, v in enumerate(temp) if v == 2]
        m.append(temp)

    MAX_VAL = 10**6
    min_val = MAX_VAL
    for combination in combinations(can_place_virus_pos, M):
        result = spread_virus(combination, deepcopy(m), N)
        if result != -1 and result < min_val:
            min_val = result

    if min_val == MAX_VAL:
        print(-1)
    else:
        print(min_val)


solution()
