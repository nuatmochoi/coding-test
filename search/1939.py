"""
N(2≤N≤10,000)개의 섬으로 이루어진 나라가 있다. 이들 중 몇 개의 섬 사이에는 다리가 설치되어 있어서 차들이 다닐 수 있다.

영식 중공업에서는 두 개의 섬에 공장을 세워 두고 물품을 생산하는 일을 하고 있다. 
물품을 생산하다 보면 공장에서 다른 공장으로 생산 중이던 물품을 수송해야 할 일이 생기곤 한다.
그런데 각각의 다리마다 중량제한이 있기 때문에 무턱대고 물품을 옮길 순 없다. 만약 중량제한을 초과하는 양의 물품이 다리를 지나게 되면 다리가 무너지게 된다.

한 번의 이동에서 옮길 수 있는 물품들의 중량의 최댓값을 구하는 프로그램을 작성하시오.
"""

# 문제에서 중량제한이 10억으로 매우 큰 값이기 때문에 이 값을 찾기 위해서는 log나 root를 씌워야함.
# 찾고자 하는 값에 대해서 이분탐색을 수행한다고 보면 된다.

from collections import deque

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]

def bfs(c):
    queue = deque([start_node])
    visited = [False] * (n+1)
    visited[start_node] = True
    while queue:
        x = queue.popleft()
        for y, weight in adj[x]:
            if not visited[y] and weight >= c:
                visited[y] = True
                queue.append(y)
    return visited[end_node]

start = 1000000000
end = 1

for _ in range(m):
    x, y, w = map(int, input().split())
    adj[x].append((y, w)) 
    adj[y].append((x, w))
    start = min(start, w) # 가장 중량이 작은 것을 start에 넣고
    end = max(end, w) # 가장 중량이 큰 것을 end에 넣음

start_node, end_node = map(int, input().split())

result = start
while(start <= end):
    mid = (start + end) // 2
    if bfs(mid): # 이동 가능
        result = mid
        start = mid + 1
    else: 
        end = mid -1

print(result)