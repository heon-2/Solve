import sys
input = sys.stdin.readline
M = int(input())

summ = 0
xor = 0
for i in range(M) :
    lst = list(map(int,input().split()))

    if lst[0] == 1 :
        summ += lst[1]
        xor ^= lst[1]
    elif lst[0] == 2 :
        summ -= lst[1]
        xor ^= lst[1]
    elif lst[0] == 3 :
        print(summ)
    elif lst[0] == 4 :
        print(xor)



