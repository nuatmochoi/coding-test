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
