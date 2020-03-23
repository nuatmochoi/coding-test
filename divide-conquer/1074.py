"""
한수는 2차원 배열 (항상 2^N * 2^N 크기이다)을 Z모양으로 탐색하려고 한다. 
예를 들어, 2*2배열을 왼쪽 위칸, 오른쪽 위칸, 왼쪽 아래칸, 오른쪽 아래칸 순서대로 방문하면 Z모양이다.
만약, 2차원 배열의 크기가 2^N * 2^N라서 왼쪽 위에 있는 칸이 하나가 아니라면, 
배열을 4등분 한 후에 (크기가 같은 2^(N-1)로) 재귀적으로 순서대로 방문한다.

다음 예는 2^2 * 2^2 크기의 배열을 방문한 순서이다.
N이 주어졌을 때, (r, c)를 몇 번째로 방문하는지 출력하는 프로그램을 작성하시오.
"""

N, r, c = map(int, input().split())

def Z(size, x, y):
    if size == 1:
        return 0
    size = size // 2
    for i in range(2):
        for j in range(2):
            if x < size * (i+1) and y < size * (j+1):
                return (i*2+j) * (size*size) + Z(size, x-size*i, y-size*j)

print(Z(2**N, r, c))