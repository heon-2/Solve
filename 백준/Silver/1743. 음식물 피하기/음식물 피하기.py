N,M,K = map(int,input().split())
graph = [[0]*M for _ in range(N)]
visited = [[False]*M for _ in range(N)]
for i in range(K) :
    r,c = map(int,input().split())
    graph[r-1][c-1] = 1
from collections import deque
directy = [-1,0,0,1]
directx = [0,-1,1,0]
def bfs(y,x) :
    cnt = 1
    q = deque()
    q.append((y,x))
    visited[y][x] = True

    while q :
        yy,xx = q.popleft()
        for i in range(4) :
            dy = yy + directy[i]
            dx = xx + directx[i]
            if 0<= dy<N and 0<=dx<M and graph[dy][dx] == 1 :
                if not visited[dy][dx] :
                    cnt += 1
                    visited[dy][dx] = True
                    q.append((dy,dx))
    return cnt

maxx = -21e8
for i in range(N) :
    for j in range(M) :
        if graph[i][j] == 1 :
            v = bfs(i,j)
            if v > maxx :
                maxx = v

print(maxx)