import heapq,sys
input = sys.stdin.readline

N,M,X = map(int,input().split())
graph = [[] for _ in range(N+1)]
INF = 1e9

for i in range(M) :
    u,v,w = map(int,input().split())
    graph[u].append((v,w))

def dijkstra(start,end) :
    distance = [INF] * (N + 1)
    distance[start] = 0
    q = []
    heapq.heappush(q,(0,start))

    while q :
        dist,now = heapq.heappop(q)
        if distance[now] < dist :
            continue
        for i in graph[now] :
            if distance[i[0]] > dist + i[1] :
                distance[i[0]] = dist + i[1]
                heapq.heappush(q,(dist+i[1],i[0]))
    maxx = -21e8
    for i in distance :
        if i != INF and i > maxx :
            maxx = i
    return distance[end]

# 왕복 소요시간 적는 곳
time = [0] * (N+1)

for i in range(1,N+1) :
    # 시작 -> X
    go = dijkstra(i,X)
    time[i] += go
    # X -> 도착
    back = dijkstra(X, i)
    time[i] += back

print(max(time))

