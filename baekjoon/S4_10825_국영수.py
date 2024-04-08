N=int(input())
score_list=[]
for _ in range(N):
    child_score_info=input().split()
    score_list.append([child_score_info[0], int(child_score_info[1]), int(child_score_info[2]), int(child_score_info[3])])
score_list.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))

for element in score_list:
    print(element[0])
