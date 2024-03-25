# 이젠 하다하다 실버3도 어렵네..
N = int(input())
dist = list(map(int,input().split()))
price = list(map(int,input().split()))

minn = price[0]
total_price = 0

for i in range(N-1) :
    if minn > price[i] :
        minn = price[i]

    total_price += minn*dist[i]

print(total_price)