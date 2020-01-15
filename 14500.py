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
