import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
directy = [-1,0,0,1]
directx = [0,-1,1,0]

def dfs(y,x) :
    global width
    visited[y][x] = True
    for i in range(4) :
        yy = directy[i] + y
        xx = directx[i] + x
        if 0<=yy<n and 0<=xx<m :
            if not visited[yy][xx] and graph[yy][xx] == 1:
                dfs(yy,xx)
                width += 1
    return
max_width = 0
paper = 0
for i in range(n) :
    for j in range(m) :
        if not visited[i][j] and graph[i][j] :
            width = 1
            dfs(i,j)
            max_width = max(width,max_width)
            paper += 1
print(paper)
print(max_width)
