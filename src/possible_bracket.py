def check_bracket(string):
    balance = 0
    for bracket_char in string:
        if balance < 0:
            return False
        if bracket_char == '(':
            balance += 1
        else:
            balance -= 1
    return False if balance != 0 else True


def go(N, left_cnt, right_cnt, bracket_string):
    if left_cnt > N or right_cnt > N:
        return

    if left_cnt == right_cnt:
        if left_cnt == N and right_cnt == N and check_bracket(bracket_string):
            print(bracket_string)

    go(N, left_cnt + 1, right_cnt, bracket_string + '(')
    go(N, left_cnt, right_cnt + 1, bracket_string + ')')


def solution():
    N = int(input())
    go(N, 0, 0, '')


solution()
