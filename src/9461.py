# https://www.acmicpc.net/problem/9461


def solution():
    T = int(input())
    for _ in range(T):
        N = int(input())
        dp = []
        dp.append(1)
        dp.append(1)
        dp.append(1)
        dp.append(2)
        dp.append(2)
        if N >= 5:
            for i in range(5, N):
                dp.append(dp[i - 5] + dp[i - 1])

        print(dp[N - 1])


solution()
