def solution(k, dungeons):
    global answer  
    answer = 0
    visited = [False]*len(dungeons)
    dfs(visited,0,[],k,dungeons)
    return answer

def dfs(visited,level,path,k,dungeons) :
    global answer
    answer = max(answer,level)
    if level == len(dungeons) :
        return

    for i in range(len(dungeons)) :
        if not visited[i] and k >= dungeons[i][0] :
            visited[i] = True
            dfs(visited,level+1,path+[i],k-dungeons[i][1],dungeons)
            visited[i] = False
