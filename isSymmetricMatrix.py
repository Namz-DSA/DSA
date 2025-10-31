def isSymmetric(matrix):
    noRows = len(matrix)
    noCols = len(matrix[0])
    if noRows != noCols:
        return False
    if noRows == noCols:
        for i in range(noRows):
            for j in range(noCols):
                if (matrix[i][j] != matrix[j][i]):
                    return False
    return True

print(isSymmetric(
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
))

print(isSymmetric(
    [
        [1,2,3],
        [2,5,6],
        [3,6,9]
    ]
))