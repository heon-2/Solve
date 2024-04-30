number = int(input())
steps = [0]* 301
for i in range(number) :
    step = int(input())
    steps[i+1] = step
arr = [0] * 301
arr[1] = steps[1]
arr[2] = steps[1] + steps[2]
arr[3] = max(steps[2] + steps[3], steps[1] + steps[3])
for i in range(4,number+1) :
    arr[i] = max(arr[i-3] + steps[i-1] + steps[i], arr[i-2] + steps[i])
print(arr[number])

'''
[풀이 일자] : 2024.04.30
[문제 출처] : 백준
[난이도] : Silver 3
[문제 유형] : DP
[문제 풀이] : 계단의 시점에서 계단이 어디서 올라왔는지를 생각해보자.
3번째 계단까지는 도출해낼 수 있을 것이고,
4번째 계단부터는 3번째 이전 계단까지의 최댓값 + 이전계단의 값 + 지금 계단값 과
2번째 이전 계단까지의 최댓값 + 지금 계단값을 비교해서 둘 중 큰 값으로 갱신한다.

왜 dp[i-1] 과 dp[i-2] 를 직접 비교하지 않느냐면, 3번 연속 계단을 밟으면 안 되기 때문에
직전에서 올라온 계단은 무조건 한 칸을 건너뛰어 온 것임을 알아야 함. 따라서 3계단 직전까지의 최댓값과 이전 계단을 밟았
[배운 점] : 
'''