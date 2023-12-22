import sys
# input = sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)
n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

directy = [-1,0,0,1]
directx = [0,-1,1,0]

def dfs(y,x,rain) :
    visited[y][x] = True
    for i in range(4) :
        yy = y + directy[i]
        xx = x + directx[i]
        if 0<=yy<n and 0<=xx<n and not visited[yy][xx] :
            if graph[yy][xx] > rain :
                dfs(yy,xx,rain)
    return
# 최대 높이 구하기
max_height = -1
for i in range(n) :
    for j in range(n) :
        max_height = max(graph[i][j],max_height)

maxx = -1
rain = -1
while rain < 100 :
    if rain == max_height :
        # print(1)
        break
    rain += 1
    visited = [[False] * n for _ in range(n)]
    safe = 0
    for i in range(n) :
        for j in range(n) :
            if not visited[i][j] :
                if graph[i][j] > rain :
                    dfs(i,j,rain)
                    safe += 1
    maxx = max(maxx,safe)
print(maxx)


