N,M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
path =[]
visited = [False] * len(lst)

def x(level) :
    if level == M :
        print(*path)
        return

    for i in range(len(lst)) :
        if not visited[i] :
            visited[i] = True
            path.append(lst[i])
            x(level+1)
            visited[i] = False
            path.pop()
x(0)

