T = int(input())
for tc in range(T) :
    n = int(input())
    dict = {}
    for i in range(n) :
        price,name = map(str,input().split())
        price = int(price)
        dict[name] = price
    sort1 = sorted(dict,key=lambda x:dict[x])
    print(sort1[-1])