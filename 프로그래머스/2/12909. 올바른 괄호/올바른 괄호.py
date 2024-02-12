def solution(s):
    answer = True
    q = []
    s = list(s)
    for i in s :
        if i == "(" :
            q.append("(")
        elif i == ")" :
            try :
                q.pop()
            except :
                answer = False
                break
    if q : 
        answer = False
    
    return answer