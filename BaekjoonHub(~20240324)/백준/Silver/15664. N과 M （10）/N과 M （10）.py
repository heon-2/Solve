N,M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
visited = [False] * len(lst)
path = []
answers = []

def x(level,path,start) :
    if level == M :
        if path not in answers :
            print(*path)
            answers.append(path)
        return

    for i in range(start,len(lst)) :
        if not visited[i] :
            visited[i] = True
            x(level+1, path+[lst[i]],i)
            visited[i] = False

x(0,path,0)