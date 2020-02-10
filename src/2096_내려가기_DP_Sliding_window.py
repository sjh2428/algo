# N = int(input())
# rows = [[0, 0, 0]]
# answer = [0, 0, 0]
# for i in range(N):
#     row = []
#     row = list(map(int, input().split()))
#     row[0] += min([rows[i][0], rows[i][1]])
#     row[1] += min([rows[i][0], rows[i][1], rows[i][2]])
#     row[2] += min([rows[i][1], rows[i][2]])
#     rows.append(row)
# print(rows)
import sys
sysInput = sys.stdin.readline

MIN, MAX = 0, 1
N = int(sysInput())
answer = [[0, 0, 0], [0, 0, 0]]

for _ in range(N):
    row = list(map(int, sysInput().split()))
    minRow, maxRow = row[:], row[:]
    minRow[0] += min([answer[MIN][0], answer[MIN][1]])
    minRow[1] += min([answer[MIN][0], answer[MIN][1], answer[MIN][2]])
    minRow[2] += min([answer[MIN][1], answer[MIN][2]])
    answer[MIN] = minRow
    maxRow[0] += max([answer[MAX][0], answer[MAX][1]])
    maxRow[1] += max([answer[MAX][0], answer[MAX][1], answer[MAX][2]])
    maxRow[2] += max([answer[MAX][1], answer[MAX][2]])
    answer[MAX] = maxRow

print(max(answer[MAX]), min(answer[MIN]))
