def is_build_okay(x, y, type, answer):
    if type==0: #기둥-> 바닥위, 보의 한쪽 끝 부분 위, 다른 기둥 위
        if y==0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
            return True
    else:
        if y>0:
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer:
                return True
            if [x-1, y, 1] in answer and [x+1, y, 1] in answer:
                return True
    return False

def solution(n, build_frame):

    answer=[]
    for now in build_frame:
        if now[3]==0: #삭제
            all_okay=True
            check_answer_xy=[]
            check_answer_xy=[xy for xy in [[now[0]-1, now[1], 1], [now[0], now[1], 1], [now[0]-1, now[1]+1, 1], [now[0], now[1]+1, 1], [now[0]+1, now[1], 1]] if xy in answer]
            check_answer_xy+=[xy for xy in [[now[0], now[1]-1, 0], [now[0], now[1], 0],  [now[0], now[1]+1, 0], [now[0]+1, now[1]-1, 0],[now[0]+1, now[1], 0]] if xy in answer]
            
            temp_answer=answer[:]
            
            if now[2]==0:
                temp_answer.remove([now[0], now[1], 0])
            else:
                temp_answer.remove([now[0], now[1], 1])
                
            for xy in check_answer_xy:
                all_okay=is_build_okay(xy[0], xy[1], xy[2], temp_answer)
                if all_okay==False:
                    break
                    
            if all_okay==True:
                if now[2]==0:
                    answer.remove([now[0], now[1], 0])
                else:
                    answer.remove([now[0], now[1], 1])
        else:
            if now[2]==0: #기둥
                if is_build_okay(now[0], now[1], 0, answer):#설치
                    answer.append([now[0], now[1], 0])
            else: #보 조건
                if is_build_okay(now[0], now[1], 1, answer):#설치
                    answer.append([now[0], now[1], 1])
    answer.sort()
    return answer
