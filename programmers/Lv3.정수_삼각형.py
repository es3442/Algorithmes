#아래에서 위
def solution(triangle):
    for row in range(len(triangle)-2, -1, -1):
        for col in range(0, row+1, 1):
            triangle[row][col]+=max(triangle[row+1][col], triangle[row+1][col+1])
    return triangle[0][0]
 
 #위에서 아래
 def solution(triangle):
    for row in range(1, len(triangle), 1):
        for col in range(0, row+1, 1):
            if col==0:#오른쪽 위만 가능
                triangle[row][col]+=triangle[row-1][col]
            elif col==row:#왼쪽 위만 가능
                triangle[row][col]+=triangle[row-1][col-1]
            else:
                triangle[row][col]+=max(triangle[row-1][col], triangle[row-1][col-1])
    return max(triangle[len(triangle)-1])
