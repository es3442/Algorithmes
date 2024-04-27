from collections import defaultdict
def solution(genres, plays):
    genre_count=defaultdict(int)
    genre_idx=defaultdict(list)
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        genre_count[genre]+=play
        genre_idx[genre].append([play, idx])
    sorted_genre_num=sorted(genre_count.items(), key=lambda x:-x[1])

    for sorted_genre in sorted_genre_num:
        key=sorted_genre[0]
        genre_dict[key].sort(key=lambda x:(-x[0], x[1]))
        answer.append(genre_dict[key][0][1])
        if len(genre_dict[key])>1:
            answer.append(genre_dict[key][1][1])
    return answer
