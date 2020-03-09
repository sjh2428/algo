import sys

sysInput = sys.stdin.readline


def swap(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp


def perm(lst, depth, n, k):
    if (depth == k):
        print(lst)
        return

    for i in range(depth, n):
        swap(lst, i, depth)
        perm(lst, depth + 1, n, k)
        swap(lst, i, depth)


def solution():
    N = int(sysInput())
    lst = [x for x in range(1, N + 1)]
    perm(lst, 0, N, N)


solution()
