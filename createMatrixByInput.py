def createMatrixByInput(m,n):
    matrix = []
    for i in range(m):
      row = []
      for j in range(n):
         row.append(j+1 + i * n)
      matrix.append(row)
    return matrix
print(createMatrixByInput(2,3))