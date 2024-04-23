from collections import defaultdict, deque
def can_change(word1, word2):
    count=0
    for char1, char2 in zip(word1, word2):
        if char1!=char2:
            count+=1
        if count>=2:
            return False
    return True

def solution(begin, target, words): #모든 단어의 길이가 같다.(최대10)
    visited=[0 for _ in range(len(words))]
    queue=deque()
    queue.append([begin, 0])
    
    while queue:
        word, length=queue.popleft() #word
        for idx, next_word in enumerate(words): #50개 이하의 단어
            if visited[idx]==0:
                if can_change(word, next_word)==True:
                    if next_word==target:
                        return length+1
                    visited[idx]=1
                    queue.append([next_word, length+1])
    return 0
