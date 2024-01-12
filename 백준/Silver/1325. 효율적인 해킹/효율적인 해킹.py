import sys
input = sys.stdin.readline
from collections import deque
n,m = map(int,input().split())
visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]
for i in range(m) :
    a,b = map(int,input().split())
    graph[b].append(a)

def bfs(now):
    q = deque()
    q.append(now)
    visited[now] = 1
    cnt = 1
    while q:
        now = q.popleft()
        for i in graph[now]:
            if visited[i] == 0:
                visited[i] = 1
                cnt += 1
                q.append(i)
    return cnt

answer = []
DAT = [0]*(n+1)
for i in range(1,n+1):
    visited = [0]*(n+1)
    cnt = bfs(i)
    DAT[i] = cnt
for i in range(1,n+1):
    if DAT[i] == max(DAT):
        answer.append(i)
answer.sort()
print(*answer)