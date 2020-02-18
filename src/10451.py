# https://www.acmicpc.net/problem/10451

import sys


def dfs(i, v, permutation):
    if v[i]:
        return
    v[i] = True
    dfs(permutation[i], v, permutation)


def solution():
    sysInput = sys.stdin.readline
    T = int(sysInput())
    for _ in range(T):
        answer = 0
        N = int(sysInput())
        v = [False for _ in range(N + 1)]
        permutation = [-1] + list(map(int, sysInput().split()))
        for i in range(1, N + 1):
            if v[i]:
                continue
            dfs(i, v, permutation)
            answer += 1
        print(answer)


solution()
