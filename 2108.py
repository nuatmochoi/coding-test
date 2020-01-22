"""
수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.

1.산술평균 : N개의 수들의 합을 N으로 나눈 값
2.중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
3.최빈값 : N개의 수들 중 가장 많이 나타나는 값
4.범위 : N개의 수들 중 최댓값과 최솟값의 차이
N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.
"""

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