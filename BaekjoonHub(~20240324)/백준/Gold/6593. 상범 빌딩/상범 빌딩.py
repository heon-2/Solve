
import sys
from collections import deque
input = sys.stdin.readline
dx = [0, 0, 1, -1, 0, 0]
dy = [0, 0, 0, 0, 1, -1]
dz = [1, -1, 0, 0, 0, 0]

while True:
    L,R,C = map(int, input().split())
    # if L == 0 and R == 0 and C == 0:
    # all 파이썬 내장함수 한번 써봤음. all은 iterable 한 모든 객체를 인자로 받을 수 있음.
    if not all((L,R,C)) :
        break
    graph = []
    visited = [[[False] * C for _ in range(R)] for _ in range(L)]
    for _ in range(L):
        graph.append([list(input().rstrip()) for _ in range(R)])
        temp = input()

    q = deque()
    flag = False

    for i in range(L):
        for j in range(R):
            for k in range(C):
                if graph[i][j][k] == 'S':
                    start = (i, j, k, 0)
                    visited[i][j][k] = True
                if graph[i][j][k] == 'E':
                    end = (i, j, k)

    q.append(start)
    while q:
        z, x, y, d = q.popleft()
        if (z, x, y) == end:
            flag = True
            print(f'Escaped in {d} minute(s).')
            break
        dd = d + 1

        for i in range(6):
            zz = z + dz[i]
            xx = x + dx[i]
            yy = y + dy[i]

            if 0 <= zz < L and 0 <= xx < R and 0 <= yy < C and not visited[zz][xx][yy]:
                if graph[zz][xx][yy] == '.' or graph[zz][xx][yy] == 'E':
                    q.append((zz,xx,yy,dd))
                    visited[zz][xx][yy] = True

    if not flag:
        print('Trapped!')