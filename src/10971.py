# https://www.acmicpc.net/problem/10971


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
    ans = 9999999999
    w = []
    N = int(input())

    for _ in range(N):
        w.append(list(map(int, input().split())))

    d = [x for x in range(N)]

    while True:
        can_i_go = True
        res = 0
        for i in range(N - 1):
            if w[d[i]][d[i + 1]] == 0:
                can_i_go = False
                break
            else:
                res += w[d[i]][d[i + 1]]

        if can_i_go and w[d[N - 1]][d[0]] != 0:
            res += w[d[N - 1]][d[0]]
            if ans > res:
                ans = res

        if not next_permutation(d):
            break

    print(ans)


solution()
