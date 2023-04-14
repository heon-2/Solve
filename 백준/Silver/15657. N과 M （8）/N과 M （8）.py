N,M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
path =[]
def x(level,start,path) :
    if level == M :
        print(*path)
        return

    for i in range(start,len(lst)) :
        x(level+1,i,path+[lst[i]])

x(0,0,path)