# https://www.acmicpc.net/problem/11048


def solution():
    N, M = map(int, input().split())
    miro = []
    for _ in range(N):
        miro.append(list(map(int, input().split())))

    dp = [[0 for x in range(M)] for y in range(N)]
    dp[0][0] = miro[0][0]
    for i in range(1, M):
        dp[0][i] = dp[0][i - 1] + miro[0][i]
    for i in range(1, N):
        dp[i][0] = dp[i - 1][0] + miro[i][0]

    for i in range(1, N):
        for j in range(1, M):
            dp[i][j] = max(dp[i - 1][j],
                           dp[i][j - 1],
                           dp[i - 1][j - 1]) + miro[i][j]

    print(dp[N - 1][M - 1])


solution()
