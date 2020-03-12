# https://www.acmicpc.net/problem/6603


def go(n, lotto, picked_lotto, i):
    if len(picked_lotto) == n:
        for num in picked_lotto:
            print(num, end=" ")
        print()
        return
    if i < len(lotto):
        picked_lotto.append(lotto[i])
        go(n, lotto, picked_lotto, i + 1)
        picked_lotto.pop()
        go(n, lotto, picked_lotto, i + 1)


def solution():
    while True:
        t = list(map(int, input().split()))
        if t[0] == 0:
            break
        t.pop(0)
        go(6, t, [], 0)
        print()


solution()
