from heapq import heappush,heappop
import sys
input = sys.stdin.readline


def push_num(num) :
    if len(max_heap) == len(min_heap) :
        heappush(max_heap,-num)
    else :
        heappush(min_heap,num)

    if min_heap and -max_heap[0] > min_heap[0] :
        temp_min = heappop(min_heap)
        temp_max = heappop(max_heap)
        heappush(max_heap,-temp_min)
        heappush(min_heap,-temp_max)

def find_median() :
    return -max_heap[0]

T = int(input())
for tc in range(T) :
    max_heap = []
    min_heap = []
    ans_lst = []
    n = int(input())
    a = []
    for i in range(n//10+1) :
        lst = list(map(int,input().split()))
        a+=lst

    for i in range(n) :
        num = a[i]
        push_num(num)
        if i%2 == 0 :
            ans = find_median()
            ans_lst.append(ans)
    print(len(ans_lst))

    cnt = 0
    for i in range(len(ans_lst)) :
        print(ans_lst[i],end=' ')

        cnt += 1
        if cnt%10 == 0 :
            print()
    print()