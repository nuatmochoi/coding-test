"""
숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 
정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.
"""

from collections import Counter

n = int(input())
li = list(map(int, input().split()))

d = dict(Counter(li))
m = int(input())
target = list(map(int, input().split()))

for ele in target:
    if ele in d.keys():
        print(d[ele], end=" ")
    else:
        print(0, end=" ")