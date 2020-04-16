import sys

for _ in range(int(input())):
    n = int(sys.stdin.readline())
    flag = "YES"
    li = []
    for _ in range(n):
        li.append(sys.stdin.readline().rstrip('\n'))

    li.sort()
    for i, j in zip(li, li[1:]):
        if i == j[:len(i)]:
            flag = "NO"

    print(flag)