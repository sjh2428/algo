# https://www.acmicpc.net/problem/2225

def solution():
    N, K = map(int, input().split())
    dp = [[0 for _ in range(N + 1)] for __ in range(K + 1)]
    for i in range(N + 1):
        dp[1][i] = 1

    for i in range(1, K + 1):
        for j in range(N + 1):
            for l in range(j + 1):
                dp[i][j] += dp[i - 1][l]
                dp[i][j] %= 1000000000

    print(dp[K][N])


solution()
