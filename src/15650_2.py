# https://www.acmicpc.net/problem/15650


def go(idx, selected, ans, N, M):
    if selected == M:
        for a in ans:
            print(a, end=" ")
        print()
        return
    if idx > N:
        return
    ans[selected] = idx
    go(idx + 1, selected + 1, ans, N, M)
    ans[selected] = 0
    go(idx + 1, selected, ans, N, M)


def solution():
    N, M = map(int, input().split())
    ans = [0 for _ in range(M)]
    go(0, ans, N, M)


solution()
