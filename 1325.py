"""
해커 김지민은 잘 알려진 어느 회사를 해킹하려고 한다. 이 회사는 N개의 컴퓨터로 이루어져 있다. 
김지민은 귀찮기 때문에, 한 번의 해킹으로 여러 개의 컴퓨터를 해킹 할 수 있는 컴퓨터를 해킹하려고 한다.

이 회사의 컴퓨터는 신뢰하는 관계와, 신뢰하지 않는 관계로 이루어져 있는데, 
A가 B를 신뢰하는 경우에는 B를 해킹하면, A도 해킹할 수 있다는 소리다.

이 회사의 컴퓨터의 신뢰하는 관계가 주어졌을 때, 
한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 출력하는 프로그램을 작성하시오.
"""

# 모든 정점에 대해 DFS or BFS 수행
# DFS or BFS를 수행할 때마다 방문하게 되는 node의 수 계산
# 가장 노드의 개수가 크게 되는 시작 정점 출력

from collections import deque

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    adj[y].append(x) # 연결된 간선에 대한 정보

def bfs(v): # 연결된 간선이 많기 떄문에 bfs가 유리
    q = deque([v])
    visited = [False] * (n+1)
    visited[v] = True
    count = 1 # 특정 정점 부터 시작해서
    while q:
        v= q.popleft()
        for e in adj[v]:
            if not visited[e]:
                q.append(e)
                visited[e] = True
                count +=1 # 방문할 때마다 count++
    return count

result =[]
max_value = -1

for i in range(1, n+1):
    c = bfs(i) # 모든 정점에 대해 수행
    if c > max_value: # count 값이 가장 큰 경우를 찾기 위함
        result = [i]
        max_value = c
    elif c == max_value: # 가장 count 값이 클 때에
        result.append(i) # 시작 정점 값을 담아줌
        max_value = c

for e in result:
    print(e, end=' ')