import heapq

def solution(jobs):
    jobs.sort()
    h=[]

    last_time=-1
    time=0
    
    count=0
    last_idx=0
    
    answer=0
    while count<len(jobs):
        for job_idx in range(last_idx, len(jobs)):
            job=jobs[job_idx]
            if last_time<job[0]<=time:
                heapq.heappush(h, [job[1], job[0]])#소요시간, 시작시간
                last_idx+=1
            else:
                break
        if h:
            current=heapq.heappop(h)
            last_time=time
            time+=current[0]
            answer+=(time-current[1])
            count+=1
        else:
            time=jobs[last_idx][0]
    return answer//len(jobs)
        
        
