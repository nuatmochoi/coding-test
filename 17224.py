"""
현정이는 L 만큼의 역량을 가지고 있어 L보다 작거나 같은 난이도의 문제를 풀 수 있다. 또한 현정이는 코딩이 느리기 때문에 대회 시간이 부족해 K개보다 많은 문제는 해결할 수 없다. 어떤 문제에 대해 쉬운 버전을 해결한다면 100점을 얻고, 어려운 버전을 해결한다면 여기에 40점을 더 받아 140점을 얻게 된다. 어려운 버전을 해결하면 쉬운 버전도 같이 풀리게 되므로, 한 문제를 해결한 것으로 계산한다.

현정이가 APC에 참가했다면 최대 몇점을 얻을 수 있었을지 알려주자.
"""

N, L, K = map(int, input().split())
li=[tuple(map(int,input().split())) for _ in range(N)]
score=0
cnt=0
for ele in li:
    if ele[0]>L and ele[1]>L:
        li.remove(ele)
li.sort(key=lambda x: x[1])
for ele in li:
    if cnt==K:
        break
    if ele[1]<=L:
        score+=140
        cnt+=1
    elif ele[0]<=L:
        score+=100
        cnt+=1
print(score)