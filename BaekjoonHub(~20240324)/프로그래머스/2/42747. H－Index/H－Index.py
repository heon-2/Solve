def solution(citations):
    DAT = [0]*10001
    for i in citations :
        DAT[i] += 1
    answer = 0
    for i in range(1000,0,-1) :
        lst = DAT[i:]
        if i <= sum(lst) :
            answer = i
            break
    return answer
    
