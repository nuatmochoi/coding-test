"""
N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.
"""

def is_available(candidate, cur_col):
    cur_row = len(candidate)
    for queen_row in range(cur_row):
    	if candidate[queen_row] == cur_col or abs(candidate[queen_row]-cur_col) == cur_row - queen_row:
        	return False
    return True

def DFS(N, cur_row, cur_queens, final_result): # cur_queens : 지금까지 배치된 퀸의 정보
    if cur_row == N:
        final_result.append(cur_queens[:]) # [:] == shallow copy
        return 
    for checking_col in range(N):
        if is_available(cur_queens, checking_col):
            cur_queens.append(checking_col)
            DFS(N, cur_row+1, cur_queens, final_result)
            cur_queens.pop()
        
def solve_n_queens(N):
    final_result = []
    DFS(N, 0, [],final_result)
    return final_result

N = int(input())
print(len(solve_n_queens(N)))