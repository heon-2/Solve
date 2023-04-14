N,M = map(int,input().split())
path =[]
lst = [ _ for _ in range(1,N+1) ]

def comb(level,start) :
    if level == M :
        print(*path)
        return

    for i in range(start,len(lst)) :
        path.append(lst[i])
        comb(level+1,i)
        path.pop()
comb(0,0)