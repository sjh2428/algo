# https://programmers.co.kr/learn/courses/30/lessons/67256
# 키패드 누르기


def get_height_position(start):
    if start in [1, 2, 3]:
        return 0
    elif start in [4, 5, 6]:
        return 1
    elif start in [7, 8, 9]:
        return 2
    elif start in ['*', 0, '#']:
        return 3


def get_height_distance(height_position, distance):
    for i in range(len(distance)):
        distance[i] -= height_position
        distance[i] = abs(distance[i])


def get_distance(start, dest):
    distance = [0, 1, 2, 3]
    height_position = get_height_position(start)
    get_height_distance(height_position, distance)
    if start not in [2, 5, 8, 0]:
        for i in range(len(distance)):
            distance[i] += 1
    return distance[get_height_position(dest)]


def solution(numbers, hand):
    answer = ''
    NOW = {
        "LEFT": '*',
        "RIGHT": '#'
    }
    for number in numbers:
        if number in [1, 4, 7]:
            NOW["LEFT"] = number
            answer += 'L'
        elif number in [3, 6, 9]:
            NOW["RIGHT"] = number
            answer += 'R'
        else:
            left_distance = get_distance(NOW["LEFT"], number)
            right_distance = get_distance(NOW["RIGHT"], number)
            if left_distance < right_distance:
                NOW["LEFT"] = number
                answer += 'L'
            elif left_distance > right_distance:
                NOW["RIGHT"] = number
                answer += 'R'
            else:
                if hand == "right":
                    NOW["RIGHT"] = number
                    answer += 'R'
                else:
                    NOW["LEFT"] = number
                    answer += 'L'

    return answer
