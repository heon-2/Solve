import sys
input = sys.stdin.readline
N,M = map(int,input().split())
lst = list(map(int,input().split()))
sub_sum = [0]
sum = 0
for i in lst :
    sum += i
    sub_sum.append(sum)
for i in range(M) :
    st,ed = map(int,input().split())
    print(sub_sum[ed]-sub_sum[st-1])