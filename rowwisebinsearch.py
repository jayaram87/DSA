mat = [[1,3,5,7],[10,11,15,17],[22,29,32,45]]

def binsearch(matrix, i, j, m, n, target):
    if i == j-1:
        if martix[i][i] == target:
            return True
        else:
            return False
	elif i > j:
		return False
    else:
        mid = i + (j-i)//2
        mid_element = matrix[mid//n][mid%n]
        if mid_element == target:
            return True
        elif mid_element < target:
            return binsearch(matrix, mid+1, j, m, n, target)
        elif mid_element > target:
            return binsearch(matrix, i, mid-1, m, n, target)
    return False

m = len(mat)
n = len(mat[0])
i = 0
j = m*n-1
print(binsearch(mat, i, j, m, n, 1))