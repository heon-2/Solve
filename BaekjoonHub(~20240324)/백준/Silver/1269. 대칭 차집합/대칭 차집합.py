import sys
input = sys.stdin.readline

A,B = map(int,input().split())
lst_a = list(map(int,input().split()))
lst_b = list(map(int,input().split()))

x = dict()

for a in lst_a :
    if a in x :
        x[a] += 1
    else :
        x[a] = 1

for b in lst_b :
    if b in x :
        x[b] += 1
    else :
        x[b] = 1

cnt = 0
for i in x :
    if x[i] == 1 :
        cnt += 1
print(cnt)