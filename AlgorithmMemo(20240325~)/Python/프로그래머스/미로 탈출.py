from collections import deque
directy = [-1,0,0,1] 
directx = [0,-1,1,0]

def bfs(st,ed,maps) :
    visited = [[False]*len(maps[0]) for _ in  range(len(maps))]
    visited[st[0]][st[1]] = True
    q = deque()
    q.append((st[0],st[1],0))
    while q :
        y,x,cnt = q.popleft()
        if y == ed[0] and x == ed[1] :
            return cnt
        for i in range(4) :
            dy = y + directy[i]
            dx = x + directx[i]
            if 0 <= dy < len(maps) and 0 <= dx < len(maps[0]) :
                if not visited[dy][dx] and maps[dy][dx] != 'X' :
                    visited[dy][dx] = True
                    q.append((dy,dx,cnt+1))
    return -1
def solution(maps):
    answer = 0
    maps = [list(row) for row in maps]
    for i in range(len(maps)) :
        for j in range(len(maps[0])) :
            if maps[i][j] == 'S' :
                start = [i,j]
            elif maps[i][j] == 'L' :
                lever = [i,j]
            elif maps[i][j] == 'E' :
                end = [i,j]
    dist_start_to_lever = bfs(start,lever,maps)
    if dist_start_to_lever == -1 :
        return -1
    dist_lever_to_end = bfs(lever,end,maps)
    if dist_lever_to_end == -1 :
        return -1
    answer = dist_start_to_lever + dist_lever_to_end
    return answer


'''
[풀이 일자] : 2024.04.27
[문제 출처] : 프로그래머스
[난이도] : Level 2
[문제 유형] : BFS
[문제 풀이] : S 에서 L로 가는 최단 거리를 구하고, L에서 E로 가는 최단거리를 구한 뒤, 더한다.
'''