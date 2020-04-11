"""
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

첫째 줄에 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.
둘째 줄에 어떻게 이동해야 하는지 공백으로 구분해 출력한다.
"""

from collections import deque  

def bfs(n):
    q = deque([n])
    while q:
        now_pos = q.popleft()
        if now_pos == k:
            print(array[now_pos])
            p = []
            while now_pos != n:
                p.append(now_pos)
                now_pos = path[now_pos]
            p.append(n)
            p.reverse()
            print(' '.join(map(str,p)))
            return
        for next_pos in (now_pos-1, now_pos+1, now_pos*2): 
            if 0 <= next_pos < MAX and not array[next_pos]: 
                path[next_pos]= now_pos
                array[next_pos] = array[now_pos] +1 
                q.append(next_pos)

MAX = 100001
n, k = map(int,input().split())
array = [0] * MAX
path = [0] * MAX
bfs(n)
