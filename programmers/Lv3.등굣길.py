def solution(m, n, puddles):
    answer=[[0 for _ in range(n+1)] for _ in range(m+1)]
    answer[1][0]=1
    for row in range(1, m+1, 1):
        for col in range(1, n+1, 1):
            #왼쪽이나 오른쪽으로 이동
            if [row, col] in puddles:
                answer[row][col]=0
            else:
                if row==1:
                    answer[row][col]=answer[row][col-1]
                elif col==1:
                    answer[row][col]=answer[row-1][col]
                else:
                    answer[row][col]=answer[row-1][col]+answer[row][col-1]
    return answer[m][n]%1000000007
