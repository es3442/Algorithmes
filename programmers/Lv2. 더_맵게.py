import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer=0
    while len(scoville)>=2:
        scoville_first=heapq.heappop(scoville)
        if scoville_first<K:
            scoville_second=heapq.heappop(scoville)
            heapq.heappush(scoville, scoville_first+scoville_second*2)
            answer+=1
        else:
            return answer
    if len(scoville)==1:
        if heapq.heappop(scoville)>=K:
            return answer
    return -1
