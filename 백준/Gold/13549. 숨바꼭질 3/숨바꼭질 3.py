DAT = [0] * 100001
visited = [False]*100001
st,ed = map(int,input().split())
from collections import deque
def bfs(x) :
    q = deque()
    q.append(x)
    DAT[x] = 1
    visited[x] = True
    while q:
        v = q.popleft()
        move = [v, 1, -1]

        for i in range(3) :
            dx = v + move[i]
            if 0<=dx<100001 and DAT[dx] == 0 :
                if not visited[dx] :
                    visited[dx] = True
                    if i != 0 :
                        DAT[dx] = DAT[v]+1
                        q.append(dx)
                    else :
                        DAT[dx] = DAT[v]
                        q.appendleft(dx)


    return DAT[ed]-1
minn = bfs(st)
print(minn)
# print(DAT)

# 이 문제를 풀다가 생긴 문제점.
# move ( direct 방향 배열을 설정할 때, 2배 순간이동 할 떄 초기값을 2배로 해버림... 이거 착각해서 오래 걸렸다. )
# 그리고 순간이동의 경우 우선순위를 제일 높여야하기 떄문에, 큐에 append하는게 아니라, appendleft를 하는 게 맞다!

