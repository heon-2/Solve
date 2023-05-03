import sys
input = sys.stdin.readline
n = int(input())
current = set()
for i in range(n) :
    name,go = map(str,input().split())
    if go == 'enter' :
        current.add(name)
    elif go == 'leave' :
        current.discard(name)

current = list(current)
current.sort(reverse=True)

for i in current :
    print(i)