"""
신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다.
한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.

예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자. 
1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐 3번과 6번 컴퓨터까지 전파되어
2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다. 
하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.

어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 
컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 
1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.
"""

# 시작 정점에서부터 도달할 수 있는 노드의 수를 계산 (DFS,BFS)
# 컴퓨터의 수가 작으므로 python의 재귀 한계에 걸리지 않고 DFS로 빠르게 해결 가능

n = int(input())
m = int(input())
adj = [[] for _ in range(n+1)]
visited = [False] *(n+1)
count=0

for _ in range(m):
    x,y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

def dfs(now_pos):
    global count
    count +=1 # 방문할 때마다 count를 증가
    visited[now_pos] = True 
    for next_pos in adj[now_pos]:
        if not visited[next_pos]:
            dfs(next_pos)

dfs(1)
print(count-1) # 시작 정점 제외