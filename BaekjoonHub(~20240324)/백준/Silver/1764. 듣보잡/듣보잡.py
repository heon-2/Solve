N,M = map(int,input().split())
dict = {}
for i in range(N+M) :
    name = input()
    if name in dict :
        dict[name] += 1
    else :
        dict[name] = 1
arr = []
for i in dict :
    if dict[i] == 2:
        arr.append(i)

arr.sort()
print(len(arr))
for i in arr :
    print(i)