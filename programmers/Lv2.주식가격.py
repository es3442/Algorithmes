def solution(prices):
    last_min=prices[-1]
    last_min_idx=len(prices)-1
    answer=[0]
    
    for now_idx in range(last_min_idx-1, -1, -1):
        now=prices[now_idx]
        if now<=last_min:#끝까지 감소하지 않음
            answer.append(len(prices)-now_idx-1)
            last_min, last_min_idx=now, now_idx
        else:#어디가 최소인지 찾기
            for next_idx in range(now_idx+1, last_min_idx+1):
                if now>prices[next_idx]:
                    answer.append(next_idx-now_idx)
                    break
    return answer[::-1]
