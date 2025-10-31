def SumRowCol(matrix):
    row_sum = []
    col_sum = [0] * len(matrix[0])

    for row in matrix:
        row_sum.append(sum(row))
    
    for row in matrix:
        for i in range(len(row)):
            col_sum[i] += row[i]
    
    return (row_sum,col_sum)

print(SumRowCol([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]))