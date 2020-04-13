# https://www.acmicpc.net/problem/9465


def solution():
    T = int(input())
    for _ in range(T):
        n = int(input())
        dp = [[], []]
        arr = [[], []]
        input_arr1 = list(map(int, input().split()))
        input_arr2 = list(map(int, input().split()))

        for x in input_arr1:
            arr[0].append(x)
        for x in input_arr2:
            arr[1].append(x)

        dp[0].append(arr[0][0])
        dp[1].append(arr[1][0])
        dp[0].append(dp[1][0] + arr[0][1])
        dp[1].append(dp[0][0] + arr[1][1])

        for i in range(2, n):
            dp[0].append(max(dp[1][i - 1], dp[1][i - 2]) + arr[0][i])
            dp[1].append(max(dp[0][i - 1], dp[0][i - 2]) + arr[1][i])

        print(max(dp[0][n - 1], dp[1][n - 1]))


solution()
