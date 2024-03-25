from collections import deque
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
graph = [ list(input()) for _ in range(N) ]
# print(graph)
directy = [-1,0,0,1]
directx = [0,-1,1,0]
maxx = 0


def bfs(y,x) :
    hour = 0
    q = deque()
    q.append((y,x,hour))
    land = [ [0]*M for _ in range(N) ]
    land[y][x] = 1
    while q :
        y,x,hour = q.popleft()
        for i in range(4) :
            yy = y + directy[i]
            xx = x + directx[i]
            if 0<=yy<N and 0<=xx<M and graph[yy][xx] == 'L' and land[yy][xx] == 0 :
                land[yy][xx] = 1
                q.append((yy,xx,hour+1))
    return hour
for i in range(N) :
    for j in range(M) :
        if graph[i][j] == 'L' :
            maxx = max(bfs(i,j),maxx)

print(maxx)

