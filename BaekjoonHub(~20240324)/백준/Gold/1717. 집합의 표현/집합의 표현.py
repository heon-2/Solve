import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find_parent(parent,x) :
    if parent[x] != x :
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b) :
    aa = find_parent(parent,a)
    bb = find_parent(parent,b)

    if aa < bb :
        parent[bb] = aa
    else :
        parent[aa] = bb

n,m = map(int,input().split())
parent = [0] * (n+1)
for i in range(n+1) :
    parent[i] = i

for i in range(m) :
    cal,a,b = map(int,input().split())
    if cal == 0 :
        union_parent(parent,a,b)
    elif cal == 1 :
        if find_parent(parent,a) == find_parent(parent,b) :
            print('YES')
        else :
            print('NO')
