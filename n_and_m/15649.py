"""
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

- 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
"""

import itertools as it


N, M = map(int, input().split())
li= [ i for i in range(1,N+1)]
p_li=list(it.permutations(li,M))
for each_tuple in p_li:
    for ele in each_tuple:
        print(ele, end=' ')
    print()

