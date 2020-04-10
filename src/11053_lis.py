def solution():
    N = int(input())
    A = list(map(int, input().split()))
    dp = [0 for _ in range(N)]
    for i in range(N):
        dp[i] = 1
        for j in range(i):
            if A[i] > A[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1

    print(max(dp))


solution()
