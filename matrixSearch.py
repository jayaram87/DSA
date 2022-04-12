matrix = [[1,4,7,11,15], [2,5,8,12,19], [3,6,9,16,22], [10,13,14,17,24], [18,21,23,28,30]]
target = 1

def matsearch(mat, rows, cols, target):
    row = rows - 1
    col = 0
    while row >= 0 and col < cols:
        if mat[row][col] > target:
            row-=1
        elif mat[row][col] < target:
            col+=1
        elif mat[row][col] == target:
            return True
    return False

print(matsearch(matrix, len(matrix), len(matrix[0]), target))