"""
준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.

동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.
"""

def count_each_coin(li,money):
    cnt=0  
    for ele in li:
        if money>=ele:
            each_cnt = int(money//ele)
            cnt+=each_cnt
            money=money-each_cnt*ele
            if money ==0:
                return cnt

N, K = map(int,input().split())

li = [int(input()) for _ in range(N)]
filtered_li =[]
for ele in li:
    if ele < K:
        filtered_li.append(ele)
filtered_li.sort(reverse=True)

print(count_each_coin(filtered_li,K))
