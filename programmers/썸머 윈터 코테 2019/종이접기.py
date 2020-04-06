def solution(n):
    answer = [0]
    i = 1
    hollzzack = 0
    if n > 1:
        answer.pop()
        while i < 2**n:
            if i % 4 == 0:
                answer.append(answer[(i // 4) - 1])
                i += 1
            else:
                i += 3
                if hollzzack % 2 == 0:
                    answer += [0, 0, 1]
                else:
                    answer += [0, 1, 1]
                hollzzack += 1
    return answer

# 0
# 001
# 001 0 011
# 001 0 011 0 001 1 011
# 001 0 011 0 001 1 011 0 001 0 011 1 001 1 011
