# https://programmers.co.kr/learn/courses/30/lessons/67258
# 보석 쇼핑


def solution(gems):
    candidates = []
    gems_set = set(gems)
    l, r = 0, 0
    frequency = {}
    while True:
        if r == len(gems):
            break
        while r < len(gems) and len(frequency.keys()) != len(gems_set):
            if gems[r] not in frequency:
                frequency[gems[r]] = 1
            else:
                frequency[gems[r]] += 1
            r += 1

        if l == len(gems):
            break
        while l < len(gems) and len(frequency.keys()) == len(gems_set):
            frequency[gems[l]] -= 1
            if frequency[gems[l]] == 0:
                del frequency[gems[l]]
            candidates.append([l, r - 1])
            l += 1

    answer = [candidates[0][0], candidates[0][1]]
    for candidate in candidates:
        if candidate[1] - candidate[0] < answer[1] - answer[0]:
            answer = [candidate[0], candidate[1]]

    return [x + 1 for x in answer]
