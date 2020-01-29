"""
세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.
"""

li=[]

for _ in range(3):
    li.append(tuple(map(int, input().split())))
if li[0][0]==li[1][0]:
    first=li[2][0]
else:
    if li[0][0]==li[2][0]:
        first=li[1][0]
    else:
        first=li[0][0]

if li[0][1]==li[1][1]:
    second=li[2][1]
else:
    if li[0][1]==li[2][1]:
        second=li[1][1]
    else:
        second=li[0][1]

print(first, second)