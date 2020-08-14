# https://www.acmicpc.net/problem/2011

def solution():
    s = input()
    mod = 1000000
    dp = [0 for _ in range(len(s) + 1)]
    dp[0] = dp[1] = 1

    if s[0] == '0':
        return 0

    for i in range(2, len(s) + 1):
        v = int(s[i - 1])
        if v != 0:
            dp[i] = dp[i - 1] % mod

        two_jarisu = int(s[i - 2]) * 10 + v

        if 10 <= two_jarisu <= 26:
            dp[i] = (dp[i] + dp[i - 2]) % mod

    return dp[-1]


print(solution())
