import sys
sysInput = sys.stdin.readline


def find_gate(parent_gates, x):
    if parent_gates[x] == x:
        return x
    parent_gates[x] = find_gate(parent_gates, parent_gates[x])
    return parent_gates[x]


def union_gate(parent_gates, a, b):
    a = find_gate(parent_gates, a)
    b = find_gate(parent_gates, b)
    if a > b:
        parent_gates[a] = b
    else:
        parent_gates[b] = a


def solution():
    answer = 0
    G = int(sysInput())
    P = int(sysInput())
    parent_gates = [x for x in range(G + 1)]
    wanted_gates = []

    for _ in range(P):
        wanted_gates.append(int(sysInput()))

    for wanted_gate in wanted_gates:
        x = find_gate(parent_gates, wanted_gate)
        if x == 0:
            break
        union_gate(parent_gates, x, x - 1)
        answer += 1

    return answer


print(solution())
