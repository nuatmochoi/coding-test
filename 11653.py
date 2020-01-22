"""
정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.
"""

N = int(input())
i=2
li=[]
while N!=1:
    if N%i==0:
        li.append(i)
        N=N/i
    else:
        i+=1
for ele in li:
    print(ele)