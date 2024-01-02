import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
k = int(input())

def dfs(x,color) :
    global answer
    if not answer :
        return
    visited[x] = color
    for i in graph[x] :
        if visited[i] == 0 :
            dfs(i,-color)
        elif visited[x] == visited[i] :
            answer = False
            return


for _ in range(k) :
    answer = True
    v,e = map(int,input().split())
    visited = [0]*(v+1)
    graph = [[] for _ in range(v+1)]
    for i in range(e) :
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    for i in range(1,v+1) :
        if visited[i] == 0 :
            dfs(i,1)
            if not answer :
                break
    if answer :
        print('YES')
    else :
        print('NO')

