N = int(input())
i=2
li=[]
while N!=1:
    if N%i==0:
        li.append(i)
        N=N/i
    else:
        i+=1
for ele in li:
    print(ele)