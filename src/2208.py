# https://www.acmicpc.net/problem/2208

def solution():
    N, M = map(int, input().split())
    arr = []
    dp = [0] * N
    for i in range(N):
        arr.append(int(input()))

    dp[0] = arr[0]
    for i in range(1, N):
        dp[i] = dp[i - 1] + arr[i]

    answer = min_val = 0
    for i in range(M, N):
        min_val = min(dp[i - M], min_val)
        answer = max(dp[i] - min_val, answer)

    print(answer)


solution()
