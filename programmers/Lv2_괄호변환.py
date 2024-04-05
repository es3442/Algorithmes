def split_balance(string): #balance로 split
    sum=0
    index=0
    for idx, bracket in enumerate(string):
        if bracket=='(':
            sum-=1
        else:
            sum+=1
        if sum==0:
            break
    return string[:idx+1], string[idx+1:]

def is_correct_str(string):
    sum=0
    for bracket in string:
        if bracket=='(':
            sum-=1
        else:
            sum+=1
        if sum>0:
            return False
    return sum==0

def reverse_str(string):
    answer=''
    for bracket in string:
        if bracket=='(':
            answer+=')'
        else:
            answer+='('
    return answer

def solution(p): #2이상 짝수
    if len(p)==0:
        return ''
    idx=0
    while idx<len(p):
        u, v=split_balance(p)
        if is_correct_str(u)==True:
            return u+solution(v)
        else:
            return '('+solution(v)+')'+reverse_str(u[1:-1])
