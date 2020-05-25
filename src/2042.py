# https://www.acmicpc.net/problem/2042


def init(lst, tree, node_num, start, end):
    if (start == end):
        temp = lst[start]
        tree[node_num] = temp
        return temp
    else:
        temp = init(lst, tree, node_num * 2, start, (start + end) // 2) + \
            init(lst, tree, node_num * 2 + 1, ((start + end) // 2) + 1, end)
        tree[node_num] = temp
        return temp


# node가 담당하는 구간 [start, end]
# 합을 구해야 하는 구간 [left, right]
def subSum(tree, node_num, start, end, left, right):
    # 겹치는 구간이 없음
    if left > end or right < start:
        return 0

    # 구해야 하는 범위는 [left, right]인데 [start, end]는 그 범위에 포함되고
    # 그 node의 자식도 모두 포함되기 때문에 더 이상 호출을 하는 것은 비효율적
    if left <= start and end <= right:
        return tree[node_num]

    return subSum(tree, node_num * 2, start, (start + end) // 2, left, right) + \
        subSum(tree, node_num * 2 + 1, ((start + end) // 2) + 1, end, left, right)


def update(tree, node_num, start, end, index, diff):
    if index < start or index > end:
        return
    tree[node_num] = tree[node_num] + diff
    if (start != end):
        update(tree, node_num * 2, start, (start + end) // 2, index, diff)
        update(tree, node_num * 2 + 1, ((start + end) // 2) + 1, end, index, diff)


def solution():
    n, m, k = map(int, input().split())
    lst = []
    tree = [0] * 3000000

    for _ in range(n):
        lst.append(int(input()))

    init(lst, tree, 1, 0, n - 1)

    for _ in range(m + k):
        a, b, c = map(int, input().split())

        if a == 1:
            b -= 1
            diff = c - lst[b]
            lst[b] = c
            update(tree, 1, 0, n - 1, b, diff)
        elif a == 2:
            print(subSum(tree, 1, 0, n - 1, b - 1, c - 1))


solution()
