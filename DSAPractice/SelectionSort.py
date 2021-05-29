def SelectionSort(A):
    for i in range(len(A)):
        cur = A[i]
        j=i
        min = A[j]
        while j < len(A):
            if A[j] < min:
                min = A[j]
                min_p = j
            j += 1 
        if min != cur:
            A[min_p] = cur
            A[i] = min
        print(A)
    return A
SelectionSort([7,8,5,2,4,6,3])