def upperTriangular(matrix):
    noRows = len(matrix)
    noCols = len(matrix[0])

    if noRows == noCols:
        for i in range(noRows):
            for j in range(noCols):
                if i > j and matrix[i][j] != 0:
                    return False
    return True


print(
    upperTriangular(
        [
            [1,2,3],
            [0,5,6],
            [0,0,9]
        ]
    )
)

print(
    upperTriangular(
        [
            [1,2,3],
            [4,5,6],
            [0,0,9]
        ]
    )
)