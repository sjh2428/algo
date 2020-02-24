from sys import stdin

sysInput = stdin.readline


def find(parents, distances, x):
    if parents[x] == x:
        return x
    p = find(parents, distances, parents[x])
    distances[x] += distances[parents[x]]
    parents[x] = p
    return p


def union(parents, distances, i, j):
    parents[i] = j
    distances[i] = abs(i - j) % 1000


def solution():
    T = int(sysInput())  # 테스트 케이스
    for _ in range(T):
        N = int(sysInput())  # 기업의 수
        parents = [x for x in range(N + 1)]
        distances = [0 for _ in range(N + 1)]
        while True:
            order = sysInput().split()
            OP, I, J = 0, 1, 2
            OP = order[OP]
            if OP == 'E':
                I = int(order[I])
                find(parents, distances, I)
                print(distances[I])
            elif OP == 'I':
                I, J = int(order[I]), int(order[J])
                union(parents, distances, I, J)
            elif OP == 'O':
                break


solution()
