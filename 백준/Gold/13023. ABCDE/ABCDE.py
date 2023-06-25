import sys
input = sys.stdin.readline
N,M = map(int,input().split())

lst = [ [] for _ in range(N+1) ]
visited = [False] * (N+1)
for _ in range(M) :
    a,b = map(int,input().split())
    lst[a].append(b)
    lst[b].append(a)
# print(lst)
flag = 0
def dfs(level,x) :
    global flag
    if level == 5 :
        flag = 1
        return
    for i in lst[x] :
        if not visited[i] :
            visited[i] = True
            dfs(level+1,i)
            visited[i] = False

for i in range(N) :
    visited[i] = True
    dfs(1,i)
    visited[i] = False
    if flag :
        break

print(flag)