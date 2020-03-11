"""
<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 
철수는 이 지도를 가지고 연결된 집들의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 
여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다.
대각선상에 집이 있는 경우는 연결된 것이 아니다. 
<그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 
지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.
"""

def dfs(i, j, cnt):
    A[i][j] = 0 # 방문했음을 확인
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1] # 방향벡터
    for way in range(4):
        ii, jj = i + dx[way], j + dy[way]
        if ii>=0 and ii<N and jj>=0 and jj<N: # 범위체크
            if A[ii][jj] == 1: # 해당 부분이 1이면
                cnt = dfs(ii, jj, cnt+1)  # cnt 증가시켜서 근처 확인
    return cnt

N = int(input())
A= [list(map(int, list(input()))) for _ in range(N)]

li=[]
for i in range(N):
    for j in range(N):
        if A[i][j] == 1: # 그룹에 속한다면
            cnt = 0
            li.append(dfs(i, j,1))

print(len(li))
for ele in sorted(li):
    print(ele)