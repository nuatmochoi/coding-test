"""
수열 A가 주어졌을 때, 그 수열의 증가 부분 수열 중에서 합이 가장 큰 것을 구하는 프로그램을 작성하시오.
"""

import copy

n = int(input())
A = list(map(int, input().split()))

dp = copy.deepcopy(A)

for i in range(1,n):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(A[i] + dp[j], dp[i])

print(max(dp))