import sys
sysInput = sys.stdin.readline


def find_parent_gate(parent_gate, x):
    if parent_gate[x] == x:
        return x
    parent_gate[x] = find_parent_gate(parent_gate, parent_gate[x])
    return parent_gate[x]


def union_parent_gate(parent_gate, a, b):
    a = find_parent_gate(parent_gate, a)
    b = find_parent_gate(parent_gate, b)
    if a < b:
        parent_gate[b] = a
    else:
        parent_gate[a] = b


def solution():
    answer = 0
    G = int(sysInput())
    P = int(sysInput())
    wanted_gates = []
    parent_gate = [x for x in range(G + 1)]
    for _ in range(P):
        wanted_gates.append(int(sysInput()))

    for wanted_gate in wanted_gates:
        x = find_parent_gate(parent_gate, wanted_gate)
        if x == 0:
            break
        union_parent_gate(parent_gate, x, x - 1)
        answer += 1

    return answer


print(solution())
