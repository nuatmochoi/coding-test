"""
대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.
첫째 줄에는 테스트 케이스의 개수 C가 주어진다.

둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
"""

C = int(input())
for _ in range(C):
    li=list(map(int, input().split()))
    cnt=0
    li.pop(0)
    avg=sum(li)/len(li)
    for ele in li:
        if ele > avg:
            cnt+=1
    rate = str(round(cnt/len(li)*100,3))
    if rate.index('.')==2:
        comp_n=6
    else :
        comp_n=5
    while len(rate) !=comp_n:
        rate=rate+"0"

    print(rate+"%")
