"""
지민이는 항구에서 일한다. 그리고 화물을 배에 실어야 한다. 모든 화물은 박스에 안에 넣어져 있다. 
항구에는 크레인이 N대 있고, 1분에 박스를 하나씩 배에 실을 수 있다. 모든 크레인은 동시에 움직인다.

각 크레인은 무게 제한이 있다. 이 무게 제한보다 무거운 박스는 크레인으로 움직일 수 없다. 
모든 박스를 배로 옮기는데 드는 시간의 최솟값을 구하는 프로그램을 작성하시오.
"""

import sys

n = int(input())
w_limit = list(map(int, input().split()))
m = int(input())
w = list(map(int, input().split()))

if max(w_limit) < max(w):
    print(-1)
    sys.exit()

pos = [0] * n # 크레인이 옮겨야되는 박스 번호
check = [False] * m # 박스를 옮겼는지

w.sort(reverse=True)
w_limit.sort(reverse=True)

cnt = 0
ret = 0

while True:
    if cnt == len(w):
        break
    for i in range(n):
        while pos[i] < len(w):
            if not check[pos[i]] and w_limit[i] >= w[pos[i]]: # 옮겨지지 않은 박스 중에서, 옮길 수 있는 박스를 찾을 때까지 반복
                check[pos[i]] = True
                pos[i] += 1
                cnt +=1
                break
            pos[i] += 1
    ret += 1

print(ret)