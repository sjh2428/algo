def dfs(x):
    global parent, node, visited
    if visited[x]:
        return
    visited[x] = True
    for i in node[x]:
        if not visited[i]:
            parent[i] = x
            dfs(i)

t = int(input())
parent = [-1] * (t+1)
node = [[] for i in range(t+1)]
visited = [False] * (t+1)

for i in range(t-1):
    n, p = map(int, input().split())
    node[n].append(p)
    node[p].append(n)

dfs(1)

for i in range(2, t+1):
    print(parent[i])