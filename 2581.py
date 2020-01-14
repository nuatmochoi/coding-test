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