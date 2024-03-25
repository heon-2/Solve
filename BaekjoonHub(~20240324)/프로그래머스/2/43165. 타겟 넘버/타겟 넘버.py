def dfs(idx,numbers,target,summ) :
    global answer
    if idx == len(numbers)-1 :
        if summ == target :
            answer += 1
        return
    else :
        dfs(idx+1,numbers,target,summ + numbers[idx+1])
        dfs(idx+1,numbers,target,summ - numbers[idx+1])
        return

def solution(numbers, target):
    global answer
    idx = -1
    answer = 0
    summ  = 0
    dfs(idx,numbers,target,summ)
    return answer