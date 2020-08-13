# https://www.acmicpc.net/problem/17140

def change_row_col(A):
    temp_arr = []
    for col_idx in range(len(A[0])):
        row_arr = []
        for row_idx in range(len(A)):
            row_arr.append(A[row_idx][col_idx])
        temp_arr.append(row_arr)
    return temp_arr


def cal(A):
    max_col_len = 0
    for row_idx in range(len(A)):
        cal_dict = {}
        replace_row_arr = []
        for col in A[row_idx]:
            if col == 0:
                continue
            if col not in cal_dict.keys():
                cal_dict[col] = 1
            else:
                cal_dict[col] += 1
        for k, v in sorted(cal_dict.items(), key=lambda item: (item[1], item[0])):
            replace_row_arr += [k, v]
            max_col_len = max(max_col_len, len(replace_row_arr))
            if len(replace_row_arr) > 100: # 열의 크기가 100을 넘어가면
                replace_row_arr = replace_row_arr[:100] # 100번째까지만
                max_col_len = max(max_col_len, len(replace_row_arr))
                break
        A[row_idx] = replace_row_arr

    for row_idx in range(len(A)):
        for _ in range(max_col_len - len(A[row_idx])):
            A[row_idx].append(0)


def solution():
    r, c, k = map(int, input().split())
    answer, A = 0, []

    for _ in range(3):
        A.append(list(map(int, input().split())))

    while True:
        if r <= len(A) and c <= len(A[r - 1]) and A[r - 1][c - 1] == k:
            return answer
        if len(A) >= len(A[0]):
            cal(A)
        else:
            A = change_row_col(A)
            cal(A)
            A = change_row_col(A)
        answer += 1
        if answer > 100:
            return -1


print(solution())
