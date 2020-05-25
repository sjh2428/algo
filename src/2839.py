# https://www.acmicpc.net/problem/2839


def solution():
    N = int(input())
    total = 0
    cnt = 0
    while total < N:
        total += 5
        cnt += 1

    if N - total < 0:
        total -= 5
        cnt -= 1

    if N != total:
        if (N - total) % 3 != 0:
            while (N - total) % 3 != 0:
                total -= 5
                cnt -= 1
                if total < 0:
                    return -1

        while total != N:
            total += 3
            cnt += 1

    return cnt


print(solution())
