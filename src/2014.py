# https://www.acmicpc.net/problem/2014

import heapq


def solution():
    K, N = map(int, input().split())
    prime_numbers = list(map(int, input().split()))
    hq = [x for x in prime_numbers]
    heapq.heapify(hq)
    for i in range(N - 1):
        front = heapq.heappop(hq)
        for pnum in prime_numbers:
            mul_val = front * pnum
            heapq.heappush(hq, mul_val)
            if front % pnum == 0:
                break

    print(heapq.heappop(hq))


solution()
