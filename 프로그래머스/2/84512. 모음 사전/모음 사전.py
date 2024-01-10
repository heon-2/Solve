import sys
sys.setrecursionlimit(10**6)
def solution(word):
    answer = 0
    global lst
    lst = []
    alpha = ['A','E','I','O','U']
    for i in range(1,6) :
        dfs(i,[],alpha)
    lst.sort()
    
    return lst.index(word)+1

def dfs(level,path,alpha) :
    global lst
    if len(path) == level :
        lst.append(''.join(path))
        return
    for i in range(5) :
        dfs(level,path+[alpha[i]],alpha)
