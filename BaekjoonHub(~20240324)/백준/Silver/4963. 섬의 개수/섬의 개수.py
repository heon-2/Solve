from collections import deque

def bfs(y,x) :
    visited[y][x] = True
    q = deque()
    q.append((y,x))
    while q :
        y,x = q.popleft()
        for i in range(8) :
            yy = y + directy[i]
            xx = x + directx[i]
            if 0<=yy<n and 0<=xx<m :
                if not visited[yy][xx] and maps[yy][xx] == 1 :
                    visited[yy][xx] = True
                    q.append((yy,xx))


while True :
    m, n = map(int, input().split())
    if m == 0 and n == 0 :
        break
    maps = [list(map(int,input().split())) for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    directy=[-1,-1,-1,0,0,1,1,1]
    directx = [-1,0,1,-1,1,-1,0,1]
    island = 0
    for i in range(n) :
        for j in range(m) :
            if not visited[i][j] and maps[i][j] == 1 :
                island += 1
                bfs(i,j)
    print(island)


