from collections import deque
def solution(s):
    q1 = deque(list(s))
    q2 = deque()
    first = q1.popleft()
    
    if first == ')' :
        return False
    else :
        q2.append(first)
        while q1 :
            try :
                v = q1.popleft()
                if v == ')' :
                    q2.pop()
                else :
                    q2.append('(')
            except:
                return False
    if q2 :
        return False
    else :
        return True
                
            
        
    