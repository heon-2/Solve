import sys
input = sys.stdin.readline
N,won = map(int,input().split())
coins = []
for i in range(N) :
    coins.append(int(input()))

coins.sort(reverse=True)
cnt = 0
for coin in coins :
    if won // coin > 0 :
        cnt += (won//coin)
        won -= coin*(won//coin)

    if won == 0 :
        print(cnt)
        break