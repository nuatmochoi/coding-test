"""
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.

1+1+1+1
1+1+2
1+2+1
2+1+1
2+2
1+3
3+1

정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.
"""

import sys

dp = [0 for _ in range(11)]
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 4

for _ in range(int(input())):
    n = int(sys.stdin.readline().rstrip())
    for i in range(4, n+1):
        dp[i] = dp[i-3]+dp[i-2]+dp[i-1]
    print(dp[n])