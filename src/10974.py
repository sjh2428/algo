# https://www.acmicpc.net/problem/10974

import sys
import itertools

sysInput = sys.stdin.readline


def solution():
    N = int(sysInput())
    lst = [x for x in range(1, N + 1)]
    for p in list(itertools.permutations(lst)):
        for num in p:
            print(num, end=" ")
        print()


solution()
