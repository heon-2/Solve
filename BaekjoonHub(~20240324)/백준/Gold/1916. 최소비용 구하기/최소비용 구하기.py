import heapq
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
INF = 1e9
distance = [INF]*(N+1)

for i in range(M) :
    st,ed,w = map(int,input().split())
    graph[st].append((ed,w))

def dijkstra(start) :
    distance[start]=0
    q = []
    heapq.heappush(q,(0,start))

    while q :
        dist,now = heapq.heappop(q)
        if distance[now] < dist :
            continue
        for i in graph[now] :
            if distance[i[0]] > dist+i[1] :
                distance[i[0]] = dist+i[1]
                heapq.heappush(q,(dist+i[1],i[0]))

start,end = map(int,input().split())
dijkstra(start)
print(distance[end])