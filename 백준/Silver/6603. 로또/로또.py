while True :
    k,*lst = map(int,input().split())
    if k == 0 :
        break
    visited = [False] * k
    path =[]
    def comb(level,start,path) :
        if level == 6 :
            print(*path)
            return

        for i in range(start,k) :
            if not visited[i] :
                visited[i] = True
                comb(level+1,i,path+[lst[i]])
                visited[i] = False

    comb(0,0,path)
    print()