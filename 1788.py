def fibo_dp_minus(num):
    if num==0:
        return 0
    cache = [ 0 for idx in range(abs(num)+1)] 
    cache[0]=0
    cache[1]=1
    if num>1:
        for idx in range(2,num+1):
            cache[idx]=cache[idx-1]+cache[idx-2]
    else:
        cache[-1]=1
        for idx in range(-2, -(abs(num)+1), -1):
            cache[idx]=cache[idx+2]-cache[idx+1]
    return cache[num]
    
n= int(input())
num=fibo_dp_minus(n)
if num>0:
    print(1)
elif num==0:
    print(0)
else:
    print(-1)
print(abs(num)%1000000000)