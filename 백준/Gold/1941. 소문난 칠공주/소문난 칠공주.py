arr = [ list(input()) for _ in range(5) ]

lst = []
for i in range(5) :
    for j in range(5) :
        lst.append((i,j))

visited = [False]*25

v = []
def comb(level,start,path,doyeon) :

    if level == 7 and doyeon < 4 :
        path2 = path.copy()
        v.append(path2)
        return
    if doyeon >= 4 :
        return

    for i in range(start,25):
        if not visited[i] :
            visited[i] = True
            x,y = lst[i][0],lst[i][1]
            if arr[x][y] == 'Y' :
                comb(level + 1, i, path + [lst[i]],doyeon+1)
            else :
                comb(level + 1, i, path + [lst[i]],doyeon)
            visited[i] = False

comb(0,0,[],0)

# 전체 경우의 수
answer = 0

from collections import deque

def bfs(dddd) :

    maps = [[0]*5 for _ in range(5)]
    for i in range(7) :
        y,x = dddd[i]
        maps[y][x] = 1
    visited = [[False]*5 for _ in range(5) ]
    q = deque()
    # print(dddd[0][0],dddd[0][1])
    maps[dddd[0][0]][dddd[0][1]] = True
    q.append((dddd[0][0],dddd[0][1]))
    directy = [-1,0,0,1]
    directx = [0,-1,1,0]
    cnt = 0
    while q :
        y,x = q.popleft()
        for i in range(4) :
            dy = directy[i] + y
            dx = directx[i] + x
            if 0<=dy<5 and 0<=dx<5 and maps[dy][dx] == 1:
                if not visited[dy][dx] :
                    visited[dy][dx] = True
                    q.append((dy,dx))
                    cnt += 1
    if cnt == 7 :
        return 1
    else :
        return 0

# 모든 경우의 수 넣기
for i in range(len(v)) :
    # print(v[i])
    a = bfs(v[i])
    answer += a

print(answer)