def solution(s):
    result=len(s)
    if result==1:
        return 1
    for length in range(1, len(s)//2+1, 1):
        idx=0
        압축_string=""
        last_iter=0
        for idx in range(0, len(s)-2*length+1, length):#idx+2*length-1<len(s) -> idx<len(s)+1-2*length
            if s[idx:idx+length]==s[idx+length:idx+2*length]:
                last_iter+=1
            else:
                if last_iter!=0:
                    압축_string+=str(last_iter+1)
                    last_iter=0
                압축_string+=s[idx:idx+length]
        if last_iter!=0:
            압축_string+=str(last_iter+1)
        압축_string+=s[idx+length:]
        #result.append(len(압축_string))
        result=min(len(압축_string), result)
    return result
