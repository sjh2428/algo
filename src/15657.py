# https://www.acmicpc.net/problem/15652


def go(idx, start, ans, N, M, nums):
    if idx == M:
        for a in ans:
            print(a, end=" ")
        print()
        return
    for i in range(start, N + 1):
        ans[idx] = nums[i - 1]
        go(idx + 1, i, ans, N, M, nums)


def solution():
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()
    ans = [0 for _ in range(M)]
    go(0, 1, ans, N, M, nums)


solution()
