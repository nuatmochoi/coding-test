"""
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

- N개의 자연수 중에서 M개를 고른 수열
"""

import itertools as it

n, m = map(int, input().split())
li = list(map(int, input().split()))

p_li = set(list(it.permutations(li, m)))
p_set = sorted(p_li)

for each_tuple in p_set:
    for ele in each_tuple:
        print(ele, end=" ")
    print()