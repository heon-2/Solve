N = int(input())
cnt = 0
imotion = set()
for i in range(N) :
    name = input()
    if name == 'ENTER':
        cnt += len(imotion)
        imotion = set()
    else :
        imotion.add(name)
cnt += len(imotion)
print(cnt)

