# https://programmers.co.kr/learn/courses/30/lessons/67257
# 수식 최대화


import itertools


def calc(a, b, op):
    if op == '*':
        return a * b
    elif op == '-':
        return a - b
    elif op == '+':
        return a + b


def solution(expression):
    answer = []
    operators = ['*', '-', '+']
    op_stack = []
    num_stack = []
    prev_idx = 0
    for i in range(len(expression)):
        if expression[i] in operators:
            num_stack.append(int(expression[prev_idx: i]))
            op_stack.append(expression[i])
            prev_idx = i + 1
    num_stack.append(int(expression[prev_idx: len(expression)]))
    num_stack = num_stack[::-1]
    op_stack = op_stack[::-1]

    for ops in list(map(''.join, itertools.permutations(operators))):
        new_op_stack = op_stack[:]
        new_num_stack = num_stack[:]
        for op in list(ops):
            temp_op_stack = []
            temp_num_stack = []
            while len(new_op_stack) != 0:
                temp_num_stack.append(new_num_stack.pop())
                temp_op_stack.append(new_op_stack.pop())
                if temp_op_stack[-1] == op:
                    temp_op_stack.pop()
                    a = temp_num_stack.pop()
                    b = new_num_stack.pop()
                    new_num_stack.append(calc(a, b, op))
            new_op_stack += temp_op_stack[::-1]
            new_num_stack += temp_num_stack[::-1]
        answer.append(abs(new_num_stack[0]))

    return max(answer)
