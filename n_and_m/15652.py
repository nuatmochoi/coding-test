"""
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

- 1부터 N까지 자연수 중에서 M개를 고른 수열
- 같은 수를 여러 번 골라도 된다.
- 고른 수열은 비내림차순이어야 한다.
    - 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.
"""

# 중복조합 -> itertools.combinations_with_replacement 

import itertools as it

n, m = map(int, input().split())

li = [i for i in range(1, n+1)]
c_li = list(it.combinations_with_replacement(li, m))

for each_tuple in c_li:
    for i in each_tuple:
        print(i, end=' ')
    print()