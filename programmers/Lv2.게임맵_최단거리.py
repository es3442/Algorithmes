from collections import deque
def solution(maps):
    row=len(maps)
    col=len(maps[0])
    if row==1 and col==1:
        return 1
    stack=deque()
    stack.append([0, 0, 1])
    maps[0][0]=0
    
    while stack:#[x, y, 거리]
        now=stack.popleft()
        next_list=[[now[0]-1, now[1]],[now[0], now[1]-1],[now[0]+1, now[1]], [now[0], now[1]+1]]  
        for n in next_list:
            if 0<=n[0]<row and 0<=n[1]<col and maps[n[0]][n[1]]==1:
                if n[0]==row-1 and n[1]==col-1:
                    return now[2]+1
                stack.append([n[0], n[1], now[2]+1])
                maps[n[0]][n[1]]=0
    return -1
