import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N,M,R = map(int,input().split())
visited = [0]*(N+1)
graph = [[] for _ in range(N+1) ]
for i in range(M) :
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in graph :
    i.sort(reverse=True)
c=1
def dfs(x) :
    global c

    for i in graph[x] :
        if not visited[i] :
            c += 1
            visited[i] = c
            dfs(i)
    return
visited[R] = c
dfs(R)

for i in visited[1:] :
    print(i)