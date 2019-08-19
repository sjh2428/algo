def preorder(x):
    if x == -1:
        return
    print(chr(x + ord('A')), end="")
    preorder(lst[x][0])
    preorder(lst[x][1])

def inorder(x):
    if x == -1:
        return
    inorder(lst[x][0])
    print(chr(x + ord('A')), end="")
    inorder(lst[x][1])

def postorder(x):
    if x == -1:
        return
    postorder(lst[x][0])
    postorder(lst[x][1])
    print(chr(x + ord('A')), end="")

t = int(input())
lst = [[-1]*2 for i in range(26)]

for i in range(t):
    ch1, ch2, ch3 = map(str, input().split())
    lst[ord(ch1) - ord('A')][0] = ord(ch2) - ord('A')
    lst[ord(ch1) - ord('A')][1] = ord(ch3) - ord('A')
    if ch2 == '.':
        lst[ord(ch1) - ord('A')][0] = -1
    if ch3 == '.':
        lst[ord(ch1) - ord('A')][1] = -1

preorder(0)
print()
inorder(0)
print()
postorder(0)
print()