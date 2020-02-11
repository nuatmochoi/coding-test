"""
밑면이 정사각형인 직육면체 벽돌들을 사용하여 탑을 쌓고자 한다.
탑은 벽돌을 한 개씩 아래에서 위로 쌓으면서 만들어 간다. 
아래의 조건을 만족하면서 가장 높은 탑을 쌓을 수 있는 프로그램을 작성하시오.

1. 벽돌은 회전시킬 수 없다. 즉, 옆면을 밑면으로 사용할 수 없다.
2. 밑면의 넓이가 같은 벽돌은 없으며, 또한 무게가 같은 벽돌도 없다.
3. 벽돌들의 높이는 같을 수도 있다.
4. 탑을 쌓을 때 밑면이 좁은 벽돌 위에 밑면이 넓은 벽돌은 놓을 수 없다.
5. 무게가 무거운 벽돌을 무게가 가벼운 벽돌 위에 놓을 수 없다.
"""

# 벽돌을 무게 기준으로 정렬한 다음
# D[i] : index가 i인 벽돌이 가장 아래일 때 최대 높이
# LIS의 응용 문제

n = int(input())
arr = []

arr.append((0,0,0,0))
for i in range(1, n+1):
    area, h, w = map(int,input().split())
    arr.append((i, area, h, w))

arr.sort(key=lambda x: x[3])

dp = [0] * (n+1)

for i in range(1, n+1):
    for j in range(0, i):
        if arr[i][1] > arr[j][1]:
            dp[i] = max(dp[i],dp[j]+arr[i][2])

max_value = max(dp)
index = n 
result= []

while index != 0: # max값부터 idx 역추적
    if max_value == dp[index]:
        result.append(arr[index][0])
        max_value -= arr[index][2]
    index -= 1

result.reverse()
print(len(result))
[print(i) for i in result]