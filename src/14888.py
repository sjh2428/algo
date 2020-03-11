# https://www.acmicpc.net/problem/14888


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


def div(a, b):
    if a >= 0:
        return a // b
    else:
        return -(-a // b)


def calc(A, op):
    res = A[0]
    for i, operator in enumerate(op):
        if operator == 0:
            res = res + A[i + 1]
        elif operator == 1:
            res = res - A[i + 1]
        elif operator == 2:
            res = res * A[i + 1]
        else:
            res = div(res, A[i + 1])
    return res


def solution():
    ans = []
    max_val, min_val = 0, 9999999999
    N = int(input())
    A = list(map(int, input().split()))
    op_cnt = list(map(int, input().split()))
    op = []  # 0 - 덧셈, 1 - 뺄셈, 2 - 곱셈, 3 - 나눗셈
    for idx, cnt in enumerate(op_cnt):
        for k in range(cnt):
            op.append(idx)
    op.sort()

    while True:
        ans.append(calc(A, op))
        if not next_permutation(op):
            break

    ans.sort()
    print(ans[-1])
    print(ans[0])


solution()
