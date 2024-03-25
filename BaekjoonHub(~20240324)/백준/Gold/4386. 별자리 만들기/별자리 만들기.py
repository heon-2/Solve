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

n= int(input())
parent = [ _ for _ in range(n) ]
stars = {}
for i in range(n) :
    x,y = map(float,input().split())
    stars[i] =(x,y)

# 별들 하나하나에 인덱스 부여하고 거리 담기
edges = []
for i in range(n) :
    for j in range(i+1,n) :
        star1 = stars[i]
        star2 = stars[j]
        dist_x = (star1[0]-star2[0])**2
        dist_y = (star1[1]-star2[1])**2
        dist = (dist_x + dist_y) ** 0.5
        edges.append((dist,i,j))
# 별들 거리순으로 오름차순 정렬
edges.sort()
total_cost = 0
for i in edges :
    dist,a,b = i
    if find_parent(parent,a) != find_parent(parent,b) :
        union_parent(parent,a,b)
        total_cost += dist

print(total_cost)




