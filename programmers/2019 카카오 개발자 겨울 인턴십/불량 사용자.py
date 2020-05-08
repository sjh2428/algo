import itertools
import re


def solution(user_ids, banned_ids):
    regexes_of_banned_ids = []
    matched = []

    # banned_ids의 각 요소들을 regex로 변환
    for banned_id in banned_ids:
        regexes_of_banned_ids.append(re.compile(
            '^' + banned_id.replace('*', '.') + '$'))

    # 순열을 돌다보면 앞부분이 banned_id의 정규표현식의 순서와 일치하는 순열이 나옴
    # 그 순열을 matched 배열에 넣어줌
    for user_ids_perms in list(itertools.permutations(user_ids)):
        cnt = 0
        temp_matched = []
        for idx, banned_id_regex in enumerate(regexes_of_banned_ids):
            res = banned_id_regex.match(user_ids_perms[idx])
            if res:
                cnt += 1
                temp_matched.append(res.group())
        if cnt == len(regexes_of_banned_ids):
            matched.append(temp_matched)

    # matched의 길이가 0이라면 매치되는 밴 아이디는 없는 것
    if len(matched) == 0:
        return 0

    # 마지막 2단계
    answer = [sorted(x) for x in matched]  # 1. 매칭된 순열들의 원소를 정렬해줌
    answer = list(set(map(tuple, answer)))  # 2. 중복된 배열 제거

    return len(answer)
