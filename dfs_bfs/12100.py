"""
첫째 줄에 보드의 크기 N (1 ≤ N ≤ 20)이 주어진다. 둘째 줄부터 N개의 줄에는 게임판의 초기 상태가 주어진다. 
0은 빈 칸을 나타내며, 이외의 값은 모두 블록을 나타낸다. 
블록에 쓰여 있는 수는 2보다 크거나 같고, 1024보다 작거나 같은 2의 제곱꼴이다. 블록은 적어도 하나 주어진다.

최대 5번 이동시켜서 얻을 수 있는 가장 큰 블록을 출력한다.
"""

# 상하좌우 이동 같은경우는 map을 회전시키는 것이 더 효율적

from copy import deepcopy # deepcopy 함수의 내용을 그대로 복사하되, 주소값은 복사 X

def rotate90(A, n):
    new_A = deepcopy(A)
    for i in range(n):
        for j in range(n):
            new_A[j][n-1-i] = A[i][j] # 90도 회전
    return new_A

def convert(li, n):
    new_li = [i for i in li if i] # 0이 아닌 숫자만 남김
    for i in range(1, len(new_li)):
        if new_li[i-1] == new_li[i]:
            new_li[i-1] *= 2
            new_li[i] = 0
    new_li = [i for i in new_li if i]
    return new_li + [0] * (n-len(new_li))

def dfs(n, A, cnt):
    ret = max([max(i) for i in A])
    if cnt == 0:
        return ret
    for _ in range(4): # 회전하면서 최대값만 갱신
        x = [convert(row, n) for row in A]
        if x != A:
            ret = max(ret, dfs(n, x, cnt-1))
        A = rotate90(A, n)
    return ret

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

print(dfs(n, board, 5))