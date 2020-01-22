"""
폴리오미노란 크기가 1×1인 정사각형을 여러 개 이어서 붙인 도형이며, 다음과 같은 조건을 만족해야 한다.

-정사각형은 서로 겹치면 안 된다.
-도형은 모두 연결되어 있어야 한다.
-정사각형의 변끼리 연결되어 있어야 한다. 즉, 꼭짓점과 꼭짓점만 맞닿아 있으면 안 된다.

아름이는 크기가 N×M인 종이 위에 테트로미노 하나를 놓으려고 한다. 종이는 1×1 크기의 칸으로 나누어져 있으며, 각각의 칸에는 정수가 하나 쓰여 있다.

테트로미노 하나를 적절히 놓아서 테트로미노가 놓인 칸에 쓰여 있는 수들의 합을 최대로 하는 프로그램을 작성하시오.
"""

""" 
<MEMO>
 - DON'T SORT!
 - 이 상태에서 어떻게 인접한 4 BLOCK만 찾을 수 있을까? 
 - DFS로 고쳐야 할까? 
"""

N, M = map(int,input().split())
p=[]
comp_li=list()
n=[[None]]
li=[]
ans=[]
for _ in range(N):
    p.append(list(map(int,input().split())))
for i in range(N+2):
    for j in range(M+2):
        if i == 0 or i ==N+1:
            li.append(0)
        elif 1 <= i <=N:
            if j==0 or j==M+1:
                li.append(0)
            else:
                li.append((p[i-1][j-1]))

for j in range(M+2):
    n.append(li[j*(M+2):(j+1)*(M+2)])
n.remove([None])
        

for i in range(1,N+1):
    for j in range(1,M+1):
        comp_li=[]
        comp_li.append(n[i-1][j-1])
        comp_li.append(n[i][j-1])
        comp_li.append(n[i+1][j-1])
        
        comp_li.append(n[i-1][j])
        comp_li.append(n[i][j])
        comp_li.append(n[i+1][j])

        comp_li.append(n[i-1][j+1])
        comp_li.append(n[i][j+1])
        comp_li.append(n[i+1][j+1])

        comp_li.sort() 
        print(comp_li)
        print(comp_li[-1]+comp_li[-2]+comp_li[-3]+comp_li[-4])
