N = int(input())
from collections import deque
q = deque()

for _ in range(1,N+1) :
    q.append(_)

i=0
while len(q) != 1 :
    if i % 2 == 0 :
        q.popleft()
    else :
        v = q.popleft()
        q.append(v)

    i+=1

print(q[0])