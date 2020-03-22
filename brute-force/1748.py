"""
1부터 N까지의 수를 이어서 쓰면 다음과 같이 새로운 하나의 수를 얻을 수 있다.

1234567891011121314151617181920212223...

이렇게 만들어진 새로운 수는 몇 자리 수일까? 이 수의 자릿수를 구하는 프로그램을 작성하시오.
"""

import math

n = int(input())
log = math.floor(math.log10(n))

cnt = 0
result = 0
while cnt != log:
    result += 9*(10**cnt)*(cnt+1)
    cnt+=1

result += ((n+1)-10**cnt)*(cnt+1)
print(result)