def rotate(key_xy, key_size):
    answer=[]
    for xy in key_xy:
        answer.append([xy[1], key_size-1-xy[0]])
    return answer

def solution(key, lock):
    key_xy=[[row_idx, col_idx] for row_idx in range(len(key)) for col_idx in range(len(key)) if key[row_idx][col_idx]==1]
    lock_xy=[[row_idx, col_idx] for row_idx in range(len(lock)) for col_idx in range(len(lock)) if lock[row_idx][col_idx]==0]
    
    if len(lock_xy)==0:
        return True
    if len(key_xy)<len(lock_xy):
        return False

    for _ in range(0, 4):
        for row_idx in range(-(len(key)-1), len(lock), 1): #0~lock+key-1
            for col_idx in range(-(len(key)-1), len(lock), 1):
                now_lock_xy=lock_xy[:]
                now_key_xy=[]
                for xy in key_xy:
                    if (xy[0]+row_idx)>=0 and (xy[0]+row_idx)<len(lock) and (xy[1]+col_idx)>=0 and (xy[1]+col_idx)<len(lock):
                        now_key_xy.append([xy[0]+row_idx, xy[1]+col_idx])

                now_key_xy.sort()
                now_lock_xy.sort()
                
                while len(now_lock_xy)>0 and len(now_key_xy)>0:
                    key_element=now_key_xy[-1]
                    lock_element=now_lock_xy[-1]
                    if key_element==lock_element:
                        now_key_xy.pop()
                        now_lock_xy.pop()
                    else:
                        break
                if len(now_lock_xy)==0 and len(now_key_xy)==0:
                    print(_, row_idx, col_idx)
                    return True
        key_xy=rotate(key_xy, len(key))
    return False
