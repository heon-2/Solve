N = int(input())
num_lst = list(map(int,input().split()))
cal = list(map(int,input().split()))
cal_lst = []

# 순열을 사용하기 위해서 더하기,빼기,나눗셈,곱하기에 적힌 숫자만큼 cal_lst에 추가하기
if cal[0] != 0 :
    for i in range(cal[0]):
        cal_lst.append('a')
if cal[1] != 0 :
    for i in range(cal[1]):
        cal_lst.append('s')
if cal[2] != 0 :
    for i in range(cal[2]) :
        cal_lst.append('m')
if cal[3] != 0:
    for i in range(cal[3]):
        cal_lst.append('d')

visited = [False]*(N-1)
# 중복 제거 & 속도향상을 위해 set사용
cal_perm_lst = set()
def dfs(level,x) :
    if level == N-1 :
        # set 사용을 위해 튜플로 변환해서 넣기
        # list는 not hasable 이라 set에 안 들어가.
        cal_perm_lst.add(tuple(x))
        return

    for i in range(N-1) :
        if not visited[i] :
            visited[i] = True
            dfs(level+1,x+[cal_lst[i]])
            visited[i] = False
dfs(0,[])

# 정답 후보 리스트 만들기
ans_lst = []
# 계산해야하는 맨 첫 숫자를 temp라는 변수에 담고
temp = num_lst[0]
# 각 연산자에 따라 계산을 맞게 해주기
for i in cal_perm_lst :
    for j in range(N-1) :
        if i[j] == 'a' :
            temp += num_lst[j+1]
        elif i[j] == 's' :
            temp -= num_lst[j+1]
        elif i[j] == 'm' :
            temp *= num_lst[j+1]
        elif i[j] == 'd' :
            if temp < 0 :
                temp = -temp
                temp = -(temp // num_lst[j + 1])
            else :
                temp = temp//num_lst[j+1]
    # 연산이 끝났다면, 정답 후보 리스트에 담기
    ans_lst.append(temp)
    # temp 변수 초기화.
    temp = num_lst[0]

# 최댓값과 최솟값을 출력하기
print(max(ans_lst))
print(min(ans_lst))
