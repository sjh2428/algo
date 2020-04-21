# https://www.acmicpc.net/problem/2293

import sys


def solution():
    sys_input = sys.stdin.readline
    n, k = map(int, sys_input().split())
    coins = []
    for _ in range(n):
        coins.append(int(sys_input()))

    dp = [0 for _ in range(k + 1)]
    dp[0] = 1

    for i in range(n):
        for j in range(coins[i], k + 1):
            dp[j] += dp[j - coins[i]]

    print(dp[k])


solution()
