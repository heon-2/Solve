DAT = [0] * 100001

st,ed = map(int,input().split())
from collections import deque
def bfs(x) :
    q = deque()
    q.append(x)
    DAT[x] = 1
    while q:
        v = q.popleft()
        if v == ed :
            return DAT[ed] -1
        move = [v, -1,1]
        # move = [v, 1, -1]
        for i in range(3) :
            dx = v + move[i]
            if 0<=dx<100001 and DAT[dx] == 0 :
                    if i != 0 :
                        DAT[dx] = DAT[v]+1
                        q.append(dx)
                    else :
                        DAT[dx] = DAT[v]
                        q.appendleft(dx)
minn = bfs(st)
print(minn)