import sys
sysInput = sys.stdin.readline


def find(parents, x, distance):
    if x == parents[x]:
        return x, distance
    xx, distance_result = find(
        parents, parents[x], distance + (abs(x - parents[x]) % 1000))
    return xx, distance_result


def connect(parents, x, y):  # union
    parents[x] = y


def solution():
    T = int(sysInput())
    N = int(sysInput())

    centers = [x for x in range(N + 1)]
    picked_center = 0

    for _ in range(T):
        while True:
            operator = list(sysInput().split())
            if len(operator) > 0:
                if operator[0] == 'O':
                    centers = [x for x in range(N + 1)]
                    picked_center = 0
                    break
                elif operator[0] == 'E':
                    if picked_center == 0:  # 선택된 센터가 없으면
                        picked_center = int(operator[1])  # 센터를 선택해주고
                        print(0)  # 0을 출력해줌
                    else:  # 선택된 센터가 있으면
                        _x, d = find(centers, picked_center, 0)
                        print(d)
                elif operator[0] == 'I':
                    connect(centers, int(operator[1]), int(operator[2]))


solution()
