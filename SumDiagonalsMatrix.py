def SumDiagonal(matrix):
    main_diag_sum = sum([matrix[i][i] for i in range(len(matrix))])
    sec_diag_sum = sum([matrix[i][len(matrix)-1-i] for i in range(len(matrix))])
    total = main_diag_sum + sec_diag_sum
    total -= matrix[len(matrix)//2][len(matrix)//2]
    return total

print(SumDiagonal([
    [1,2,3],
    [4,5,6],
    [7,8,9]
]))