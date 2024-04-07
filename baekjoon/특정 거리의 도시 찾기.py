from collections import defaultdict
from collections import deque
import sys

def solution():
    f = sys.stdin.readline
    N, M, K, X= map(int, f().split())
    city_link_dict=defaultdict(list)
    for _ in range(M):
        a, b=map(int, f().split())
        city_link_dict[a].append(b)
    
    q=deque([X])
    distance=deque([0])
    visited_city_list=[X]
    
    answer=[]
    while q:
        now_city=q.popleft()
        now_distance=distance.popleft()
        if now_distance==K:
            break
        for city in city_link_dict[now_city]:
            if city not in visited_city_list:
                q.append(city)
                distance.append(now_distance+1)
                visited_city_list.append(city)
                if now_distance+1==K:
                    answer.append(city)
        city_link_dict.pop(now_distance, None)

    if len(answer)==0:
        print("-1")
    else:
        answer.sort()
        for city in answer:
            print(city)

solution()
