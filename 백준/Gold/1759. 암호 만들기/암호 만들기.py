# pick : 뽑는 수 / N : 전체 개수
pick,N = map(int,input().split())

# 뽑을 수 있는 것들 담아놓기
lst = list(map(str,input().split()))
# 알파벳이 증가하는 순서대로 출력하기 위해 오름차순 정렬
lst.sort()
visited =[False]*N
# 모음 리스트
vowels_lst = ['a','e','i','o','u']
def comb(level,start,path) :
    if level == pick :
        # 모음 / 자음
        vowels = 0
        consonants = 0
        # 모음 찾으면 모음 +1 / 아니면 자음 + 1
        for i in range(pick) :
            if path[i] in vowels_lst :
                vowels += 1
            else :
                consonants += 1
        # 모음이 1개 이상이고 자음이 2개 이상이면 출력을 위해 join 사용하고 출력
        if vowels >= 1 and consonants >= 2:
            ans = ''.join(path)
            print(ans)
        return

    for i in range(start,N) :
        if not visited[i] :
            visited[i] = True
            comb(level+1,i,path+[lst[i]])
            visited[i] = False
# 맨날 전역변수로 path =[] 로 해놓고 풀었는데, 이번엔 그냥 매개변수로 풀어봄 ㅋㅋ
comb(0,0,[])


