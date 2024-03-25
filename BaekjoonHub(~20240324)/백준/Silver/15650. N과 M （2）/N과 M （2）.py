N,M = map(int,input().split())

lst = [_ for _ in range(1,N+1) ]
visited = [False] * N
path =[]
def comb(level,start,lst) :
    if level == M :
        print(*path)
        return

    for i in range(start,len(lst)) :
        if not visited[i] :
            visited[i] = True
            path.append(lst[i])
            comb(level+1,i,lst)
            path.pop()
            visited[i] = False

comb(0,0,lst)