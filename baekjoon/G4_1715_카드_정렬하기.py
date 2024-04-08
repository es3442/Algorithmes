import heapq
N=int(input())
answer=0
card_list=[]
for _ in range(N):
    heapq.heappush(card_list, int(input()))

while len(card_list)>1:
    first_small=heapq.heappop(card_list)
    second_small=heapq.heappop(card_list)
    sum=first_small+second_small
    answer+=sum
    heapq.heappush(card_list, sum)

print(answer)
