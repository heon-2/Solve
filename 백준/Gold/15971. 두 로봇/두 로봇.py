import sys
input = sys.stdin.readline
from collections import deque

n,st,ed = map(int,input().split())
graph = [ [] for _ in range(n+1) ]
for _ in range(n-1) :
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def bfs() :
    q = deque()
    visited = [0] * (n+1)
    q.append((st,0,0))
    visited[st] = 1
    
    while q :
        path,total,maxx = q.popleft()
        if path == ed :
            ans = total-maxx
            return ans
        else :
            for next_path,dist in graph[path] :
                if not visited[next_path] :
                    visited[next_path] = 1
                    q.append((next_path,total+dist,max(maxx,dist)))

print(bfs())