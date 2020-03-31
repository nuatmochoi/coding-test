"""
N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다.
이 수열의 i번째 수부터 j번째 수까지의 합 A[i]+A[i+1]+…+A[j-1]+A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.
"""

n, m = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0

for idx, ele in enumerate(A):
    sum_ele = 0
    for j in range(idx, n):
        sum_ele += A[j]
        if sum_ele == m:
            cnt += 1
        if sum_ele > m:
            break
print(cnt)