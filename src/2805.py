# https://www.acmicpc.net/problem/2805


def solution():
    N, M = map(int, input().split())
    tree_heights = list(map(int, input().split()))
    low = 1
    high = max(tree_heights)

    while low <= high:
        mid = (low + high) // 2

        heights_sum = 0
        for height in tree_heights:
            if height > mid:
                heights_sum += height - mid

        if heights_sum >= M:
            low = mid + 1
        else:
            high = mid - 1

    print(high)


solution()
