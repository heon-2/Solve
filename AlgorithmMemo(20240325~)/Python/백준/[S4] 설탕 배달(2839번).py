BAG = [10e9] * 5001
for i in range(2000) :
    for j in range(2000) :
        SUGAR = 3*i + 5*j
        if SUGAR < 5001 :
            BAG[SUGAR] = min(BAG[SUGAR],i+j)
n = int(input())
if BAG[n] == 10e9 :
    print(-1)
else :
    print(BAG[n])

'''
[풀이 일자] : 2024.05.02
[문제 출처] : 백준
[난이도] : Silver 4
[문제 유형] : 구현
[문제 풀이] : 
설탕 킬로그램인 n값의 범위가 5000이하 이므로 3과 5를 각각 0~2000씩 곱하는 반복문을 돌려도
시간초과가 나지 않을 것으로 생각하고 반복문으로 구현해서 풀이함.

근데, 문제를 풀이하고 나니 동전 DP 문제와 유사한 문제라는 생각이 들어
재사용가능한 로직으로 재구현 해보았다.
'''

# 문제 풀이 2
BAG = [10e9] * 5010
three,three_cnt = 0,0
five,five_cnt = 0,0
while three < 5001 :
    three += 3
    three_cnt += 1
    BAG[three] = three_cnt
while five < 5001 :
    five += 5
    five_cnt += 1
    BAG[five] = five_cnt
for i in range(3,5001) :
    if BAG[i-3] == 10e9 and BAG[i-5] == 10e9 :
        continue
    else :
        BAG[i] = min(BAG[i-3],BAG[i-5])+1
n = int(input())
if BAG[n] == 10e9 :
    print(-1)
else :
    print(BAG[n])
'''
3의 배수로 채우고,
5의 배수를 채우면 항상 최솟값으로 갱신된다.

이후 3~5000까지 순회하며 i-3과 i-5에 봉지 사용 개수가 있다면,
i-3번째 숫자에서 사용한 봉지수와 i-5번째 사용한 봉지수 중 최솟값을 구한 뒤 +1 을 하면 된다.
'''
