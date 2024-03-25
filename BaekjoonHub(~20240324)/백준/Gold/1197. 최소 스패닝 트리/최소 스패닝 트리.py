import sys
input = sys.stdin.readline

def find_parent(parent,x) :
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b) :
    root_a = find_parent(parent,a)
    root_b = find_parent(parent,b)

    if root_a < root_b :
        parent[root_b] = root_a
    else :
        parent[root_a]= root_b

edges = []
V,E = map(int,input().split())
parent = [ _ for _ in range(V+1)]
total_cost = 0
for i in range(E) :
    a,b,w = map(int,input().split())
    edges.append((w,a,b))
edges.sort()

for i in range(E) :
    w,a,b = edges[i]
    if find_parent(parent,a) != find_parent(parent,b) :
        union_parent(parent,a,b)
        total_cost += w
print(total_cost)