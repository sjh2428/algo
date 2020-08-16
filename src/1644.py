# https://www.acmicpc.net/problem/1644

def get_prime_nums(N):
    prime_list = [False] * (N + 1)
    prime_list[0] = prime_list[1] = True
    answer = []
    for i in range(2, N + 1):
        if not prime_list[i]:
            answer.append(i)
            for j in range(i, N + 1, i):
                prime_list[j] = True
    return answer


def solution():
    N = int(input())
    prime_list = get_prime_nums(N)
    l = r = answer = prime_sum = 0

    while True:
        if r == len(prime_list):
            break
        while r < len(prime_list) and prime_sum < N:
            prime_sum += prime_list[r]
            if prime_sum == N:
                answer += 1
            r += 1
        if l == len(prime_list):
            break
        while l < len(prime_list) and prime_sum >= N:
            prime_sum -= prime_list[l]
            if prime_sum == N:
                answer += 1
            l += 1
    print(answer)


solution()
