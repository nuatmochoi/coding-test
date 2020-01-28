import itertools

N, S = map(int,input().split())
li = list(map(int,input().split()))
case_li=[]
cnt=0

for i in range(1,len(li)+1):
    for ele in list(itertools.combinations(li,i)):
        case_li.append(ele)

for each_tuple in case_li:
    if sum(each_tuple)==S:
        cnt+=1
print(cnt)