'''
Largest sum of contiguous subarray
consider a sequence of 14 elements [-5, -10, 6, 3, -1, -2, 13, 4, -9, -1, 4, 12, -3, 0]
subsequence sum S(i,j) = sum(arr[k:])

determine the max sum

'''
def maxSum(arr, p, mid, q):
    # O(n/2)+o(n/2)
    max1, max2 = -999999, -999999
    sum1 = 0
    for i in range(mid, p-1, -1):
        sum1 += arr[i]
        if sum1 > max1: max1 = sum1
    sum1 = 0
    for j in range(mid+1, q+1):
        sum1 += arr[j]
        if sum1 > max2: max2 = sum1
    return max(max1, max2, max1+max2)
    
def maxSumSubarray(arr, i, j):
    if i == j:
        return arr[i]
    elif i > j:
        return -1
    else:
        mid = i + (j-i)//2
        # returns max of sum of 2 divided subarrays and the max of the combined 2 subarrays
        # max(arr[0:6], arr[7:13], arr[0:13])
        return max(maxSumSubarray(arr, i, mid), maxSumSubarray(arr, mid+1, j), maxSum(arr, i, mid, j))

arr = [-5, -10, 6, 3, -1, -2, 13, 4, -9, -1, 4, 12, -3, 1]
k = 4
print(maxSumSubarray(arr, 0, len(arr)-1))