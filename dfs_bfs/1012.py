"""
차세대 영농인 한나는 강원도 고랭지에서 유기농 배추를 재배하기로 하였다. 
농약을 쓰지 않고 배추를 재배하려면 배추를 해충으로부터 보호하는 것이 중요하기 때문에,
한나는 해충 방지에 효과적인 배추흰지렁이를 구입하기로 결심한다.
이 지렁이는 배추근처에 서식하며 해충을 잡아 먹음으로써 배추를 보호한다.
특히, 어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면 이 지렁이는 인접한 다른 배추로 이동할 수 있어,
그 배추들 역시 해충으로부터 보호받을 수 있다.

(한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있다고 간주한다)

한나가 배추를 재배하는 땅은 고르지 못해서 배추를 군데군데 심어놓았다.
배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로 
서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 총 몇 마리의 지렁이가 필요한지 알 수 있다.

(0은 배추가 심어져 있지 않은 땅이고, 1은 배추가 심어져 있는 땅을 나타낸다.)
"""

# 연결 요소의 개수를 세는 문제
# 모든 정점에 대해 DFS or BFS 수행, 방문한 정점은 재확인 X
# 전체적으로 DFS or BFS의 총 수행 횟수 계산
# DFS를 푸는 경우 sys.setrecursionlimit() 설정 필요 - python basic recursionlimit == 1000

import sys
sys.setrecursionlimit(100000)

def dfs(x, y):
    visited[x][y] = True
    directions = [ (-1,0), (1,0), (0, -1), (0,1)] # 상하좌우
    for dx, dy in directions: # 상하좌우에 대해서 
        nx, ny = x+ dx, y+dy # next_x , next_y가
        if nx < 0 or nx >=n or ny< 0 or ny >=m: # 2차원 배열에 포함되어 있기만 하면
            continue
        if array[nx][ny] and not visited[nx][ny]: # 방문하지 않은 경우를 제외하고, 배추가 심어져있는 경우에
            dfs(nx,ny) # dfs를 처리하도록

for _ in range(int(input())): # 모든 테스트케이스에 대해
    m,n,k = map(int,input().split())
    array = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    for _ in range(k):
        y,x = map(int, input().split()) 
        array[x][y] = 1
    result = 0 
    for i in range(n): # 모든 정점에 대해서 dfs를 수행하는데, 조건은
        for j in range(m):
            if array[i][j] and not visited[i][j]: # 정점이 방문되지 않았을 때만!
                dfs(i,j) # dfs가 실행될 떄마다 
                result +=1 # result에 1을 더해 수행횟수 계산
    print(result)