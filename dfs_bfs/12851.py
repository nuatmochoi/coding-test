"""
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 그리고, 
가장 빠른 시간으로 찾는 방법이 몇 가지 인지 구하는 프로그램을 작성하시오.
"""

from collections import deque 

def bfs():
    ans, cnt = 0, 0
    q = deque([n])
    while not cnt:
        s = len(q)
        while s:
            s -= 1
            now_pos = q.popleft()
            if now_pos == k: 
                cnt += 1
            for next_pos in (now_pos-1, now_pos+1, now_pos*2): # 3가지 이동 경우에 대하여
                if next_pos < 0 or next_pos > MAX-1: # 범위 안에 포함된 경우
                    continue
                if not array[next_pos] or array[next_pos] == array[now_pos]+1:  # 방문하지 않았거나, 방문했더라도 이동거리가 같다면
                    array[next_pos] = array[now_pos] + 1 # 이전 정점에서 1을 더하여, 최소시간 갱신
                    q.append(next_pos)
        ans += 1
    print("%d\n%d" %(ans-1, cnt))

MAX = 100001
n, k = map(int,input().split())
array = [0] * MAX
bfs()