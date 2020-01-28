m,n,k = map(int,input().split())
if m==n and m==k :
    print(10000+m*1000)
elif m==n or m==k :
    print(1000+m*100)
elif n==k :
    print(1000+n*100)
else:
    print(max(m,n,k)*100)