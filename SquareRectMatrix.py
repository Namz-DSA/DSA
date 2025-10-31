def SquareRect(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    if rows == cols:
        print("Square Matrix")
    else:
        print("Rectangle Matrix")

SquareRect([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

SquareRect([
    [1,2,3],
    [4,5,6]
])