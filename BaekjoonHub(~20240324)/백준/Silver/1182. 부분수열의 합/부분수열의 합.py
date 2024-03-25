N,summ = map(int,input().split())
lst = list(map(int,input().split()))
i = 0
cnt = 0
while i != N :
    i += 1
    visited = [False] * len(lst)
    def comb(level,start,path) :
        global cnt
        if level == i :
            if sum(path) == summ :
                cnt += 1
            return

        for s in range(start,len(lst)) :
            if not visited[s] :
                visited[s] = True
                comb(level+1,s,path+[lst[s]])
                visited[s] = False
    comb(0,0,[])

print(cnt)