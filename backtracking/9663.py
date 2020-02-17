"""
N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.
"""

# x번째 행에 배치한 queen에 대해 검사
def check(x):
    # 이전 행에 놓았던 모든 queen들을 검사
    for i in range(x):
        if row[x] == row[i]:
            return False
        if abs(row[x] - row[i]) == x - i:
            return False
    return True

# x번째 행에 대하여 처리
def dfs(x):
    global result
    if x == n:
        result += 1
    else:
        # x번째 행의 각 열에 queen을 둔다고 가정
        for i in range(n):
            row[x] = i 
            # 해당 위치에 queen 배치가 가능한 경우
            if check(x):
                # 다음 행으로 넘어감
                dfs(x+1)

n = int(input())
row = [0] * n
result = 0
dfs(0)
print(result)

