"""
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 30, 50} 이고, 길이는 4이다.
"""

# LIS -> O(N^2)
# D[i] : arr[i]를 마지막 ele로 가지는 부분 수열의 최대 길이
# D[i] = max(D[i],D[j]+1) if arr[j] < arr[i]

n = int(input())
arr = list(map(int, input().split()))
dp  = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))