# https://programmers.co.kr/learn/courses/30/lessons/42579


def solution(genres, plays):
    answer = []
    dicts = {}
    sum_dict = {}
    for g in set(genres):
        dicts[g] = []
        sum_dict[g] = 0

    for i, v in enumerate(plays):
        sum_dict[genres[i]] += v
        dicts[genres[i]].append((i, v))

    sorted_sum_dict = sorted(sum_dict.items(), key=lambda x: -x[1])
    for (genre, play_sum) in sorted_sum_dict:
        sorted_dicts = sorted(dicts[genre], key=lambda x: (-x[1], x[0]))
        answer.append(sorted_dicts[0][0])
        if len(sorted_dicts) >= 2:
            answer.append(sorted_dicts[1][0])

    return answer
