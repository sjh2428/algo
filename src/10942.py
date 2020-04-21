# https://www.acmicpc.net/problem/10942

import sys


def solution():
    sys_input = sys.stdin.readline
    N = int(sys_input())
    arr = list(map(int, sys_input().split()))
    M = int(sys_input())

    dp = [[False for _x in range(N)] for _y in range(N)]

    # 길이 1
    for i in range(N):
        dp[i][i] = True

    # 길이 2
    for i in range(N - 1):
        if arr[i] == arr[i + 1]:
            dp[i][i + 1] = True
            dp[i + 1][i] = True

    # 길이 3 이상
    for i in range(2, N):
        for j in range(N - i):
            if arr[j] == arr[j + i] and dp[j + 1][j + i - 1]:
                dp[j][j + i] = True
                dp[j + i][j] = True

    for _ in range(M):
        q = list(map(int, sys_input().split()))
        print(1 if dp[q[0] - 1][q[1] - 1] else 0)


solution()
