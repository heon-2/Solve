from collections import deque
M,N,K = map(int,input().split())
graph = [[0]*N for _ in range(M)]
visited = [[False]*N for _ in range(M)]

for i in range(K):
    x1,x2,y1,y2 = map(int,input().split())
    for j in range(x2,y2) :
        for k in range(x1,y1) :
            graph[j][k] = 1

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
            if 0<=dy<M and 0<=dx<N and graph[dy][dx]== 0 :
                if not visited[dy][dx] :
                    cnt += 1
                    visited[dy][dx] = True
                    q.append((dy,dx))
    return cnt

lst = []
for i in range(M) :
    for j in range(N) :
        if graph[i][j] == 0 :
            if not visited[i][j] :
                v = bfs(i,j)
                lst.append(v)
lst.sort()
print(len(lst))
print(*lst)