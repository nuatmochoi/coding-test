C = int(input())
for _ in range(C):
    li=list(map(int, input().split()))
    cnt=0
    li.pop(0)
    avg=sum(li)/len(li)
    for ele in li:
        if ele > avg:
            cnt+=1
    rate = str(round(cnt/len(li)*100,3))
    if rate.index('.')==2:
        comp_n=6
    else :
        comp_n=5
    while len(rate) !=comp_n:
        rate=rate+"0"

    print(rate+"%")
