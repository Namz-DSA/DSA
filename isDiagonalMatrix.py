def isDiagonal(matrix):
    noRows = len(matrix)
    noCols = len(matrix[0])

    if noRows == noCols:
        for i in range(noRows):
            for j in range(noCols):
                if (i > j or i < j) and matrix[i][j] != 0:
                    return False
    return True


print(
    isDiagonal(
        [
            [1,0,0],
            [0,7,0],
            [0,0,9]
        ]
    )
)

print(
    isDiagonal(
        [
            [1,0,2],
            [0,0,0],
            [0,0,9]
        ]
    )
)