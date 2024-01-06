import sys
sys.setrecursionlimit(10**6)
n = int(input())
graph = [[] for _ in range(n)]
nodes = list(map(int,input().split()))
leaf,root = 0,0
for i in range(n) :
    if nodes[i] == -1 :
        root = i
    else :
        # 부모 인접 그래프에 자식 추가
        graph[nodes[i]].append(i)
delete = int(input())
visited = [False]*n
# 삭제할 노드들
del_nodes = set()
# 삭제할 노드부터 DFS로 탐색하며 삭제할 노드 찾기
def dfs(x) :
    visited[x] = True
    del_nodes.add(x)
    for i in graph[x] :
        if not visited[i] :
            dfs(i)
dfs(delete)
# 삭제할 노드들 트리에서 지우기
for i in range(n) :
    for j in graph[i] :
        if j in del_nodes :
            graph[i].remove(j)

# 삭제할 노드가 아니고, 인접 그래프가 빈배열(=[]) 인 경우에 leaf += 1
for i in range(n) :
    if i not in del_nodes :
        if graph[i] == [] :
            leaf += 1
print(leaf)