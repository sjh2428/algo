# https://www.acmicpc.net/problem/1806


N, S = map(int, input().split())
A = list(map(int, input().split()))

l, r = 0, 0
candidates = []
cur_sum = 0

while True:
    if r == len(A):
        break
    while cur_sum < S and r < len(A):
        cur_sum += A[r]
        if cur_sum >= S:
            candidates.append([l, r])
        r += 1
    if l == len(A):
        break
    while cur_sum >= S and l < len(A):
        cur_sum -= A[l]
        l += 1
        if cur_sum >= S:
            candidates.append([l, r - 1])

if len(candidates) == 0:
    print(0)
else:
    answer = [candidates[0][0], candidates[0][1]]
    for candidate in candidates:
        if candidate[1] - candidate[0] < answer[1] - answer[0]:
            answer = [candidate[0], candidate[1]]
    print(answer[1] - answer[0] + 1)
