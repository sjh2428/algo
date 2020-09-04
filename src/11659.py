# https://www.acmicpc.net/problem/11659

from sys import stdin


def solution():
    N, M = map(int, stdin.readline().split())
    A = list(map(int, stdin.readline().split()))
    sum_A = [0 for _ in range(N + 1)]
    sum_A[0] = 0
    for i in range(1, N + 1):
        sum_A[i] = sum_A[i - 1] + A[i - 1]

    for _ in range(M):
        i, j = map(int, stdin.readline().split())
        print(sum_A[j] - sum_A[i - 1])


solution()
