from collections import deque
import sys
input = sys.stdin.readline
directy = [-1,-1,-1,0,0,1,1,1]
directx = [-1,0,1,-1,1,-1,0,1]

while True :
    island = 0
    w,h = map(int,input().split())
    if w==0 and h==0 :

        break
    graph = [list(map(int,input().split())) for _ in range(h) ]
    visited = [[False]*w for _ in range(h) ]

    def bfs(y,x) :

        q = deque()
        q.append((y,x))
        visited[y][x] = True

        while q :
            yy,xx = q.popleft()
            for i in range(8) :
                dy = yy + directy[i]
                dx = xx + directx[i]
                if 0<=dy<h and 0<=dx<w and graph[dy][dx] == 1 :
                    if not visited[dy][dx] :
                        visited[dy][dx] = True
                        q.append((dy,dx))

    for i in range(h) :
        for j in range(w) :
            if graph[i][j] == 1 :
                if not visited[i][j] :
                    island += 1
                    bfs(i,j)
    print(island)
