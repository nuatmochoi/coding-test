"""
자연수 과 정수 가 주어졌을 때 이항 계수 를 구하는 프로그램을 작성하시오.
"""

# 계산에서 항상 분모에 0 들어가는 조건처리 조심할 것!

n,k = map(int, input().split())

up = 1
down =1

while True:
    if k == 0:
        break
    up = up * n
    down = down *k
    n -= 1
    k -= 1
    
print(up//down)