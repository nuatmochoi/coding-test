from collections import deque


def dfs(v): # 일반적으로는 stack으로 구현 but 재귀로 구현 가능
    print(v, end=' ')
    visited[v] = True # 한번 방문한 거는 방문 처리
    for e in adj[v]: # 정점에 연결되어 있는 모든 다른 정점에 대해
        if not(visited[e]):
            dfs(e) # 전부다 dfs를 재귀적으로 수행

def bfs(v):
    q = deque([v]) 
    while q: # q가 빌 때까지 반복 수행
        v= q.popleft()
        if not(visited[v]):
            visited[v] = True
            print(v, end=' ')
            for e in adj[v]: # 정점에 연결되어 있는 모든 정점을 확인하며
                if not visited[e]: # 방문하지 않았다면
                    q.append(e) # queue에 넣어줌

n, m, v = map(int, input().split())
adj =  [[] for _ in range(n+1)] # 기본적으로 연결리스트 사용 -> N+1개

for _ in range(m):
    x, y = map(int, input().split()) # 어떤 두개의 정점이 연결되어 있다고 하면
    adj[x].append(y) # 각각 서로의 연결 리스트에 추가
    adj[y].append(x) # same as above

# 문제에서 낮은 것부터 방문하라고 했다면 이렇게 sorting 추가할 것
for e in adj: # 모든 연결되어 있는 각각의 정점에 대한 연결 리스트에 대해서
    e.sort() # 정렬시켜서 -> 낮은 것부터 방문할 수 있게 
   

visited = [False] * (n+1) # 방문한 정점을 다시 방문하지 않도록 초기화
dfs(v)
print()
visited = [False] * (n+1)
bfs(v)