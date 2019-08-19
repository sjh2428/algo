def find_lier(total, smalls):
    for i in range(len(smalls) - 1):
        for j in range(i + 1, len(smalls)):
            if total - (smalls[i] + smalls[j]) == 100:
                return [smalls[i], smalls[j]]

smalls = []
for _ in range(9):
    small = int(input())
    smalls.append(small)

smalls.sort()
total = sum(smalls)
lier_list = find_lier(total, smalls)
for small in smalls:
    if small in lier_list:
        continue
    print(small)