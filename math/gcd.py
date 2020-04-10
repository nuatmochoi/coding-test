# 단순 반복문
def gcd_naive(a, b):
    for i in range(min(a, b), 0, -1):
        if a%i ==0 and b%i==0: return i

# 유클리드 호제법
def gcd(a, b):
    return gcd(b, a%b) if a%b!=0 else b

# 유클리드 호제법 반복문으로 변경
def gcd2(a, b):
    while a % b !=0 : a, b = b, a%b
    return b

# math 라이브러리 사용
import math
math.gcd(1, 2)


# 아래로 갈수록 최적화 좋음
print(gcd_naive(1, 2))
print(gcd(1, 2))
print(gcd2(1, 2))
print(math.gcd(1, 2))

# LCM은 gcd 이용하여 계산
def lcm(a, b):
    return a*b//gcd(a, b)

print(lcm(2, 4))
