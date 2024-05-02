DAT = [False] * 10100
n = 0
while n < 10000 :
    n += 1
    num = list(str(n))
    summ = n
    for i in num :
        summ += int(i)
    DAT[summ] = True
for i in range(1,10001) :
    if not DAT[i] :
        print(i)

'''
[풀이 일자] : 2024.05.02
[문제 출처] : 백준
[난이도] : Silver 5
[문제 유형] : 구현
[문제 풀이] : 
1번부터 10000번까지 셀프 넘버를 구해서 셀프 넘버들을 모두 DAT 배열에 True로 바꿈.
이후 1부터 10000까지 순회하며 배열의 값이 False이면 출력을 진행함.
'''