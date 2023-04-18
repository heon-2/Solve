import sys
sys.setrecursionlimit(100000)

N,M = map(int,input().split())
graph = [ [] for _ in range(N+1) ]
for i in range(M) :
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N+1)
dfs_lst = []
def dfs(graph,v,visited) :
    visited[v] = True
    dfs_lst.append(v)
    for i in graph[v] :
        if not visited[i] :
            visited[i] = True
            dfs(graph,i,visited)
connect =[]
for i in range(1,N+1) :
    dfs(graph,i,visited)
    dfs_lst.sort()
    if dfs_lst not in connect :
        connect.append(dfs_lst)
    dfs_lst = []
    visited = [False] * (N+1)

print(len(connect))