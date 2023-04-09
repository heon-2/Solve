N = int(input())
gop = 1
def fact(level) :
    global gop
    if level == 0 :
        return
    gop *= level
    fact(level-1)
fact(N)

gop_lst = list(str(gop))

gop_lst.reverse()
cnt = 0
for i in gop_lst :
    if i == '0' :
        cnt += 1
    else :
        print(cnt)
        break