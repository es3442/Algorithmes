import copy
empty_map = []
teacher = []
map_list = []

N = int(input())
for row_idx in range(N):
    now_row = input().split()
    map_list.append(now_row)
    for col_idx in range(N):
        if now_row[col_idx] == 'T':
            teacher.append([row_idx, col_idx])
        elif now_row[col_idx] == 'X':
            empty_map.append([row_idx, col_idx])
        else:
            continue


def search(map_list, teacher_list):
    N = len(map_list)
    for teacher in teacher_list:
        now_x = teacher[0]
        now_y = teacher[1]
        for row_idx in range(now_x-1, -1, -1):
            if map_list[row_idx][now_y] == 'O':
                break
            if map_list[row_idx][now_y] == 'S':
                return False

        for row_idx in range(now_x+1, N, 1):
            if map_list[row_idx][now_y] == 'O':
                break
            if map_list[row_idx][now_y] == 'S':
                return False

        for col_idx in range(now_y-1, -1, -1):
            if map_list[now_x][col_idx] == 'O':
                break
            if map_list[now_x][col_idx] == 'S':
                return False

        for col_idx in range(now_y+1, N, 1):
            if map_list[now_x][col_idx] == 'O':
                break
            if map_list[now_x][col_idx] == 'S':
                return False
    return True


if_okay = False
for first_idx in range(0, len(empty_map)-2):
    first_wall = empty_map[first_idx]
    for second_idx in range(first_idx+1, len(empty_map)-1):
        second_wall = empty_map[second_idx]
        for third_idx in range(second_idx+1, len(empty_map)):
            third_wall = empty_map[third_idx]
            temp_map = copy.deepcopy(map_list)
            temp_map[first_wall[0]][first_wall[1]] = 'O'
            temp_map[second_wall[0]][second_wall[1]] = 'O'
            temp_map[third_wall[0]][third_wall[1]] = 'O'
            is_okay = search(temp_map, teacher)
            if is_okay == True:
                break
        if is_okay == True:
            break
    if is_okay == True:
        break

if is_okay == True:
    print('YES')
else:
    print("NO")
