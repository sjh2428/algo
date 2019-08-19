M, N = map(int, input().split())
v = [False] * (N + 1)
v[1] = True
for i in range(1, N+1):
    if v[i] == False:
        v[i] = True
        if M <= i and i <= N:
            print(i)
        for j in range(i, N + 1, i):
            if v[j] == False:
                v[j] = True