import heapq
def solution(food_times, k):
    if sum(food_times)<=k:
        return -1
    
    h=[]
    for idx, food in enumerate(food_times):
        heapq.heappush(h, [food, idx+1])
        
    sum_eat=0
    prev_eat=0
    while sum_eat+(h[0][0]-prev_eat)*len(h)<=k:
        now_eat=h[0][0]
        sum_eat+=(now_eat-prev_eat)*len(h)
        while len(h)>0:
            if h[0][0]==now_eat:
                heapq.heappop(h)
            else:
                break
        prev_eat=now_eat
    h_idx=sorted([row[1] for row in h])
    return h_idx[(k-sum_eat)%len(h_idx)]
