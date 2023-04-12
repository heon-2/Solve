N = int(input())
graph = [list(input()) for _ in range(N) ]
import copy
from collections import deque
visited1 = [[False]*N for _ in range(N)]
visited2 = [[False]*N for _ in range(N)]
cnt1 = 0
cnt2 = 0
directy = [-1,0,0,1]
directx = [0,-1,1,0]

def bfs1(y,x) :
    global cnt1
    visited1[y][x] = True
    q = deque()
    q.append((y,x))

    while q :
        y,x = q.popleft()
        for i in range(4) :
            dy = y + directy[i]
            dx = x + directx[i]
            if 0<=dy<N and 0<=dx<N and graph[y][x] == graph[dy][dx]:
                if not visited1[dy][dx] :
                    visited1[dy][dx] = True
                    q.append((dy,dx))
    cnt1 += 1

graph2 = copy.deepcopy(graph)
for i in range(N) :
    for j in range(N) :
        if graph2[i][j] == 'G' :
            graph2[i][j] = 'R'
def bfs2(y,x) :
    global cnt2
    visited2[y][x] = True
    q = deque()
    q.append((y,x))

    while q :
        y,x = q.popleft()
        for i in range(4) :
            dy = y + directy[i]
            dx = x + directx[i]
            if 0<=dy<N and 0<=dx<N and graph2[y][x] == graph2[dy][dx]:
                if not visited2[dy][dx] :
                    visited2[dy][dx] = True
                    q.append((dy,dx))
    cnt2 += 1

for i in range(N) :
    for j in range(N) :
        if not visited1[i][j] :
            bfs1(i,j)
        if not visited2[i][j] :
            bfs2(i,j)
print(cnt1,cnt2)