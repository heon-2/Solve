n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
graph.reverse()
dp = []
for i in range(len(graph)) :
    dp.append([0]*len(graph[i]))
dp[0] = graph[0]
for i in range(1,n) :
    for j in range(len(dp[i])) :
        dp[i][j] = max(dp[i-1][j],dp[i-1][j+1]) + graph[i][j]
print(dp[-1][0])