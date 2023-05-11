from heapq import heappop,heappush,heapify
import sys
input = sys.stdin.readline
heap =[]
heapify(heap)

N =int(input())
for i in range(N) :
    x = int(input())
    if x != 0 :
        heappush(heap,(abs(x),x))
    elif x == 0 :
        if len(heap) :
            x,y = heappop(heap)
            print(y)
        else :
            print(0)