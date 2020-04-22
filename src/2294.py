# https://www.acmicpc.net/problem/2294
import sys


def solution():
    sys_input = sys.stdin.readline
    MAX_VAL = 100001
    n, k = map(int, sys_input().split())
    coins = []
    dp = [MAX_VAL for _ in range(k + 1)]
    dp[0] = 0
    for _ in range(n):
        coins.append(int(sys_input()))

    for i in range(coins[0], k + 1, coins[0]):
        dp[i] = dp[i - coins[0]] + 1

    for i in range(1, n):
        for j in range(coins[i], k + 1):
            if dp[j - coins[i]] + 1 == 0:
                continue
            if dp[j] > dp[j - coins[i]] + 1:
                dp[j] = dp[j - coins[i]] + 1

    print(dp[k] if dp[k] != MAX_VAL else -1)


solution()
