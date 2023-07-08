from collections import deque
N,M = map(int,input().split())

maps = [list(map(int,input().split())) for _ in range(N)]
directy = [-1,-1,-1,0,0,1,1,1]
directx = [-1,0,1,-1,1,-1,0,1]
maxx = 1

def bfs():
    global maxx
    q = deque()
    for i in range(N):
        for j in range(M):
            if maps[i][j]:
                q.append((i, j))

    while q:
        y, x = q.popleft()

        for i in range(8):
            yy = y + directy[i]
            xx = x + directx[i]
            if 0 <= yy < N and 0 <= xx < M:
                if maps[yy][xx] == 0 :
                    maps[yy][xx] = maps[y][x] + 1
                    q.append((yy,xx))
                    maxx = max(maps[yy][xx], maxx)
    return maxx-1

ans = bfs()
print(ans)


