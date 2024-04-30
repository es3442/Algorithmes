def solution(s):
    left=0
    for char in s:
        if char=='(':
            left+=1
        else: #')'
            if left==0:
                return False
            left-=1
    return True if left==0 else False
