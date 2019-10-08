# Binary Search, Parametric Search
# N - 아이들의 수
# M - 색상의 수
import sys
import math
sysInput = sys.stdin.readline

def is_ok(mid, N, color):
    summation = 0
    print('summation = 0', end='')
    for i in color:
        summation += i // mid
        # print(' + ', i // mid, '(', i, '//', mid, ')', end='')
        if (i % mid != 0): summation += 1
        # print(' + ', (i // mid) + 1, '((', i, '//', mid, ') + 1)', end='')
    print(' =', summation)
    return summation <= N

def solution():
    N, M = map(int, input().split())
    color = []
    M_max = 0

    for _ in range(M):
        i = int(input())
        color.append(i)
        M_max = max(M_max, i)

    first, mid, last = 1, 0, M_max
    answer = 1000000000
    while first <= last:
        mid = (first + last) // 2
        print('first', first, ', last', last, ', mid', mid)
        if (is_ok(mid, N, color)):
            last = mid - 1
            answer = min(mid, answer)
        else:
            first = mid + 1
    return answer

print('answer =', solution())

# import sys
# import math
# sysInput = sys.stdin.readline

# def isPossible(mid, N, color):
#     count = 0
#     for n in color:
#         count += ((n-1) // mid)+1
#     return count <= N

# def solution():
#     N, M = map(int, input().split())
#     color = []
#     M_max = 0

#     for _ in range(M):
#         i = int(input())
#         color.append(i)
#         M_max = max(M_max, i)

#     left, right = 1, M_max
#     while left <= right:
#         mid = (left + right) >> 1
#         if (isPossible(mid, N, color)):
#             right = mid - 1
#         else:
#             left = mid + 1
#     return left

# print(solution())