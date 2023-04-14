N,M = map(int,input().split())
lst = [_ for _ in range(1,N+1)]
path = []
visited = [False] * len(lst)
def perm(level,lst) :
    if level == M :
        print(*path)
        return

    for i in range(len(lst)) :
        if not visited[i] :
            visited[i] = True
            path.append(lst[i])
            perm(level+1,lst)
            path.pop()
            visited[i] = False

perm(0,lst)



