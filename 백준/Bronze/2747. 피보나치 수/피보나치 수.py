lst = [0,1]
n = int(input())
for i in range(2,n+1) :
    next = lst[i-2]+lst[i-1]
    lst.append(next)
print(lst[-1])