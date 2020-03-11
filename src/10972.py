# https://www.acmicpc.net/problem/10972


def next_permutation(perm):
    n = len(perm)
    i = n - 1
    while i > 0 and perm[i - 1] >= perm[i]:
        i -= 1

    if i <= 0:
        return False

    j = n - 1
    while perm[j] <= perm[i - 1]:
        j -= 1
    perm[i - 1], perm[j] = perm[j], perm[i - 1]

    k = n - 1
    while i < k:
        perm[i], perm[k] = perm[k], perm[i]
        i += 1
        k -= 1

    return True


def solution():
    N = int(input())
    perm = list(map(int, input().split()))
    if next_permutation(perm):
        for num in perm:
            print(num, end=" ")
        print()
    else:
        print(-1)


solution()
