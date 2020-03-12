# https://www.acmicpc.net/problem/14501


def go(day, sum, T, P, N):
    if day > N:
        return 0
    if day == N:
        return sum
    return max(go(day + T[day], sum + P[day], T, P, N), go(day + 1, sum, T, P, N))


def solution():
    N = int(input())
    T, P = [], []
    for _ in range(N):
        ti, pi = map(int, input().split())
        T.append(ti)
        P.append(pi)
    print(go(0, 0, T, P, N))


solution()
