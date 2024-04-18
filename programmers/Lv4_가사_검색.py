from collections import Counter
def search_right(words_list, word):
    start_idx=0
    end_idx=len(words_list)
    while start_idx<end_idx:
        mid=(start_idx+end_idx)//2
        if words_list[mid]==word:
            return idx
        elif words_list[mid]<word:
            start_idx=mid+1
        else:#>start
            end_idx=mid
    return start_idx
            
def solution(words, queries):
    word_list=[[] for _ in range(10001)]#0~10,000
    word_list_reverse=[[] for _ in range(10001)]#0~10,000
    for word in words:
        word_list[len(word)].append(word)
        word_list_reverse[len(word)].append(word[::-1])
    for word, word_reverse in zip(word_list, word_list_reverse):
        word.sort()
        word_reverse.sort()
    
    answer=[]
    for query in queries:
        query_count=Counter(query.split('?'))
        question_len=query_count['']
        if query[0]=='?':
            query=query[::-1]
            start=query[:-question_len]+'a'*question_len
            end=query[:-question_len]+'z'*question_len
            start_idx=search_right(word_list_reverse[len(query)], start)
            end_idx=search_right(word_list_reverse[len(query)], end)
        else:#*?
            start=query[:-question_len]+'a'*question_len
            end=query[:len(query)-question_len]+'z'*question_len
            start_idx=search_right(word_list[len(query)], start)
            end_idx=search_right(word_list[len(query)], end)
        answer.append(end_idx-start_idx)
    return answer
