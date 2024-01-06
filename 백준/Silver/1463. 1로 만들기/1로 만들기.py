# 풀이 2
n = int(input())
dp = [0] * (n+1)
for i in range(2,n+1) :
    a,b,c = 21e8,21e8,21e8
    a = dp[i-1] + 1
    if i % 2 == 0 :
        b = dp[i//2] + 1
    if i % 3 == 0 :
        c = dp[i//3] + 1
    dp[i] = min(a,b,c)
print(dp[n])