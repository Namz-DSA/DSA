def diagonals(matrix):
    main_diag = [matrix[i][i] for i in range(len(matrix))]
    sec_diag = [matrix[i][len(matrix)-1-i] for i in range(len(matrix))]
    return (main_diag, sec_diag)

print(diagonals([
    [1,2,3],
    [4,5,6],
    [7,8,9]
]))