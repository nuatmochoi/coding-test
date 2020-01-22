"""
N이 주어졌을 때, fibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.
"""

def fino_dp(num):
    cache= [ 0 for i in range(num+1)]
    cnt = [ 0 for i in range(num+1)]
    cache[0]=0
    cnt[0]=(1,0)
    if num==0:
        return cnt[num]
    cache[1]=1
    cnt[1]=(0,1)
    for idx in range(2, num+1):
        cnt[idx]=tuple(sum(ele) for ele in zip(cnt[idx-1],cnt[idx-2]))
    return cnt[num]

T=int(input())
for _ in range(T):
    n=int(input())
    print(fino_dp(n)[0], fino_dp(n)[1])