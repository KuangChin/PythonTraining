def InsertionSort(A):
    for i in range(1, len(A)):
        cur = A[i]
        j = i-1
        while j >= 0 and A[j] > cur:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = cur
    return A
print(InsertionSort([3,5,1,4,2,7,9,6,8]))