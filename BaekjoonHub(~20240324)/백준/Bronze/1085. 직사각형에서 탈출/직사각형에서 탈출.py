x,y,w,h = map(int,input().split())

dy = [0,h]
dx = [0,w]
lst = []
for i in dy :
    lst.append(abs(y-i))

for j in dx :
    lst.append(abs(x-j))

print(min(lst))