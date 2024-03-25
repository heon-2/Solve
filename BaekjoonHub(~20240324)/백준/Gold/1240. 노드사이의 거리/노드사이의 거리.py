import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
v,e = map(int,input().split())
graph = [[] for _ in range(v+1)]
visited = [False for _ in range(v+1)]

def dfs(st,ed,dist) :
    if st == ed :
        print(dist)
        return
    for i in graph[st] :
        if not visited[i[0]] :
            visited[i[0]] = True
            dfs(i[0],ed,dist+i[1])
            visited[i[0]] = False


# 인접그래프 만들 때, [노드번호,거리]
for i in range(v-1) :
    a,b,dist = map(int,input().split())
    graph[a].append([b,dist])
    graph[b].append([a,dist])

for i in range(e) :
    node1,node2 = map(int,input().split())
    visited[node1] = True
    dfs(node1,node2,0)
    visited[node1] = False
