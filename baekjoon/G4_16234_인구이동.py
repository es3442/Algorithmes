N, L, R = list(map(int, input().split()))
population_list = [[] for _ in range(N)]
for row_idx in range(N):
    population_list[row_idx] = list(map(int, input().split()))
  
def bfs(graph, visited, now_row, now_col, L, R):
    bfs_stack = [[now_row, now_col]]
    answer = [[now_row, now_col]]

    while len(bfs_stack) > 0:
        x, y = bfs_stack.pop()
        now_value = graph[x][y]
        # 상
        if x > 0:
            if visited[x-1][y] == 0 and abs(now_value-graph[x-1][y]) >= L and abs(now_value-graph[x-1][y]) <= R:
                visited[x-1][y] = 1
                bfs_stack.append([x-1, y])
                answer.append([x-1, y])
        # 하
        if x < len(graph)-1:
            if visited[x+1][y] == 0 and abs(now_value-graph[x+1][y]) >= L and abs(now_value-graph[x+1][y]) <= R:
                visited[x+1][y] = 1
                bfs_stack.append([x+1, y])
                answer.append([x+1, y])
        # 좌
        if y > 0:
            if visited[x][y-1] == 0 and abs(now_value-graph[x][y-1]) >= L and abs(now_value-graph[x][y-1]) <= R:
                visited[x][y-1] = 1
                bfs_stack.append([x, y-1])
                answer.append([x, y-1])
        # 우
        if y < len(graph)-1:
            if visited[x][y+1] == 0 and abs(now_value-graph[x][y+1]) >= L and abs(now_value-graph[x][y+1]) <= R:
                visited[x][y+1] = 1
                bfs_stack.append([x, y+1])
                answer.append([x, y+1])

    if len(answer) > 1:
        move_value = sum([population_list[row][col]
                         for row, col in answer])//len(answer)
        for row, col in answer:
            population_list[row][col] = move_value
        return False

    return True


day = 0
while day <= 2000:
    break_flag = True
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for row_idx in range(N):
        for col_idx in range(N):
            if visited[row_idx][col_idx] == 0:
                visited[row_idx][col_idx] = 1
                break_flag = break_flag & bfs(
                    population_list, visited, row_idx, col_idx, L, R)
    if break_flag == False:
        day += 1
    else:
        break
print(day)
