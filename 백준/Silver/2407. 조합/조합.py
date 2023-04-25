n,m = map(int,input().split())
gop = 1
for i in range(n,(n-m),-1) :
    gop*=i

gop2 = 1
for i in range(m,0,-1) :
    gop2 *= i

print((gop//gop2))