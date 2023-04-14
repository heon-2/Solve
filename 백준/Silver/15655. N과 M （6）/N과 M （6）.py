N,M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
path =[]
visited = [False] * N
def x(level,start) :
    if level == M :
        print(*path)
        return

    for i in range(start,len(lst)) :
        if not visited[i] :
            visited[i] = True
            path.append(lst[i])
            x(level+1,i)
            visited[i] = False
            path.pop()
x(0,0)