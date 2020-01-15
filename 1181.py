N= int(input())
li=[]
for i in range(N):
    li.append(input())
s=list(set(li))
s.sort(key=lambda x: (len(x),x)) # if sort func has no parameter -> alphabet is order by ascii 

for ele in s:
    print(ele)