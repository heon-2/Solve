import sys,heapq
input = sys.stdin.readline
V,E = map(int,input().split())
graph = [[] for _ in range(V+1)]
INF = 1e9

for i in range(E) :
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(start,end) :
    distance = [INF] * (V + 1)
    distance[start]=0
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
    return distance[end]

v1,v2 = map(int,input().split())

cal1 = 0
cal2 = 0

cal1 += dijkstra(1,v1)
cal1 += dijkstra(v1,v2)
cal1 += dijkstra(v2,V)

cal2 += dijkstra(1,v2)
cal2 += dijkstra(v2,v1)
cal2 += dijkstra(v1,V)

ans = min(cal1,cal2)
if ans >= INF :
    print(-1)
else :
    print(ans)
