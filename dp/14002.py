"""
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 30, 50} 이고, 길이는 4이다.
"""

n = int(input())
arr= list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i],dp[j]+1)

max_value=max(dp)
idx = n
result = []

print(max_value)

while idx != 0:
    if dp[idx-1] == max_value:
        result.append(arr[idx-1])
        max_value -= 1
    idx -= 1

result.reverse()
[print(i, end=' ') for i in result]