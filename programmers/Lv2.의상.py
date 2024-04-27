from collections import Counter
def solution(clothes):
    clothes_count = Counter([kind for name, kind in clothes])
    answer=1
    for clothes_num in clothes_count.values():
        answer*=(clothes_num+1)
    return answer-1
