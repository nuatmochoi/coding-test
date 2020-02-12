"""
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
"""

# 특정 정수의 등장 여부만 체크 -> dictionary or set 사용 가능

n = int(input())
arr = set(map(int, input().split()))
m = int(input())
x = list(map(int, input().split()))

for i in x:
        if i not in arr:
            print('0')
        else:
            print('1')