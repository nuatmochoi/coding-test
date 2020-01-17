# recursive method
def fibo(num):
    if num<=1:
        return num
    return fibo(num-1)+fibo(num-2)

#dp method
def fibo_dp(num):
    cache = [ 0 for idx in range(num+1)] 
    cache[0]=0
    cache[1]=1

    for idx in range(2,num+1):
        cache[idx]=cache[idx-1]+cache[idx-2]
    return cache[num]

n=int(input())
print(fibo_dp(n))