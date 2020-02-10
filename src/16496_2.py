def compare(arg1, arg2):
    return int(arg1 + arg2) >= int(arg2 + arg1)

def make_big_number(input_list):
    answer = []
    answer.append(input_list[0])

    for input_idx in range(1, len(input_list)):
        for idx, val in enumerate(answer):
            input_val = input_list[input_idx]
            if compare(input_val, val):
                answer.insert(idx, input_val)
                break
            # until last idx, if didn't inserted
            if idx == len(answer) - 1:
                answer.append(input_val)
                break
    return answer
    
def solution():
    N = int(input())
    num_list = input().split()
    print(int(''.join(make_big_number(num_list))))

solution()
