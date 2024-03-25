import math
N,K = map(int,input().split())
cnt = 0
room = [ [0] * 2 for _ in range(6) ]
for i in range(N) :
    sex, grade = map(int,input().split())
    room[grade-1][sex] += 1

for i in range(6) :
    for j in range(2) :
        if room[i][j] > 0 :
            cnt += math.ceil(room[i][j]/K)

print(cnt)
