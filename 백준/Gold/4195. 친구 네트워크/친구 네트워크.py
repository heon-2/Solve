import sys
input = sys.stdin.readline
# 빠른 출력을 위한 연습
answer = ""
def find_parent(parent,x) :
    if parent[x] != x :
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b,cnt) :
    aa = find_parent(parent,a)
    bb = find_parent(parent,b)
    if aa != bb :
        parent[bb] =aa
        cnt[aa] += cnt[bb]
DAT = [0] * 100001
T = int(input())
for tc in range(T) :
    F = int(input())

    cnt = dict()
    parent = dict()

    for i in range(F) :
        f1,f2 = map(str,input().split())
        # 중복되지 않게 각각의 이름에 키값을 부여해서 딕셔너리에 담기
        if f1 not in parent :
            parent[f1]=f1
            cnt[f1] = 1
        if f2 not in parent :
            parent[f2]=f2
            cnt[f2] = 1

        # 2개 입력받은 거 유니온
        union_parent(parent,f1,f2,cnt)
        print(cnt[find_parent(parent,f1)])