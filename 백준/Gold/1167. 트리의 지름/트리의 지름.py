import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
V = int(input())
graph = [[] for _ in range(V+1)]
visited = [False]*(V+1)
for _ in range(V) :
    a = list(map(int,input().split()))
    for i in range(1,len(a)-1,2) :
        graph[a[0]].append([a[i],a[i+1]])

maxx = -1
node = 0
def dfs(x,dist) :
    global maxx,node
    if dist > maxx :
        maxx = dist
        node = x
    visited[x] = True
    for i in graph[x] :
        if not visited[i[0]] :
            dfs(i[0],dist+i[1])
# print(graph[1][0][0])

# 아무 노드에서나 시작
dfs(1,0)
# print(node)
# print(maxx)
a = node
node,maxx = 0,0
visited = [False]*(V+1)

dfs(a,0)
print(maxx)