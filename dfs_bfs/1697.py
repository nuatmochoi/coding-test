"""
수빈이는 동생과 숨바꼭질을 하고 있다.
수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 
수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.
"""

# 숨바꼭질 문제 - 특정 위치까지 이동하는 최단 시간 계산
from collections import deque  # 이동 시간이 1초로 동일하므로 bfs(너비우선탐색) 을 이용해서 풀 수 있는 문제

MAX = 100001
n, k = map(int,input().split())
array = [0] * MAX

def bfs():
    q = deque([n])
    while q:
        now_pos = q.popleft()
        if now_pos ==k:
            return array[now_pos]
        for next_pos in (now_pos-1, now_pos+1, now_pos*2): # 3가지 이동 경우를 확인 
            if 0 <= next_pos < MAX and not array[next_pos]: # 범위 안에 포함되어 있고, 방문하지 않았다면 
                array[next_pos] = array[now_pos] +1 # 이전 정점에다 1을 더함으로 새 정점에서의 최소시간 계산
                q.append(next_pos)

print(bfs())