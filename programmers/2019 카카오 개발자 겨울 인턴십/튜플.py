def solution(s):
    answer = []
    tuples = s[1:-1].split('},{')
    tuples[0] = tuples[0][1:]
    tuples[-1] = tuples[-1][:-1]
    tuples = [list(map(int, x.split(','))) for x in tuples]
    tuples = sorted(tuples, key=lambda tuples: len(tuples))

    answer.append(tuples[0][0])
    for i in range(1, len(tuples)):
        rest = list(set(tuples[i]) - set(tuples[i - 1]))[0]
        answer.append(rest)

    return answer
