"""
Three Number Sort

Implement a function that sorts an array in place based on a custom order defined by a separate array of three distinct integers.
The output should group elements according to that order, using constant space.

**Example**
Input:

```python
array = [1, 0, 0, -1, -1, 0, 1, 1]
order = [0, 1, -1]
```

Output:

```python
[0, 0, 0, 1, 1, 1, -1, -1]
```
"""

def threeNumberSort(array, order):
    # Write your code here.

    """
    k = 0 # count of how many times the val appeared for subsequent iters
    
    for val in order:
        
        i = k # i -> popper
        
        while i < length of array:
            
            if array[i] == val:
                k++
                prepend it to the start
                
            else:
                continue

            i ++
    """

    k = 0
    len_arr = len(array)

    for val in order:

        i = k

        while i < len_arr:

            if array[i] == val:
                temp = array.pop(i)
                array = [temp] + array
                k += 1 

            i += 1

    
    return array[::-1]

            
            
