# 그래프 만들기
R,C = map(int,input().split())
graph = [ list(input()) for _ in range(R) ]

# 4방향 델타
directy = [-1,0,0,1]
directx = [0,-1,1,0]

# 최대 이동 거리와 이동 거리 변수 설정
max_move = -21e8
cnt = 1

# DAT 배열 사용 ( A~Z 까지 26개 )
# 여기서 DAT는 Visited 배열 역할을 함.
DAT = [0] * 26
v = ord(graph[0][0])-ord('A')

# 출발지점 1 체크하기
DAT[v] = 1

# DFS로 탐색.
def dfs(y,x) :
    global max_move,cnt

    # 4방향에 각각 범위 벗어나지 않고, 방문하지 않았다면 방문체크하고 이동거리도 +1 해주기.
    # 그리고 다음 위치 탐색.
    # 모든 경로를 탐색해야 하므로 탐색 후에는 방문했던 곳 0으로 바꾸고 이동거리도 -1 해주기.
    for i in range(4) :
        dy = y + directy[i]
        dx = x + directx[i]
        if 0<=dy<R and 0<=dx<C :
            dv = ord(graph[dy][dx])-ord('A')
            if DAT[dv] == 0 :
                DAT[dv] = 1
                cnt += 1
                dfs(dy,dx)
                DAT[dv] = 0
                cnt -= 1
    # 이동거리가 최대 이동거리보다 크다면 최댓값 갱신
    if cnt >= max_move :
        max_move = cnt
    return

dfs(0,0)
print(max_move)