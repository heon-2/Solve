N = int(input())
if N % 2 == 0 :
    print('CY')
else :
    print('SK')

'''
[풀이 일자] : 2024.05.01
[문제 출처] : 백준
[난이도] : Silver 5
[문제 유형] : DP
[문제 풀이] : 
DP지만 둘다 홀수개의 돌만 가져가므로 결국
N이 2의 짝수인지 아니냐에 따라 답이 결정됨.
'''