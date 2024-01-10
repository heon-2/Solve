import sys
sys.setrecursionlimit(10**6)
def solution(n, wires):
    global cnt,visited,graph
    answer = 21e8
        # 인접 그래프 생성
        

    for i in range(n) :
        graph = [[] for _ in range(n+1)]            
        for wire in wires :
            if wires.index(wire) != i :
                graph[wire[0]].append(wire[1])
                graph[wire[1]].append(wire[0])
        visited = [False]*(n+1)
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
