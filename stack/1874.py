import sys

li=[]
result = []
num = 1

for _ in range(int(input())):
    target = int(sys.stdin.readline().rstrip())
    while num <= target:
        li.append(num)
        result.append("+")
        num += 1
    if target == li.pop():
        result.append("-")
    else:
        print("NO")
        exit()

print('\n'.join(result))