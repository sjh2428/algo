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
