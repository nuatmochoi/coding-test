n = int(input())

dp = [0] * 1001

dp[1]=1
dp[2]=3

for i in range(3, n+1):
    dp[i]= (dp[i-1]+dp[i-2]*2) # 1칸 전에 2*1  or 2칸 전에 (2*2 or 2*1 2개)

print(dp[n]%10007)