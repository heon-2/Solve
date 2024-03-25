N = int(input())
lst = list(map(int,input().split()))

lst.sort()
v = []
for i in range(N) :
    v.append(sum(lst[0:i+1]))

print(sum(v))