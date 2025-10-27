"""
River Sizes

Given a 2D grid of `0`s and `1`s, where `1`s represent river cells, implement a function that finds all rivers and returns their sizes.
Rivers consist of connected `1`s (horizontally or vertically adjacent).
The function should output a list of river sizes in any order.

**Example**
Input:

```python
matrix = [
  [1, 0, 0, 1, 0],
  [1, 0, 1, 0, 0],
  [0, 0, 1, 0, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 1, 0],
]
```

Output:

```python
[1, 2, 2, 2, 5]
```
"""

def explore(matrix,
           curr_length,
           i, j,
           i_max, j_max): 

    # check 4 directions
    # Check N --> i-1, j
    if 0 <= i-1 < i_max and 0 <= j < j_max:
        if matrix[i-1][j] == 1:
            curr_length += 1
            matrix[i-1][j] = 0
            matrix, curr_length = explore(matrix,
                                          curr_length,
                                          i-1, j,
                                          i_max, j_max)
    
    # Check S --> i+1, j
    if 0 <= i+1 < i_max and 0 <= j < j_max:
        if matrix[i+1][j] == 1:
            curr_length += 1
            matrix[i+1][j] = 0
            matrix, curr_length = explore(matrix,
                                          curr_length,
                                          i+1, j,
                                          i_max, j_max)
               
    # Check E --> i, j+1
    if 0 <= i < i_max and 0 <= j+1 < j_max:
        if matrix[i][j+1] == 1:
            curr_length += 1
            matrix[i][j+1] = 0
            matrix, curr_length = explore(matrix,
                                          curr_length,
                                          i, j+1,
                                          i_max, j_max)
               
    # Chest W --> i, j-1
    if 0 <= i < i_max and 0 <= j-1 < j_max:
        if matrix[i][j-1] == 1:
            curr_length += 1
            matrix[i][j-1] = 0
            matrix, curr_length = explore(matrix,
                                          curr_length,
                                          i, j-1,
                                          i_max, j_max)
    

    return matrix, curr_length


def riverSizes(matrix):

    r, c = len(matrix), len(matrix[0])
    ans = []

    # iterate through map and find some "start" point on a river
    for i in range(0, r):
        for j in range(0, c):

            if matrix[i][j] == 1:
                length = 1
                matrix[i][j] = 0
                matrix, total_length = explore(matrix,              # modifiable matrix  
                                               length,              # start with 1
                                               i, j,                # current position 
                                               r, c         # boundary
                                              )
                ans.append(total_length)

            else:
                continue

    return ans
            

    