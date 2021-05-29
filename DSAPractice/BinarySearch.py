# [1 3 4 6 8 9] find 8 
def BinarySearch(A, key):
    left = 0
    right = len(A)
    while left <= right:
        mid = int(left + (right - left) / 2)
        if A[mid] == key:
            return mid
        elif A[mid] > key:
            right = mid - 1
        else:
            left = mid + 1
    return "KEY_NOT_FOUND"
print(BinarySearch([1,3,4,6,8,9], 4))