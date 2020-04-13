# https://www.acmicpc.net/problem/2156


def solution():
    n = int(input())
    amount = []
    dp = []
    for _ in range(n):
        a = int(input())
        amount.append(a)
    dp.append(amount[0])
    if n >= 2:
        dp.append(amount[0] + amount[1])
    if n >= 3:
        dp.append(max(dp[1], dp[0] + amount[2], amount[1] + amount[2]))
    if n >= 4:
        for i in range(3, n):
            dp.append(max(dp[i - 1],
                          dp[i - 2] + amount[i],
                          dp[i - 3] + amount[i - 1] + amount[i]))

    print(dp[n - 1])


solution()
