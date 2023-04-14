N,M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
path = []
def x(level,path) :
    if level == M :
        print(*path)
        return

    for i in range(len(lst)) :
        x(level+1,path+[lst[i]])

x(0,path)