"""
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. N개의 자연수는 모두 다른 수이다.

- N개의 자연수 중에서 M개를 고른 수열
- 고른 수열은 오름차순이어야 한다.
"""

import itertools as it

n, m = map(int, input().split())
li = list(map(int, input().split()))

c_li = list(it.combinations(sorted(li), m))

for each_tuple in p_li:
    for ele in each_tuple:
        print(ele, end=" ")
    print() 