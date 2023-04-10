N = int(input())
lst = []
for i in range(N) :
    st,ed = map(int,input().split())
    lst.append((st,ed))
lst.sort()
lst.sort(key=lambda x:x[1])

cnt = 0
end = 0
for i in range(len(lst)) :
    if lst[i][0] >= end :
        cnt += 1
        end = lst[i][1]
print(cnt)