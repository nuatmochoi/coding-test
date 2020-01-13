import sys

def era(N):
    ck=[False for i in range(N+1)]
    ret= []
    for i in range(2, N+1): 
        if ck[i] : continue
        ret.append(i)
        for j in range(i**2,N+1,i): ck[j]=True
    return ret

ans_li=[]
comp_li=[]
while(True):
    t=int(sys.stdin.readline())
    if(t==0):
        break
    li=era(t)
    for ele in li:
        for j in range(1,len(li)):
            if int(ele)+int(li[j]) == t:
                if int(li[j])>int(ele):
                    comp_li.append([int(ele),int(li[j])])


    if len(comp_li)==0:
        print("Goldbach's conjecture is wrong.")
    else:
        add=comp_li[0][1]+comp_li[0][0]
        print(add,'=',comp_li[0][0],'+',comp_li[0][1])
    ans_li=[]
    comp_li=[]