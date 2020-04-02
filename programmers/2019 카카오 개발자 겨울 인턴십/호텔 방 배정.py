# https://programmers.co.kr/learn/courses/30/lessons/64063

# 첫 시도 : 배열을 사용하여 방의 갯수만큼 미리 방을 만듦
# - 10^12 == 1조 -> 메모리 초과 + 시간초과 + 런타임에러

# 두 번째 시도 : 딕셔너리를 이용하여 시간과 메모리를 아끼고자 하였음
# - 정확성 : 100점, 효율성: 1개 틀리고 다 맞음. 1개는 런타임 에러를 뿜었음

# 세 번째 시도 : 설마라는 생각으로 recursionlimit을 설정
# - 통과

import sys
sys.setrecursionlimit(50000000)


def find(x, parents):
    if x == parents[x]:
        return x
    p = find(parents[x], parents)
    parents[x] = p
    return p


def union(x, y, parents):
    x = find(x, parents)
    y = find(y, parents)

    if x > y:
        parents[y] = x
    else:
        parents[x] = y


def solution(k, room_number):
    answer = []
    parents = {}

    for number in room_number:
        parents[number] = number

    for number in room_number:
        found_number = find(number, parents)
        answer.append(found_number)
        try:
            union(found_number, found_number + 1, parents)
        except Exception as ex:
            parents[found_number + 1] = found_number + 1
            union(found_number, found_number + 1, parents)

    return answer
