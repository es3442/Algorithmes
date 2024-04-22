import heapq

def solution(operations):
    h=[]
    for operation in operations:
        if operation in ["D 1", "D -1"]:
            if len(h)!=0:
                num=operation[2]
                if num=="1":
                    h=heapq.nsmallest(len(h)-1, h)
                else:
                    heapq.heappop(h)
        else:#insert
            num=int(operation[2:])
            heapq.heappush(h, num)
    if len(h)==0:
        return [0, 0]
    return [max(h), h[0]]
