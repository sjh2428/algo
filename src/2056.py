# https://www.acmicpc.net/problem/2056

from sys import stdin
from collections import deque


def solution():
    N = int(stdin.readline())
    costs = [-1 for _ in range(N)]
    tmp_costs = [-1 for _ in range(N)]
    requisites = [[] for _ in range(N)]
    indegree = [0 for _ in range(N)]
    dq = deque()

    for i in range(N):
        COST, REQUISITE_COUNT = 0, 1
        input_data = list(map(int, stdin.readline().split()))
        costs[i] = tmp_costs[i] = input_data[COST]
        if input_data[REQUISITE_COUNT] != 0:
            for j in input_data[2:]:
                requisites[j - 1].append(i)
                indegree[i] += 1

    for i in range(N):
        if indegree[i] == 0:
            dq.append(i)

    while dq:
        now = dq.popleft()
        for nxt in requisites[now]:
            if costs[nxt] < tmp_costs[nxt] + costs[now]:
                costs[nxt] = tmp_costs[nxt] + costs[now]

            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                dq.append(nxt)

    print(max(costs))


solution()
