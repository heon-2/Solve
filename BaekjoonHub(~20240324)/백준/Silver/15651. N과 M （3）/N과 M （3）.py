N,M = map(int,input().split())
lst = [i for i in range(1,N+1) ]
path =[]
def perm(level) :
    if level == M :
        print(*path)
        return

    for i in range(len(lst)) :
        path.append(lst[i])
        perm(level+1)
        path.pop()

perm(0)


