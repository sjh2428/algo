# https://www.acmicpc.net/problem/4673

MAX_N = 10001


def makeTrue(i, n_list):
    now_sum = i
    for j in str(i):
        now_sum += int(j)
    if now_sum < MAX_N:
        n_list[now_sum] = True
        makeTrue(now_sum, n_list)


def solution():
    n_list = [False for _ in range(MAX_N)]
    for i in range(1, MAX_N):
        if n_list[i]:
            continue
        print(i)
        makeTrue(i, n_list)


solution()
