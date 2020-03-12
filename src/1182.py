# https://www.acmicpc.net/problem/1182


def go(nums, S, now_sum, i):
    if i == len(nums):
        if now_sum == S:
            return 1
        else:
            return 0
    if i < len(nums):
        return go(nums, S, now_sum + nums[i], i + 1) + go(nums, S, now_sum, i + 1)


def solution():
    N, S = map(int, input().split())
    nums = list(map(int, input().split()))
    print(go(nums, S, 0, 0) if S != 0 else go(nums, S, 0, 0) - 1)
    # 공집합 제외


solution()
