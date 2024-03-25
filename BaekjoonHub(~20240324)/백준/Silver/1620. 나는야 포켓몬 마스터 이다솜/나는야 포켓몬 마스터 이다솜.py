import sys
input = sys.stdin.readline
N,M = map(int,input().split())
animal = dict()
lst = []
for i in range(N) :
    a = input().rstrip()
    animal[a] = i+1
    lst.append(a)
i = list(input().rstrip() for _ in range(M))

for x in i :
    if x[0].isupper() or x[-1].isupper() :
        print(animal[x])
    else :
        print(lst[int(x)-1])
