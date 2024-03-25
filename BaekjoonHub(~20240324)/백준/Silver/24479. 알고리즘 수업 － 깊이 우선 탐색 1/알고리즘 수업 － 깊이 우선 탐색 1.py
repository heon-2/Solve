import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N,M,start = map(int,input().split())
graph = [[] for _ in range(N+1)]
for i in range(M) :
    # 양방향 간선
    st,ed = map(int,input().split())
    graph[st].append(ed)
    graph[ed].append(st)
for i in graph :
    i.sort()
# 방문 순서 기록용 DAT
DAT = [0] * (N+1)
visited = [False] * (N+1)
# 트리순회랑 같지 않을까
order=1
def dfs(x) :
    global order
    DAT[x] = order
    for i in graph[x] :
        if not visited[i] :
            visited[i] = True
            order += 1
            dfs(i)
    return
visited[start] = True
dfs(start)

for i in DAT[1:] :
    print(i)