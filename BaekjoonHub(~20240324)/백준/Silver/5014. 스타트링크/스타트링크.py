from collections import deque

# 총 층수 / 시작점 / 끝점 / UP / DOWN
total,st,ed,U,D = map(int,input().split())

# visited 배열 만들기.

def bfs(x) :
    visited = [0] * (total + 2)
    q = deque()
    q.append(x)
    visited[x] = 1

    # 업 / 다운
    move = [U,-D]
    while q :
        v = q.popleft()
        for i in range(2) :
            dv = v+move[i]
            if 1<= dv < total+1 and visited[dv] == 0 :
                visited[dv] = visited[v] + 1
                q.append(dv)

    if visited[ed] :
        return visited[ed]-1
    else :
        return 'use the stairs'


print(bfs(st))


