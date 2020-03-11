"""
수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 
완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

제한사항
- 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
- completion의 길이는 participant의 길이보다 1 작습니다.
- 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
- 참가자 중에는 동명이인이 있을 수 있습니다.
"""

# 동명이인 같은 경우 collections 라이브러리의 Counter 객체를 이용하면 쉽게 풀 수 있다.
# Counter 객체는 요소끼리 subtract가 가능하다. 만약 존재하지 않으면 음수.

def solution(participant, completion):
    d = dict()
    for ele in participant:
        if ele in d:
            d[ele] += 1
        else:
            d[ele] = 1
    for each in completion:
        d[each] -= 1
    answer = ""
    for i in d:
        if d[i] == 1:
            answer = i
    return answer

participant=list(map(str,input().split()))
completion=list(map(str,input().split()))

print(solution(participant,completion))