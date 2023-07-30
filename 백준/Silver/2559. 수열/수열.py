N,K = map(int,input().split())
lst = list(map(int,input().split()))

res = sum(lst[:K])
ans = res
for i in range(N-K) :
    res += lst[i+K] - lst[i]
    ans = max(ans,res)

print(ans)