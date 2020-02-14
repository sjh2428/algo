# 부모 노드를 찾는 함수
def find_parent(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent, parent[x])
    p = parent[x]
    return p


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
