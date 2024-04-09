import sys
import heapq

f = sys.stdin.readline
N, K= map(int, f().split())

location=[]
virus_q=[]
for row in range(N):
    location.append(list(map(int, input().split())))
    for col in range(N):
        if location[row][col]!=0:
            heapq.heappush(virus_q, [0, location[row][col], row, col]) #second, virus_idx, row_idx, col_idx

f = sys.stdin.readline
S, X, Y= map(int, f().split())

while virus_q and virus_q[0][0] <= (S-1):
    if location[X-1][Y-1] != 0:
        break
    now = heapq.heappop(virus_q)
    four = [[now[2]-1, now[3]], [now[2]+1, now[3]],[now[2], now[3]-1], [now[2], now[3]+1]]
    for row_idx, col_idx in four:
        if row_idx >= 0 and row_idx < N and col_idx >= 0 and col_idx < N:
            if location[row_idx][col_idx] == 0:
                location[row_idx][col_idx] = now[1]
                heapq.heappush(virus_q, [now[0]+1, now[1], row_idx, col_idx])
print(location[X-1][Y-1])
