import heapq,sys
input = sys.stdin.readline

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
INF = 1e9
distance = [INF]*(N+1)

for i in range(M) :
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

def dijkstra(start) :
    distance[start] = 0
    q = []
    heapq.heappush(q,(0,start))

    while q :
        dist,now = heapq.heappop(q)
        if dist > distance[now] :
            continue
        for i in graph[now] :
            if dist+i[1] < distance[i[0]] :
                distance[i[0]] = dist+i[1]
                heapq.heappush(q,(dist+i[1],i[0]))
dijkstra(1)
print(distance[N])