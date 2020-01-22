"""
1742년, 독일의 아마추어 수학가 크리스티안 골드바흐는 레온하르트 오일러에게 다음과 같은 추측을 제안하는 편지를 보냈다.

4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다.
예를 들어 8은 3 + 5로 나타낼 수 있고, 3과 5는 모두 홀수인 소수이다. 또, 20 = 3 + 17 = 7 + 13, 42 = 5 + 37 = 11 + 31 = 13 + 29 = 19 + 23 이다.

이 추측은 아직도 해결되지 않은 문제이다.

백만 이하의 모든 짝수에 대해서, 이 추측을 검증하는 프로그램을 작성하시오.
"""

mport sys

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