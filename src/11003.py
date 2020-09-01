# https://www.acmicpc.net/problem/11003

from sys import stdin
from collections import deque


def solution():
    N, L = map(int, stdin.readline().split())
    A = list(map(int, stdin.readline().split()))
    D = [0 for _ in range(N)]
    dq = deque()

    IDX, VAL = 0, 1
    for i in range(N):
        while dq and dq[-1][VAL] > A[i]:
            dq.pop()
        while dq and i - dq[0][IDX] >= L:
            dq.popleft()
        dq.append((i, A[i]))
        D[i] = dq[0][VAL]
    print(*D)


solution()
