import sys
input = sys.stdin.readline
N,M = map(int,input().split())

S = set(list(input() for _ in range(N)))
check = [ input() for _ in range(M) ]

cnt = 0
for i in check :
    if i in S :
        cnt += 1

print(cnt)