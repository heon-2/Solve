import sys
from collections import deque
input = sys.stdin.readline
M,N = map(int,input().split())
graph = [ list(map(int,input().rstrip())) for _ in range(N) ]
visited = [[0]*M for _ in range(N)]
directy = [-1,0,0,1]
directx = [0,-1,1,0]

def bfs(y,x) :
    q = deque()
    q.append((y,x))
    visited[y][x] = 1
    while q :
        y,x = q.popleft()
        for i in range(4) :
            yy = y + directy[i]
            xx = x + directx[i]
            if 0 <= yy < N and 0 <= xx < M :
                if visited[yy][xx] == 0  :
                    # 0이면 그냥 이동할 수 있으니깐 벽 부수기 횟수에 포함 x
                    if graph[yy][xx] == 0 :
                        visited[yy][xx] = visited[y][x]
                        q.appendleft((yy,xx))
                    # 1이면 벽이니깐 부숴야해서 부순 횟수에 포함
                    elif graph[yy][xx] == 1 :
                        visited[yy][xx] = visited[y][x] + 1
                        q.append((yy,xx))
    return visited[N-1][M-1]-1

print(bfs(0,0))