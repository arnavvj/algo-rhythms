"""
Search In Sorted Matrix

Implement a function that takes a sorted 2D matrix and a target integer, and returns the [row, col] indices where the target appears.
If the target doesn’t exist, return [-1, -1].
Each row and column is sorted in ascending order, but the matrix can have different numbers of rows and columns.

Example
Input:
matrix = [
  [1, 4, 7, 12, 15, 1000],
  [2, 5, 19, 31, 32, 1001],
  [3, 8, 24, 33, 35, 1002],
  [40, 41, 42, 44, 45, 1003],
  [99, 100, 103, 106, 128, 1004],
]
target = 44
Output: [3, 3]
"""

# I have used a binary search approach to solve this problem.
def bin_search(array, i, j, target):
    if i<j:
        
        if array[i] == target:
            return i
        elif array[j] == target:
            return j
        
        # Check if subarray is of length 3 or more
        if i == j+1: 
            return None
        else:
            mid = (i+j)//2
            
            if array[mid] == target:
                return mid
    
            elif array[mid] > target: # go left
                return bin_search(array, i, mid - 1, target)
    
            elif array[mid] < target: # go right
                return bin_search(array, mid + 1, j , target)

    return None

def searchInSortedMatrix(matrix, target):
    
    rows = len(matrix)
    cols = len(matrix[0])

    for r in range(rows):
        if matrix[r][0] == target:
            return [r,0]
        elif matrix[r][cols - 1] == target:
            return [r, cols  - 1]
        elif matrix[r][0] < target < matrix[r][cols - 1]:
            idx = bin_search(matrix[r], 1, cols - 2, target)
            if idx != None:
                return [r, idx]

    return [-1, -1]