def gcd(x,y):
    if x<y:
        x,y = y, x
    while y>0:
        x, y = y, x%y
    return x

N= int(input())
li= [int(input()) for _ in range(N)]
li.sort()
s_li=[]
end=False
if len(li)==2:
    s_li.append(gcd(li[0],li[1]))
for i in range(2, int(max(li)**(0.5))):
    first=True
    it = iter(li)
    renewed_gcd=next(it)
    for j in range(len(li)-1):
        next_num = next(it)-i
        if min(li)==next_num:
            end=True
            break
        if first ==True:
            renewed_gcd = gcd(renewed_gcd-i,next_num)
            first=False
        else:
            renewed_gcd = gcd(renewed_gcd,next_num)
    if end==True:
        break
    if renewed_gcd > 1:
        s_li.append(renewed_gcd)

for ele in set(s_li):
    print(ele, end=" ")