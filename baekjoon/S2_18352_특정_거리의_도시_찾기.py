from collections import defaultdict
from collections import deque
import sys

f = sys.stdin.readline
N, M, K, X= map(int, f().split())
city_link_list=[[] for _ in range(N+1)]
for _ in range(M):
    a, b=map(int, f().split())
    city_link_list[a].append(b)

q = deque([[X, 0]])

answer = []
visited = [X]

while q:
    if q[0][1] == K:
        break
    now = q.popleft()
    now_city = now[0]
    now_distance = now[1]

    if len(city_link_list[now_city]) != 0:
        for next_city in city_link_list[now_city]:
            if next_city not in visited:
                q.append([next_city, now_distance+1])
                visited.append(next_city)
                if now_distance+1 == K:
                    answer.append(next_city)

if len(answer) == 0:
    print("-1")
else:
    answer.sort()
    for city in answer:
        print(city)
