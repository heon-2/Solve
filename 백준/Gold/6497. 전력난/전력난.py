import sys
input = sys.stdin.readline

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

while True :
    edges = []
    V,E = map(int,input().split())
    if V ==0 and E == 0 :
        break
    parent = [ _ for _ in range(V+1) ]
    minimum_cost = 0
    original_cost = 0
    for i in range(E) :
        a,b,w = map(int,input().split())
        edges.append((w,a,b))
        original_cost += w
    edges.sort()
    for i in range(E) :
        w,a,b = edges[i]
        if find_parent(parent,a) != find_parent(parent,b) :
            union_parent(parent,a,b)
            minimum_cost += w
    print(original_cost-minimum_cost)