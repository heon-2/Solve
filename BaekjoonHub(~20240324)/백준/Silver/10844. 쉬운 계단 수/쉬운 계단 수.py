# 값이 m인 개수는 이전 행의 m-1 개수 + m+1

n = int(input())
# DP 테이블 초기화
dp = [[0] * 10 for _ in range(n+1)]

# n = 1 일 때 세팅.
for i in range(1, 10):
    dp[1][i] = 1

# 나머지 자릿수의 경우의 수 탐색
for i in range(2, n+1):
    for j in range(10):
        # 가장 뒤에 오는 숫자가 0일 땐, 오른쪽 위만
        if j == 0:
            dp[i][j] = dp[i-1][j+1]

        # 가장 뒤에 오는 숫자가 1~8일 땐, 왼쪽 대각선위 + 오른쪽 대각선 위
        elif 1 <= j <= 8:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

        # 가장 뒤에 오는 숫자가 9일 땐, 그 앞에 8만 올 수 있습니다.
        else:
            dp[i][j] = dp[i-1][j-1]

print(sum(dp[n]) % 1000000000)