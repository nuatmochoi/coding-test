# 짝수는 소수가 아니다
# N이 소수가 되려면, 2보다 크거나 같고, 루트 N보다 작거나 같은 자연수로 나눠지면 안 된다.

def prime(n):
    if n<2:
        return False
    if n is 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3,round(n**0.5)+1,2):
        if n % i == 0:
            return False
    return True

cnt=0
N=int(input())
li=list(input().split())
for ele in li:
    if prime(int(ele))==True:
        cnt+=1
print(cnt)


