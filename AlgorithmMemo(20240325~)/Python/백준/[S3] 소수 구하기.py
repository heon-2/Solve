import math
st,ed = map(int,input().split())
odds = [True] * (ed+1)
odds[1] = False # 1은 소수가 아니므로 미리 체크
for i in range(2,int(math.sqrt(ed))+1) :
    j,num = 1,1
    while True :
        j += 1
        num = i*j
        if num > ed:
            break
        else:
            odds[num] = False
for i in range(st,ed+1) :
    if odds[i] :
        print(i)

'''
[풀이 일자] : 2024.05.03
[문제 출처] : 백준
[난이도] : Silver 3
[문제 유형] : 소수 구하기
[문제 풀이] : 
에라토스테네스의 체를 사용해 소수를 구하여 출력함.
'''