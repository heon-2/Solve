import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

v = int(input())
graph = [[] for _ in range(v+1)]
visited = [False] * (v+1)
for _ in range(v-1) :
    x,y,w = map(int,input().split())
    graph[x].append([y,w])
    graph[y].append([x,w])
max_dist = 0
node = 0
def dfs(st,dist,visited) :
    global max_dist,node
    if dist > max_dist :
        max_dist = dist
        node = st
    visited[st] = True
    for i in graph[st] :
        if not visited[i[0]] :
            dfs(i[0],dist+i[1],visited)
dfs(1,0,visited)
# 초기화 한 후에 다시 
visited = [False]*(v+1)
max_dist = 0
dfs(node,0,visited)
print(max_dist)
