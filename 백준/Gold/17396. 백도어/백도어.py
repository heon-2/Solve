import sys,heapq
input = sys.stdin.readline

V,E = map(int,input().split())
ward = list(map(int,input().split()))
ward[-1] = 0
graph = [[] for _ in range(V)]
INF = 10**11
for i in range(E) :
    u,v,w = map(int,input().split())
    if ward[u] == 0 and ward[v] == 0 :
        graph[u].append((v,w))
        graph[v].append((u,w))

def dijkstra(start) :
    distance = [INF] * (V)
    distance[start] = 0
    q = []
    heapq.heappush(q,(0,start))

    while q :
        dist,now = heapq.heappop(q)
        if dist > distance[now]  :
            continue
        for i in graph[now] :
            if dist + i[1] < distance[i[0]] :
                distance[i[0]] = dist + i[1]
                heapq.heappush(q,(dist+i[1],i[0]))


    return distance[-1]

ans = dijkstra(0)
if ans == INF :
    print(-1)
else :
    print(ans)





