import sys

li = []
for _ in range(9):
    li.append(int(sys.stdin.readline().rstrip()))

max_num = max(li)
print(max_num)
print(li.index(max_num)+1)