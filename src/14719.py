# https://www.acmicpc.net/problem/14719

from sys import stdin


def solution():
    answer = 0
    H, W = map(int, stdin.readline().split())
    heights = list(map(int, stdin.readline().split()))

    for i in range(H):
        cnt = 0
        flag = False
        for j in range(W):
            if heights[j] > i:  # 벽일 때
                if flag:  # 왼쪽에 벽이 있으며 또다시 벽을 만난 경우
                    if heights[j - 1] > i:  # 연속적으로 벽이 있었을 경우 continue
                        continue
                    answer += cnt
                    cnt = 0
                else:  # 왼쪽에 벽이 없을 경우
                    flag = True  # 왼쪽에 벽이 있으므로 빗물이 고일 수 있음
            if flag and heights[j] <= i:
                cnt += 1

    print(answer)


solution()
