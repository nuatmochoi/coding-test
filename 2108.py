from math import floor 
import sys
from collections import Counter


N= int(sys.stdin.readline())
li=[]
for _ in range(N):
    li.append(int(sys.stdin.readline()))
li.sort()
print(round(sum(li)/len(li)))
print(li[floor(len(li)/2)])

s=list(set(li))
s.sort()
d=Counter(li).most_common()
max_freq=d[0][1]
for i in d:
    if not (i[1] == max_freq):
        s.remove(i[0])
        
if len(s)==1:
    print(s[0])
else:
    print(s[1])

print(max(li)-min(li))