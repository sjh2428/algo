# https://www.acmicpc.net/problem/9372
import sys
from queue import Queue

sysInput = sys.stdin.readline


def bfs(start, schedule, v):
    answer = 0
    q = Queue()
    q.put(start)
    v[start] = True

    while q.qsize() != 0:
        now = q.get()
        for s in schedule[now]:
            if not v[s]:
                answer += 1
                v[s] = True
                q.put(s)

    return answer


def solution():
    T = int(sysInput())
    for _ in range(T):
        N, M = map(int, sysInput().split())
        schedule = [[] for _x in range(N + 1)]
        v = [False for _x in range(N + 1)]
        for __ in range(M):
            a, b = map(int, sysInput().split())
            schedule[a].append(b)
            schedule[b].append(a)
        print(bfs(1, schedule, v))


solution()
