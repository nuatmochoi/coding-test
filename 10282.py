"""
최흉최악의 해커 yum3이 네트워크 시설의 한 컴퓨터를 해킹했다! 
이제 서로에 의존하는 컴퓨터들은 점차 하나둘 전염되기 시작한다.
어떤 컴퓨터 a가 다른 컴퓨터 b에 의존한다면, b가 감염되면 그로부터 일정 시간 뒤 a도 감염되고 만다.
이때 b가 a를 의존하지 않는다면, a가 감염되더라도 b는 안전하다.

최흉최악의 해커 yum3이 해킹한 컴퓨터 번호와 각 의존성이 주어질 때,
해킹당한 컴퓨터까지 포함하여 총 몇 대의 컴퓨터가 감염되며 그에 걸리는 시간이 얼마인지 구하는 프로그램을 작성하시오.
"""

# 다익스트라 최단 경로 알고리즘 (그래프가 주어지고, 최소 시간, 최대 시간 구하는 문제일 때)
# 우선순위 큐 -> O(NlogD)

import heapq # 우선순위 큐
import sys
input= sys.stdin.readline

def dijkstra (start) :
    heap_data = []
    heapq.heappush(heap_data,(0,start)) # heap에 (cost=0, 시작 정점)
    distance[start] = 0
    while heap_data:
        dist, now = heapq.heappop(heap_data) # 꺼낸 정점을 확인한 다음
        if distance[now] < dist:
            continue
        for i in adj[now]: # 현재 보고 있는 정점을 거쳐서 
            cost = dist + i[1] # 다른 정점까지의 거리를 계산
            if distance[i[0]] > cost: # 다른 정점까지의 거리보다 distance에 담긴 값이 더 큰 경우에만 
                distance[i[0]] = cost # 갱신
                heapq.heappush(heap_data, (cost,i[0])) # 그 경우에 한해, 우선순위 큐에 새로운 정점까지의 cost를 담음
                # 함수가 끝났을 때 distance table에 각 정점으로 갈 수 있는 최단 거리가 담겨지게 될 것임

for _ in range(int(input())):
    n, m, start = map(int, input().split())
    adj= [[] for i in range(n+1)]
    distance = [1e9] * (n+1) # 10^9 == INF
    for _ in range(m):
        x, y, cost = map(int, input().split()) # y가 x를 감염
        adj[y].append((x, cost)) # 따라서 y 정점의 연결 리스트에 x 정점을 넣음 (y에서 x로 연결)
    dijkstra(start)
    count = 0 
    max_distance = 0
    for i in distance:
        if i != 1e9: # INF가 아니라면
            count +=1 # count
            if i > max_distance: # 각 정점으로 가는 distance를 확인한 다음
                max_distance = i # 가장 큰 값을 max_distance 변수에 담음
    print(count, max_distance) # 도달 가능 정점 개수와 최단 거리 출력