# DAT 사용해서 문제 풀기
from collections import deque
DAT = [0] * 100001

# 시작점, 끝점 입력받기
st,ed = map(int,input().split())

# BFS 함수 정의
def bfs(x) :
    global st,ed
    # 시작점에 1 체크해주기 ( 이렇게 안하면 시작지점으로 다시 돌아오는 경우가 있음 )
    DAT[x] = 1
    q = deque()
    q.append(x)

    while q :
        v = q.popleft()
        # -1 or +1 or *2 의 거리로 이동
        for i in range(3) :
            if i == 0 :
                # -1 로 이동
                dv = v-1
            elif i == 1 :
                # +1로 이동
                dv = v+1
            elif i == 2 :
                # *2로 순간이동
                dv = v*2

            # 범위 안에 있고 방문하지 않았던 곳이라면 이전에 적혀있던 값 +1  ( = 1번 이동한 셈이니깐 1초 증가 )
            if 0<=dv<=100000 and DAT[dv] == 0 :
                DAT[dv] = DAT[v]+1
                q.append(dv)
    # 도착지점에 적혀있는 값이 최소 이동 시간
    return DAT[ed]

# 시작할 때 1초 증가하고 시작했으니깐 결과 출력할 때는 -1 해주기
print(bfs(st)-1)