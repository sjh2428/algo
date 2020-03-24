# https://www.acmicpc.net/problem/2512

import sys


def solution():
    N = int(input())
    budgets = list(map(int, input().split()))
    M = int(input())
    low, high = 1, max(budgets)

    while low <= high:
        mid = (low + high) // 2
        temp_sum = 0
        for budget in budgets:
            if budget < mid:
                temp_sum += budget
            else:
                temp_sum += mid
        if temp_sum <= M:
            low = mid + 1
        else:
            high = mid - 1

    print(high)


solution()
