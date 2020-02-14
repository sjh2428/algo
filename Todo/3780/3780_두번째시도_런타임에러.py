import sys
sys.setrecursionlimit(100000)


def find(parents, distances, x):
    if x == parents[x]:
        return x
    p = find(parents, distances, parents[x])
    distances[x] += distances[parents[x]]
    parents[x] = p
    return p


def connect(parents, distances, x, y):  # union
    parents[x] = y
    distances[x] = abs(x - y) % 1000


def solution():
    T = int(input())
    N = int(input())

    centers = [x for x in range(N + 1)]
    distances = [0 for _ in range(N + 1)]

    for _ in range(T):
        while True:
            operator = list(input().split())
            if len(operator) > 0:
                if operator[0] == 'O':
                    centers = [x for x in range(N + 1)]
                    distances = [0 for _ in range(N + 1)]
                    break
                elif operator[0] == 'E':
                    enterprise = int(operator[1])
                    find(centers, distances, int(enterprise))
                    print(distances[enterprise])
                elif operator[0] == 'I':
                    connect(centers, distances, int(
                        operator[1]), int(operator[2]))


solution()
