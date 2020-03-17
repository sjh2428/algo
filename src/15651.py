# https://www.acmicpc.net/problem/15651


def go(idx, ans, check, N, M):
    if idx == M:
        for a in ans:
            print(a, end=" ")
        print()
        return
    for i in range(1, N + 1):
        check[i] = True
        ans[idx] = i
        go(idx + 1, ans, check, N, M)
        check[i] = False


def solution():
    N, M = map(int, input().split())
    check = [False for _ in range(N + 1)]
    ans = [0 for _ in range(M)]
    go(0, ans, check, N, M)


solution()
