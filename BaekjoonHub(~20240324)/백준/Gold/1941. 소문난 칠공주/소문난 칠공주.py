'''
< 문제 설계 >
1. 5*5 배열이므로 25개의 좌표중에 7개를 조합으로 뽑아냄.
2. 뽑아내는 과정에서 도연이가 4번이상 나오는 경우를 걸러냄. ( 다솜이가 4명ㅇ 이상 되어야하니깐 )
3. 그렇게 얻어낸 7개의 좌표를 BFS 함수를 통해서 모두 이어져있는지를 확인함.
4. 한 곳에 이어져있으면, 가능한 경우이므로 경우의 수 +1
'''

# 반 리스트 입력받기
arr = [ list(input()) for _ in range(5) ]

# 5*5 배열이니깐 25개의 인덱스 튜플 형태로 담아놓기
idx = []
for i in range(5) :
    for j in range(5) :
        idx.append((i,j))

# 25개 중 7개 뽑기 위한 visited 배열
visited = [False]*25

# 7공주 리스트
princess = []
# 25개 중 7개 뽑기.
def comb(level,start,path,doyeon) :
    # 7명이 뽑혔고, 도연이가 4명이하면 조건 만족하므로 7공주 리스트에 넣기
    if level == 7 and doyeon < 4 :
        path2 = path.copy()
        princess.append(path2)
        return
    # 만약 도연이가 4명 이상이 되면 바로 백트래킹
    if doyeon >= 4 :
        return

    # 25개 중에 7개 조합 뽑기
    for i in range(start,25):
        if not visited[i] :
            visited[i] = True
            # 도연인지 다솜인지 확인하기 위한 좌표값 뽑아내기
            y,x = idx[i][0],idx[i][1]
            # 만약 좌표값이 도연이면 도연이 +1
            if arr[y][x] == 'Y' :
                comb(level + 1, i, path + [idx[i]],doyeon+1)
            else :
                comb(level + 1, i, path + [idx[i]],doyeon)
            visited[i] = False
comb(0,0,[],0)

# 소문난 칠공주가 될 수 있는 경우의 수
princess_7 = 0

# 7명의 공주가 한 줄로 이어져있는지 확인하기 위해

from collections import deque
def bfs(case) :
    # 공주가 있는 좌표를 1로 채우기
    maps = [[0]*5 for _ in range(5)]
    for i in range(7) :
        y,x = case[i]
        maps[y][x] = 1
    visited = [[False]*5 for _ in range(5) ]
    q = deque()
    # 입력받은 7개의 좌표 중 첫번째 y,x 좌표를 큐에 담고,
    # 거기서부터 연결된 곳을 탐색하기. ( 연결된 곳을 찾을 때마다 cnt+1 )
    st_y,st_x = case[0][0],case[0][1]
    maps[st_y][st_x] = True
    visited[st_y][st_x] = True
    q.append((st_y,st_x))
    directy = [-1,0,0,1]
    directx = [0,-1,1,0]
    # 시작점으로부터 연결된 공주의 개수
    cnt = 1

    while q :
        y,x = q.popleft()
        # 4방향에 대해
        for i in range(4) :
            dy = directy[i] + y
            dx = directx[i] + x
            # 1) 범위를 벗어나지 않고, 2) 공주가 위치한 곳이고 3) 아직 방문하지 않았으면
            # 방문 체크하고 / 큐에 담고 / cnt += 1
            if 0<=dy<5 and 0<=dx<5 and maps[dy][dx] == 1:
                if not visited[dy][dx] :
                    visited[dy][dx] = True
                    q.append((dy,dx))
                    cnt += 1
    # cnt 가 7이라는 것은 7명이 서로 가로나 세로로 반드시 인접해 있다는 뜻이므로
    # 경우의 수를 1 증가시켜준다.
    if cnt == 7 :
        return 1
    else :
        return 0

# 25명 중 7명 뽑은 조합들을 다 bfs에 넣어서 서로 연결되어있는지 확인하기.
for i in range(len(princess)) :
    ans = bfs(princess[i])
    princess_7 += ans
print(princess_7)