def solution(n):
    dp = [1] * (n+1)
    for i in range(2,n+1) :
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n] % 1234567

'''
[풀이 일자] : 2024.04.26
[문제 출처] : 프로그래머스
[난이도] : Level 2
[문제 유형] : DP
[문제 풀이] : dp 테이블을 1로 초기화하고, dp[i] = dp[i-1] + dp[i-2] 라는 점화식을 찾아 풀이함.
[배운 점] : dp는 어렵다.... 그렇지만 n=1부터 n=5 정도까지 반복하다보면 규칙성을 찾을 수있음.
'''