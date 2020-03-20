"""
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

- 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
- 고른 수열은 오름차순이어야 한다.
"""

import itertools as it

n, m = map(int, input().split())
li = [i for i in range(1, n+1)]
c_li = list(it.combinations(li, m))

for each_tuple in c_li:
    for i in each_tuple:
        print(i, end=" ")
    print()