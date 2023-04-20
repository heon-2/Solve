n = int(input())
cnt = 0
cnt2 = 0
for i in range(1,n+1) :
    for j in range(1,n+1) :
        if i*j <= n and i == j :
            cnt += 1
        elif i*j <=n and i != j :
            cnt2 += 1

print(cnt+cnt2//2)

