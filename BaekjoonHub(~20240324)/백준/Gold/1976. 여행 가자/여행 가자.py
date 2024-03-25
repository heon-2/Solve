import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [ list(map(int,input().split())) for _ in range(N) ]

def find_parent(parent,x) :
    if parent[x] != x :
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b) :
    root_a = find_parent(parent,a)
    root_b = find_parent(parent,b)

    if root_a < root_b :
        parent[root_b] = root_a
    else :
        parent[root_a] = root_b

parent = [0]*(N+1)
for i in range(1,N+1) :
    parent[i] = i
for i in range(N) :
    for j in range(N) :
        if graph[i][j] == 1 :
            union_parent(parent,i+1,j+1)
travel_plan = list(map(int,input().split()))
flag = False
rlt = find_parent(parent,travel_plan[0])
for i in range(1,len(travel_plan)) :
    if find_parent(parent,travel_plan[i]) != rlt :
        flag = True
        break
if not flag :
    print('YES')
else :
    print('NO')
