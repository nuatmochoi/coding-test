"""
자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.

예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.
"""

def era(N):
    ck=[False for i in range(N+1)]
    ret= []
    for i in range(2, N+1): 
        if ck[i] : continue
        ret.append(i)
        for j in range(i**2,N+1,i): ck[j]=True
    return ret

m=int(input())
n=int(input())
add=0
ans_li=[]
li=era(n)
for ele in range(len(li)):
    if li[ele]>=m:
        add+=li[ele]
        ans_li.append(li[ele])

if len(ans_li)==0: 
    print(-1)
else:
    print(add)
    print(ans_li[0])