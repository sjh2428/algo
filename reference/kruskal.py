# 부모 노드를 찾는 함수
def find_parent(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 부모 노드를 합치는 함수
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


# 부모가 같은가
def is_equal_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a == b:
        return True
    return False


class Edge:
    def __init__(self, a, b, distance):
        self.node = [0, 0]
        self.node[0] = a
        self.node[1] = b
        self.distance = distance

    def __lt__(self, otherEdge):
        return self.distance < otherEdge.distance

    def __repr__(self):
        return "distance: %s node[0]: %s node[1]: %s\n" % (self.distance, self.node[0], self.node[1])


def solution():
    N = 7
    M = 11

    v = []
    v.append(Edge(1, 7, 12))
    v.append(Edge(1, 4, 28))
    v.append(Edge(1, 2, 67))
    v.append(Edge(1, 5, 17))
    v.append(Edge(2, 4, 24))
    v.append(Edge(2, 5, 62))
    v.append(Edge(3, 5, 20))
    v.append(Edge(3, 6, 37))
    v.append(Edge(4, 7, 13))
    v.append(Edge(5, 6, 45))
    v.append(Edge(5, 7, 73))

    # 간선의 비용을 기준으로 오름차순 정렬
    v.sort()
    # print(v)

    # 각 정점이 포함된 그래프가 어디인지 저장
    parent = [x for x in range(N)]
    summation = 0

    for x in v:
        # 사이클이 발생하지 않는 경우 그래프에 포함
        if not is_equal_parent(parent, x.node[0] - 1, x.node[1] - 1):
            summation += x.distance
            union_parent(parent, x.node[0] - 1, x.node[1] - 1)

    print(summation)


solution()
