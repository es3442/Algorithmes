import copy
N, M = map(int, input().split())
map_list = [[] for _ in range(N)]
zero_list = []
virus_list = []
for row_idx in range(N):
    map_list[row_idx] = list(map(int, input().split()))
    for col_idx in range(M):
        if map_list[row_idx][col_idx] == 0:
            zero_list.append([row_idx, col_idx])
        elif map_list[row_idx][col_idx] == 2:
            virus_list.append([row_idx, col_idx])
        else:
            continue


def dfs(temp_map, virus_list):
    row_len = len(temp_map)
    col_len = len(temp_map[0])
    while len(virus_list) != 0:
        now_virus = virus_list.pop()
        row_idx = now_virus[0]
        col_idx = now_virus[1]
        if row_idx+1 < row_len:
            # bottom
            if temp_map[row_idx+1][col_idx] == 0:
                temp_map[row_idx+1][col_idx] = 2
                virus_list.append([row_idx+1, col_idx])
        if row_idx > 0:
           # top
            if temp_map[row_idx-1][col_idx] == 0:
                temp_map[row_idx-1][col_idx] = 2
                virus_list.append([row_idx-1, col_idx])

        if col_idx+1 < col_len:
            # right
            if temp_map[row_idx][col_idx+1] == 0:
                temp_map[row_idx][col_idx+1] = 2
                virus_list.append([row_idx, col_idx+1])
        if col_idx > 0:
            # left
            if temp_map[row_idx][col_idx-1] == 0:
                temp_map[row_idx][col_idx-1] = 2
                virus_list.append([row_idx, col_idx-1])

    sum_zero = 0
    for row_idx in range(row_len):
        for col_idx in range(col_len):
            if temp_map[row_idx][col_idx] == 0:
                sum_zero += 1
    return sum_zero


answer = []

for first_idx in range(0, len(zero_list)-2):  # len(idx_list)-1-2까지 가능
    first_wall = zero_list[first_idx]
    for second_idx in range(first_idx+1, len(zero_list)-1):
        second_wall = zero_list[second_idx]
        for third_idx in range(second_idx+1, len(zero_list)):
            third_wall = zero_list[third_idx]

            temp_map = copy.deepcopy(map_list)
            temp_map[first_wall[0]][first_wall[1]] = 1
            temp_map[second_wall[0]][second_wall[1]] = 1
            temp_map[third_wall[0]][third_wall[1]] = 1
            answer.append(dfs(temp_map, virus_list[:]))

print(max(answer))
