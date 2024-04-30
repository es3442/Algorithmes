from collections import deque
def solution(priorities, location):
    answer=0
    priority_q=deque([[idx, priority] for idx, priority in enumerate(priorities)])
    
    while len(priority_q)>0:
        answer+=1
        prioty_list=[priority[1] for priority in priority_q]
        max_index=prioty_list.index(max(prioty_list))
        if priority_q[max_index][0]==location:
            return answer
        else:
            priority_q.rotate(-max_index)
            priority_q.popleft()
    return answer
