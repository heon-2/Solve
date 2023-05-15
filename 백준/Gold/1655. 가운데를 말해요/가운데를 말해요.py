from heapq import heappush,heappop
import sys
input = sys.stdin.readline
min_heap = []
max_heap = []

def push_num(num) :
    if len(min_heap) == len(max_heap) :
        heappush(max_heap,-num)
    else :
        heappush(min_heap,num)

    if min_heap and -max_heap[0] > min_heap[0] :
        temp_min = heappop(min_heap)
        temp_max = heappop(max_heap)
        heappush(max_heap,-temp_min)
        heappush(min_heap,-temp_max)

def find_median() :
    if len(min_heap) == len(max_heap) :
        return min(min_heap[0],-max_heap[0])
    else :
        return -max_heap[0]
N = int(input())
for i in range(N) :
    num = int(input())
    push_num(num)
    print(find_median())