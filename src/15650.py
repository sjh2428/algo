# https://www.acmicpc.net/problem/15650


def go(idx, start, ans, N, M):
    if idx == M:
        for a in ans:
            print(a, end=" ")
        print()
        return
    for i in range(start, N + 1):
        ans[idx] = i
        go(idx + 1, i + 1, ans, N, M)


def solution():
    N, M = map(int, input().split())
    ans = [0 for _ in range(M)]
    go(0, 1, ans, N, M)


solution()
