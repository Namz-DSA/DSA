def transposeMatrix(matrix):
    noRows = len(matrix)

    noCols = len(matrix[0])

    transpose = []

    for i in range(noCols):
        newRow = []
        for j in range(noRows):
            newRow.append(matrix[j][i])
        transpose.append(newRow)
    return transpose

print(transposeMatrix([
    [1, 2, 3],
    [4, 5, 6]
]))