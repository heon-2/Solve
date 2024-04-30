n = int(input())
dp = [0] * 91
dp[0] = 0
dp[1] = 1
for i in range(2,n+1) :
    dp[i] = dp[i-2] + dp[i-1]
print(dp[n])

'''
[풀이 일자] : 2024.04.30
[문제 출처] : 백준
[난이도] : Bronze 3
[문제 유형] : DP
[문제 풀이] : 전형적인 DP
'''