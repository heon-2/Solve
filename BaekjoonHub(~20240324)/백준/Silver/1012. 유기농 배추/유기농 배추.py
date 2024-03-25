T = int(input())
for tc in range(1,T+1) :
    M,N,K = map(int,input().split())
    graph = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    for i in range(K) :
        X,Y = map(int,input().split())
        graph[Y][X] = 1

    from collections import deque
    cnt = 0
    def bfs(y,x) :
        global cnt
        q = deque()
        q.append((y,x))
        visited[y][x] = True
        directy = [-1,0,0,1]
        directx = [0,-1,1,0]

        while q :
            y,x = q.popleft()
            for i in range(4) :
                dy = y + directy[i]
                dx = x + directx[i]
                if 0<= dy < N and 0<= dx < M and graph[dy][dx] == 1:
                    if not visited[dy][dx] :
                        visited[dy][dx] = True
                        q.append((dy,dx))
        cnt += 1

    for i in range(N) :
        for j in range(M) :
            if graph[i][j] == 1 :
                if not visited[i][j] :
                    bfs(i,j)
    print(cnt)