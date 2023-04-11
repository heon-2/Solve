from heapq import heapify,heappush,heappop
import sys
input = sys.stdin.readline
N = int(input())
heap = []
heapify(heap)

for i in range(N) :
    x = int(input())
    if x == 0 :
        if len(heap) == 0 :
            print(0)
        else :
            a = heappop(heap)
            print(a)


    else :
        heappush(heap,x)