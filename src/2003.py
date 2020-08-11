# https://www.acmicpc.net/problem/2003


N, M = map(int, input().split())
A = list(map(int, input().split()))

answer = 0
cur_sum = 0
l, r = 0, 0

while True:
    if r == len(A):
        break
    while cur_sum < M and r < len(A):
        cur_sum += A[r]
        if cur_sum == M:
            answer += 1
        r += 1
    if l == len(A):
        break
    while cur_sum >= M and l < len(A):
        cur_sum -= A[l]
        if cur_sum == M:
            answer += 1
        l += 1

print(answer)
