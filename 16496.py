# --- 마지막 제출 - 제일 pythonic한 풀이 ---
from functools import cmp_to_key

def compare(x, y):
    if x + y <= y + x:
        return 1
    else:
        return -1
    
def solution():
    N = int(input())
    num_list = input().split()
    print(int(''.join(sorted(num_list, key=cmp_to_key(compare)))))

solution()



# --- 세 번째 제출 - 성공 ---
# def compare(arg1, arg2):
#     return int(arg1 + arg2) >= int(arg2 + arg1)

# def make_big_number(input_list):
#     answer = []
#     answer.append(input_list[0])

#     for input_idx in range(1, len(input_list)):
#         for idx, val in enumerate(answer):
#             input_val = input_list[input_idx]
#             if compare(input_val, val):
#                 answer.insert(idx, input_val)
#                 break
#             # until last idx, if didn't inserted
#             if idx == len(answer) - 1:
#                 answer.append(input_val)
#                 break
#     return answer
    
# def solution():
#     N = int(input())
#     num_list = input().split()
#     print(int(''.join(make_big_number(num_list))))

# solution()



# --- 두 번째 제출 - 성공 ---

# def compare(arg1, arg2):
#     return int(arg1 + arg2) >= int(arg2 + arg1)

# def make_big_number(input_list):
#     answer = []
#     answer.append(input_list[0])

#     for input_idx in range(1, len(input_list)):
#         for idx, val in enumerate(answer):
#             input_val = input_list[input_idx]
#             #print(input_val, val)
#             if compare(input_val, val):
#                 answer.insert(idx, input_val)
#                 #print("---", answer)
#                 break
#             # until last idx, if didn't inserted
#             if idx == len(answer) - 1:
#                 answer.append(input_val)
#                 break
#     return answer
    
# def solution():
#     N = int(input())
#     num_list = list(map(int, input().split()))
#     num_list.sort()
#     str_list = list(map(str, num_list))
#     print(int(''.join(make_big_number(str_list))))

# solution()



# --- 첫 제출 - 시간 초과 ---

# import copy

# def make_big_number(str_list):
#     answer = []
#     answer.append(str_list[0])
#     for idx in range(1, len(str_list)):
#         temp_answer = copy.deepcopy(answer)
#         for idx2 in range(len(answer) + 1):
#             temp_answer2 = copy.deepcopy(answer)
#             temp_answer2.insert(idx2, str_list[idx])
#             if int(''.join(temp_answer)) <= int(''.join(temp_answer2)):
#                 temp_answer = temp_answer2
#         answer = temp_answer
#     return answer
    
# def solution():
#     N = int(input())
#     num_list = list(map(int, input().split()))
#     num_list.sort()
#     str_list = list(map(str, num_list))
#     print(int(''.join(make_big_number(str_list))))

# solution()