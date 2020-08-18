# https://www.acmicpc.net/problem/1918

# case: A*(B*(C+D)/E)/F
# answer: ABCD+*E/*F/
# case: A+B*C/D-E
# answer: ABC*D/+E-
# case: A*(B*(C+(D+E*F/G)*H+I)/J-K)+L/M-N
# answer: ABCDEF*G/+H*+I+*J/K-*LM/+N-
# case: A+B*C/D+E*F-G
# answer: ABC*D/+EF*+G-
# case: A+B*C+D*E+G
# answer: ABC*+DE*+G+
# case: A*B+C*(D+E-(F+G*H-I)*J*K*(L-M*N+O)+P/Q-R)/S-T*U/W
# answer: AB*CDE+FGH*+I-J*K*LMN*-O+*-PQ/+R-*S/+TU*W/-
# case: A+(B*C)*D*E+F
# answer: ABC*D*E*+F+
# case: A+B*C+D
# answer: ABC*+D+

def print_without_bracket(stk):
    if len(stk) > 0:
        last_elem = stk.pop()
        if last_elem != '(':
            print(last_elem, end='')


def solution():
    priority = {
        '*': 2, '/': 2,
        '+': 1, '-': 1,
        '(': 0
    }
    expression = input()
    stk = []
    for exp in expression:
        if 'A' <= exp <= 'Z':
            print(exp, end='')
        elif exp == '(':
            stk.append(exp)
        elif exp == ')':
            while len(stk) > 0 and stk[-1] != '(':
                print(stk.pop(), end='')
            stk.pop()
        else:
            while len(stk) > 0 and priority[stk[-1]] >= priority[exp] and stk[-1] != '(':
                print_without_bracket(stk)
            stk.append(exp)
    while len(stk) != 0:
        print_without_bracket(stk)


solution()
