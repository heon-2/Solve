from collections import deque

n = int(input())
graph = [list(input()) for _ in range(n)]
directy = [-1, 0, 0, 1]
directx = [0, -1, 1, 0]


def bfs(y, x, color):
    visited[y][x] = True
    q = deque()
    q.append((y, x))
    while q:
        y, x = q.popleft()
        for i in range(4):
            yy = y + directy[i]
            xx = x + directx[i]
            if 0 <= yy < n and 0 <= xx < n and not visited[yy][xx] and graph[yy][xx] == color:
                visited[yy][xx] = True
                q.append((yy, xx))

case1,case2 = 0,0
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, graph[i][j])
            case1 += 1
# RGB 적녹색약의 경우 R이랑 G랑 반복문 돌려서 같게 맞추고 다시 bfs 대입
visited = [[False] * n for _ in range(n)]
for i in range(n) :
    for j in range(n) :
        if graph[i][j] == 'R' :
            graph[i][j] = 'G'

for i in range(n) :
    for j in range(n) :
        if not visited[i][j]:
            bfs(i, j, graph[i][j])
            case2 += 1

print(case1,end=' ')
print(case2)