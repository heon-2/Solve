import heapq
import sys
input = sys.stdin.readline

V,E = map(int,input().split())
INF = 1e9
distance = [INF]*(V+1)
graph = [[] for _ in range(V+1)]
start = int(input())

for i in range(E) :
    u,v,w = map(int,input().split())
    graph[u].append((v,w))

def dijkstra(start) :
    distance[start] = 0
    q = []
    heapq.heappush(q,(0,start))

    while q :
        dist,now = heapq.heappop(q)
        if distance[now] < dist :
            continue
        for i in graph[now] :
            if dist+i[1] < distance[i[0]] :
                distance[i[0]] = dist + i[1]
                heapq.heappush(q,((dist+i[1],i[0])))
dijkstra(start)

for i in distance[1:] :
    if i == INF :
        print('INF')
    else :
        print(i)
