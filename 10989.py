"""
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
"""

import sys

n = int(sys.stdin.readline())
arr = [0] * 10001

for i in range(n):
    data = int(sys.stdin.readline())
    arr[data] += 1

for i in range(10001):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)