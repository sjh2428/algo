# https://www.acmicpc.net/problem/6603


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
    while True:
        case = list(map(int, input().split()))
        if (case[0] == 0):
            break
        case.pop(0)
        bool_perm = [0 if x < 6 else 1 for x in range(len(case))]
        while True:
            for i in range(len(bool_perm)):
                if bool_perm[i] == 0:
                    print(case[i], end=" ")
            print()

            if not next_permutation(bool_perm):
                break
        print()


solution()
