"""
이석원은 조규현과 백승환에게 상대편 마린(류재명)의 위치를 계산하라는 명령을 내렸다.
조규현과 백승환은 각각 자신의 터렛 위치에서 현재 적까지의 거리를 계산했다.

조규현의 좌표 (x1, y1)와 백승환의 좌표 (x2, y2)가 주어지고, 
조규현이 계산한 류재명과의 거리 r1과 백승환이 계산한 류재명과의 거리 r2가 주어졌을 때, 
류재명이 있을 수 있는 좌표의 수를 출력하는 프로그램을 작성하시오.

만약 류재명이 있을 수 있는 위치의 개수가 무한대일 경우에는 -1을 출력한다.
"""

from math import sqrt

for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    d = sqrt((x1-x2)**2 + (y1-y2)**2)

    if d==0:
        if r1==r2: # 두 원이 동일
            print(-1) 
        else: # 원 안에 원(중심 동일)
            print(0) 
    else:
        if d < r1+r2:
            if d+min(r1,r2)==max(r1,r2): # 내접
                print(1)
            elif d+min(r1,r2)<max(r1,r2): # 원 안에 원(중심은 다름)
                print(0)
            else:
                print(2)
        elif d==r1+r2: # 외접
            print(1)
        else: # 두 원이 멀리 떨어짐
            print(0)