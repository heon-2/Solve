# bfs,dfs 각각 visited 배열 만들어주기
N,M,V = map(int,input().split())
visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)
graph = [[] for _ in range(N+1)]

# 인접 리스트 만들기
for i in range(M) :
    A,B = map(int,input().split())
    graph[A].append(B)
    graph[B].append(A)

# 정점 번호가 작은 것부터 방문한다 했으므로, 인접 리스트를 오름차순으로 정렬
for i in range(len(graph)) :
    graph[i].sort()

# dfs 함수
def dfs(graph,v,visited) :
    visited[v] = True
    print(v,end=' ')
    for i in graph[v] :
        if not visited[i] :
            visited[i] = True
            dfs(graph,i,visited)
dfs(graph,V,visited_dfs)
print()

# bfs 함수
from collections import deque
def bfs(graph,start,visited) :
    visited[start] = True
    queue = deque()
    queue.append(start)
    while queue :
        v = queue.popleft()
        print(v,end=' ')
        for i in graph[v] :
            if not visited[i] :
                visited[i] = True
                queue.append(i)
bfs(graph,V,visited_bfs)