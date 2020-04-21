# https://www.acmicpc.net/problem/1890
from collections import deque


def solution():
    answer = 0
    N = int(input())
    arr = []
    dp = []
    for _ in range(N):
        t = list(map(int, input().split()))
        arr.append(t)
        dp.append([0 for _x in range(N)])

    dp[0][0] = 1
    for i in range(N):
        for j in range(N):
            if dp[i][j] == 0 or arr[i][j] == 0:
                continue
            next_i, next_j = i + arr[i][j], j + arr[i][j]
            if next_i < N:
                dp[next_i][j] += dp[i][j]
            if next_j < N:
                dp[i][next_j] += dp[i][j]

    print(dp[N - 1][N - 1])


solution()
