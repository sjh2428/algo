# https://www.acmicpc.net/problem/17298

from sys import stdin


def solution():
    N = int(stdin.readline())
    A = list(map(int, stdin.readline().split()))
    ans = [0 for _ in range(N)]
    stk = []
    for i in range(len(A)):
        while stk and stk[-1][1] < A[i]:
            now = stk.pop()
            ans[now[0]] = A[i]
        stk.append((i, A[i]))

    while stk:
        now = stk.pop()
        ans[now[0]] = -1

    for x in ans:
        print(x, end=" ")


solution()
