import sys

sysInput = sys.stdin.readline


def solution():
    M = int(sysInput())
    S = set()
    for _ in range(M):
        ORDER = sysInput().split()
        if ORDER[0] == "add":
            S.add(int(ORDER[1]))
        elif ORDER[0] == "remove":
            S.discard(int(ORDER[1]))
        elif ORDER[0] == "check":
            print("1" if int(ORDER[1]) in S else "0")
        elif ORDER[0] == "toggle":
            if int(ORDER[1]) in S:
                S.discard(int(ORDER[1]))
            else:
                S.add(int(ORDER[1]))
        elif ORDER[0] == "all":
            S = set([v for v in range(1, 21)])
        elif ORDER[0] == "empty":
            S = set()


solution()
