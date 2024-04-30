import math
def solution(progresses, speeds): 
    day=[math.ceil((100-progress)/speed) for progress, speed in zip(progresses, speeds)]

    answer=[1]
    last_day=day[0]
    for idx in range(1, len(day)):
        if last_day>=day[idx]:
            answer[-1]+=1
        else:
            last_day=day[idx]
            answer.append(1)
            
    return answer
