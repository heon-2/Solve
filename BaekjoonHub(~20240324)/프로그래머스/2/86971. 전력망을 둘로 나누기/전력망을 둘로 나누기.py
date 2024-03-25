import sys
sys.setrecursionlimit(10**6)
def solution(n, wires):
    global cnt,visited,graph
    answer = 21e8
    for i in range(n) :
        # 인접 그래프 생성
        graph = [[] for _ in range(n+1)]            
        for wire in wires :
            # 끊어낸 곳 제외하고 인접그래프
            if wires.index(wire) != i :
                graph[wire[0]].append(wire[1])
                graph[wire[1]].append(wire[0])
        visited = [False]*(n+1)
        # 어차피 원래 모두 연결되어 있기 때문에 1개 전선 끊으면 2개로 밖에 분리안 됨.
        group1,group2 = 0,0
        for j in range(n) :
            cnt = 0
            if not visited[j] :
                dfs(j)
                if group1 == 0 :
                    group1 = cnt
                else :
                    group2 = cnt
                    break
        abss = abs(group1-group2)
        answer = min(abss,answer)
        
    return answer


def dfs(x) :
    global cnt,visited,graph
    visited[x] = True
    for i in graph[x] :
        if not visited[i] :
            cnt += 1
            dfs(i)
