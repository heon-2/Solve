'''
< 문제 풀기 전 끄적임 >
매 초마다 번호가 낮은 종류의 바이러스부터 증식
이미 바이러스가 존재하면 증식 불가
s초가 지난 후에 (x,y)에 존재하는 바이러스의 종류 출력
바이러스 존재안하면 0을 출력
시험관의 맨위는 (1,1)임 그니깐 내가 생각하는거에서 -1 해야할듯?
s초뒤에 그냥 거기 있는 숫자 출력하면 될듯? 0은 신경안 써도 돼

N개의 줄에 걸쳐서 시험관의 정보가 주어진다
각 행은 N개의 원소로. 즉 N*N 배열인듯.
'''

# 1차 실패) 시간초과
# 그래프를 모두 순회해서 바이러스가 몇종류있는지 set에 담았음. 그리고 셋에 들어있는 바이러스를 모두 탐색하면서 확산

# 2차 실패) 시간초과
# 1차에서 시간초과나서 그래프를 한 번 탐색하면서 바이러스를 모두 큐에 담고 바이러스 순으로 정렬하는 방법으로 바꿈.
# => 여전히 시간초과

# 3차 시도) 성공
# 고려하지 못한 부분을 발견함. 내 코드는 바이러스가 확산될 만큼 확산되었는데도 어느정도 시간이 지나야 break되기 때문에 계속 돌아감.
# 그래서 매 초마다 0의 개수를 카운트해서 0이 없으면 더이상 시간 초만큼 반복문을 돌리는 게 무의미하므로 브레이크.

from collections import deque
N,K = map(int,input().split())
graph = [ list(map(int,input().split())) for _ in range(N) ]
S,Y,X = map(int,input().split())
second = 0
directy = [-1,0,0,1]
directx = [0,-1,1,0]

while True :
    # 반복문 그만 돌아가는 조건. ( 다 채워졌는데 돌아가는 건 무의미하니깐 )
    zero_cnt = 0
    for i in range(N) :
        for j in range(N) :
            if graph[i][j] == 0 :
                zero_cnt += 1
    if zero_cnt == 0 :
        print(graph[Y-1][X-1])
        break

    # 시간이 다 되었으면 브레이크
    if second == S :
        print(graph[Y-1][X-1])
        break

    # 큐를 만들고 0이 아닌 경우 바이러스의 종류와 그 위치를 큐에 담기
    q = deque()
    for i in range(N) :
        for j in range(N) :
            if graph[i][j] != 0:
                q.append((graph[i][j],i,j))
    # 큐를 정렬하고 다시 deque
    q = deque(sorted(q))

    # q에 들어있는 하나하나에 대해 사방으로 확산 딱 한번씩만 시킴.
    while q :
        virus,y,x = q.popleft()
        for i in range(4) :
            dy = directy[i] + y
            dx = directx[i] + x
            if 0<=dy<N and 0<=dx<N and graph[dy][dx] == 0:
                graph[dy][dx] = virus
    # 시간 경과에 따른 초 +1
    second += 1





