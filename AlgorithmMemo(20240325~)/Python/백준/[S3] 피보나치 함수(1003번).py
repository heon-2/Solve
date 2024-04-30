T = int(input())
for tc in range(T) :
    n = int(input())
    return_zero = [0] * 41
    return_one = [0] * 41
    return_zero[0] = 1
    return_zero[1] = 0
    return_one[0] = 0
    return_one[1] = 1
    for i in range(2,n+1) :
        return_zero[i] = return_zero[i-1] + return_zero[i-2]
        return_one[i] = return_one[i-1] + return_one[i-2]
    print(return_zero[n],return_one[n])

'''
[풀이 일자] : 2024.04.30
[문제 출처] : 백준
[난이도] : Silver 3
[문제 유형] : DP
[문제 풀이] : 
0을 리턴하는 배열과 1을 리턴하는 횟수가 담긴 배열을 따로 운용함.
각각 i-1 과 i-2 를 더해야 i가 나오므로 각각 계산
'''