def solution(stones, k):
    low = min(stones)
    high = max(stones)

    while low <= high:
        mid = (low + high) // 2
        check = 0

        for i in range(len(stones)):
            if stones[i] - mid > 0:
                check = 0
            else:
                check += 1
            if check >= k:
                high = mid - 1
                break
            if i == len(stones) - 1:
                low = mid + 1

    answer = low
    return answer
