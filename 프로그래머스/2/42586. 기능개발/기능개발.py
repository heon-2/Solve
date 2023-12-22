def solution(progresses, speeds):
    answer = []
    length = len(progresses)
    completed = [0]*(length)
    idx = 0
    while True :
        if sum(completed) == length :
            break
            
        if completed[idx] == 1 :
            idx += 1
            continue
        # 하루 지날때마다 진행률 더하기
        for i in range(length): 
            progresses[i] += speeds[i]
        
        if progresses[idx] >= 100 :
            completed[idx] = 1
            cnt = 1
            idx += 1
            for i in range(idx,length) :
                if completed[i] == 0 :
                    if progresses[i]>= 100 :
                        completed[i]=1
                        cnt+=1
                    else :
                        break

            answer.append(cnt)
                    
                        
                        
                
                
            
        
    
    return answer