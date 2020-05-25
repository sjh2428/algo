# https://www.acmicpc.net/problem/1924


def solution():
    x, y = map(int, input().split())
    end_of_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    yoil = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    days = 0
    for i in range(x - 1):
        days += end_of_days[i]
    days += y
    days %= 7
    print(yoil[days])


solution()
