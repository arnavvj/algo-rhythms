def binarySearch(array, target):
    i = 0
    j = len(array) - 1

    while (i<=j):

        mid = int((i + j)/2)

        if array[mid] == target:
            return mid

        elif array[mid] > target: # go left
            j = mid - 1
        
        else: # go right
            i = mid + 1

    return -1