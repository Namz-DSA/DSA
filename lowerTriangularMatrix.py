def lowerMatrix(matrix):
    noRows = len(matrix)
    noCols = len(matrix[0])

    if noRows == noCols:
        for i in range(noRows):
            for j in range(noCols):
                if i < j and matrix[i][j] != 0:
                    return False
    return True


print(
    lowerMatrix(
        [
            [1,0,0],
            [4,5,0],
            [7,8,9]
        ]
    )
)

print(
    lowerMatrix(
        [
            [1,0,3],
            [4,5,0],
            [7,8,9]
        ]
    )
)