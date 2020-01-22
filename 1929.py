"""
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
"""

def era(N):
    ck=[False for i in range(N+1)]
    ret= []
    for i in range(2, N+1): 
        if ck[i] : continue
        ret.append(i)
        for j in range(i**2,N+1,i): ck[j]=True
    return ret

m, n = map(int,input().split())
li= era(n)
for ele in li:
    if ele>=m:
        print(ele)