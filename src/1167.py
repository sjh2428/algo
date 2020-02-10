from collections import deque

def bfs(x):
    q.append(x)
    visited[x] = True
    while(len(q) != 0):
        now = q[0]
        q.popleft()
        length = len(node[now])
        for i in range(0, length, 2):
            con = node[now][i]
            dis = node[now][i+1]
            if visited[con] == False:
                visited[con] = True
                q.append(con)
                distance[con] = dis + distance[now]

t = int(input())
q = deque()
visited = [False] * (t+1)
node = [[] for x in range(t+1)]
distance = [0 for x in range(t+1)]
ans = 0

for i in range(t):
    V = list(map(int, input().split()))
    length = len(V)-1
    for j in range(1, length, 2):
        node[V[0]].append(V[j])
        node[V[0]].append(V[j+1])

bfs(1)
visited = [False] * (t+1)
scnd = distance.index(max(distance))
distance = [0 for x in range(t+1)]
bfs(scnd)
print(max(distance))