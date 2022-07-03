'''
Finding the kth smallest element in an array
Given an array arr of n elements and a positive integer k, find the kth smallest element in the array
It is a given that all elements in the array are distinct

(divide and conquer approach)

eg:
arr = [10, 3, 7, 13, 23, 15, 46, 24], k = 4
op = 13
'''

def partition(arr, p, q):
    pivot = arr[p]
    i = p
    for j in range(p+1, q+1):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i], arr[p] = arr[p], arr[i]
    return i

def selectionProcedure(arr, p, q, k):
    if p == q:
        return arr[p]
    elif p>q:
        return -1
    else:
        pivot_index = partition(arr, p, q)
        if pivot_index == k-1:
            return arr[k-1]
        elif pivot_index > k-1:
            return selectionProcedure(arr, p, pivot_index-1, k)
        else:
            return selectionProcedure(arr, pivot_index+1, q, k)



arr = [10, 3, 7, 13, 23, 15, 46, 24]
k = 4
print(selectionProcedure(arr, 0, len(arr)-1, k))