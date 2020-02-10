def is_ans():
    return ans == val
def val_add():
    for i in range(len(val)):
        val[i] += 1
        if val[i] > criteria[i]:
            val[i] %= criteria[i]

ans = list(map(int, input().split()))
val = [1, 1, 1]
cnt = 1
criteria = [15, 28, 19]
while not is_ans():
    val_add()
    cnt += 1
print(cnt)