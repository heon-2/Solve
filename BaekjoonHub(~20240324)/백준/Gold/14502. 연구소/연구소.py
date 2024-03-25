import copy
from collections import deque

N,M = map(int,input().split())
graph = [ list(map(int,input().split())) for _ in range(N) ]

# 빈칸 리스트 받기
lst = []
for i in range(N) :
    for j in range(M) :
        if graph[i][j] == 0 :
            lst.append((i,j))


# 빈칸 중에 3개 고르기 ( 조합 )
cases =[]
def comb(level,start,path) :
    if level == 3 :
        path2 = path[:]
        cases.append(path2)
        return

    for i in range(start,len(lst)) :
        comb(level+1,i+1,path+[lst[i]])

comb(0,0,[])

directy = [-1,0,0,1]
directx = [0,-1,1,0]
# bfs 로 탐색하기
# 그리고 바이러스가 있는 곳을 모두 찾아서 q에 담고 bfs 수행
def bfs(arr) :
    lab = copy.deepcopy(graph)
    visited = [[False]*M for _ in range(N) ]
    q = deque()
    # 입력받은 3개의 좌표에 벽을 세워
    for i in range(3) :
        y,x = arr[i][0],arr[i][1]
        lab[y][x] = 1
    for i in range(N) :
        for j in range(M) :
            if lab[i][j] == 2 :
                q.append((i,j))
                visited[i][j] = True

    while q :
        yy,xx = q.popleft()
        for i in range(4) :
            dy = yy+ directy[i]
            dx = xx + directx[i]
            if 0<=dy<N and 0<=dx<M and lab[dy][dx] == 0 :
                if not visited[dy][dx] :
                    visited[dy][dx] = True
                    lab[dy][dx] = 2
                    q.append((dy,dx))
    safe_area = 0
    for i in range(N) :
        for j in range(M) :
            if lab[i][j] == 0 :
                safe_area += 1
    return safe_area

maxx = -21e8
for i in cases :
    if bfs(i) >= maxx :
        maxx = bfs(i)

print(maxx)







