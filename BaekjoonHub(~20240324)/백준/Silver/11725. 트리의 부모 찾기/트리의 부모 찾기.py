import sys
input = sys.stdin.readline
from collections import deque
N = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
DAT = [0] *(N+1)

for i in range(N-1) :
    st,ed = map(int,input().split())
    graph[st].append(ed)
    graph[ed].append(st)

def bfs(x) :
    q =deque()
    q.append(x)
    visited[x] = True
    while q:
        v = q.popleft()
        for i in graph[v] :
            if not visited[i] :
                visited[i] = True
                DAT[i] = v
                q.append(i)
bfs(1)

for i in DAT[2:] :
    print(i)