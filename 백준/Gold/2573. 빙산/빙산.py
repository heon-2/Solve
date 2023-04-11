from collections import deque
N,M = map(int,input().split())
graph = [ list(map(int,input().split())) for _ in range(N) ]
directy = [-1,0,0,1]
directx = [0,-1,1,0]
year = 0

while True :
    # 빙하 덩어리 개수
    ice = 0
    # 0 개수 세기
    zero_cnt = 0
    for i in range(1,N-1) :
        for j in range(1,M-1) :
            if graph[i][j] == 0 :
                zero_cnt += 1
    if zero_cnt == (N-2) * (M-2) :
        print(0)
        break


    visited = [[False] * M for _ in range(N)]
    # 얼마만큼 녹일지 그래프로 만들기
    minus = [ [0]*M for _ in range(N) ]
    for y in range(1,N-1) :
        for x in range(1,M-1) :
            cnt = 0
            for k in range(4) :
                dy = directy[k] + y
                dx = directx[k] + x
                if graph[dy][dx] == 0 :
                    cnt += 1
            minus[y][x] = cnt

    for i in range(N) :
        for j in range(M) :
            if graph[i][j] - minus[i][j] <= 0 :
                graph[i][j] = 0
            else :
                graph[i][j] = graph[i][j] - minus[i][j]

    def bfs(y,x) :
        global ice
        q = deque()
        if not visited[y][x]  :
            q.append((y,x))
        else :
            return

        if len(q) > 0 :
            while q :
                visited[y][x] = True
                v1,v2 = q.popleft()
                for i in range(4) :
                    dv1 = v1 + directy[i]
                    dv2 = v2 + directx[i]
                    if graph[dv1][dv2] > 0 and not visited[dv1][dv2] :
                        visited[dv1][dv2] = True
                        q.append((dv1,dv2))
            ice += 1
            # print(ice)
    for i in range(1,N-1) :
        for j in range(1,M-1) :
            if graph[i][j] > 0 :
                bfs(i,j)
    year += 1
    if ice >= 2:
        print(year)
        break
