from collections import Counter

def solution(N, stages):
    answer=[]
    counter=Counter(stages)
    all_clear=0
    
    if N+1 in counter.keys():
        all_clear=counter[N+1]
    
    for stage in range(N, 0, -1):
        if stage  in counter.keys():
            answer.append([counter[stage]/(counter[stage]+all_clear), stage])
            all_clear+=counter[stage]
        else:
            answer.append([0, stage])

    answer.sort(key=lambda x:(-x[0], x[1]))
    return [stage_fail[1] for stage_fail in answer]
