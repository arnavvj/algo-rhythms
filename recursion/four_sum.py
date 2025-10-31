"""
Four Number Sum

Implement a function that returns all combinations of four distinct integers from the input array that sum to a given target value.
If no combination exists, return an empty list.
The order of quadruplets and elements inside each quadruplet does not matter.

**Example**
Input:

```python
array = [7, 6, 4, -1, 1, 2]
targetSum = 16
```

Output:

```python
[[7, 6, 4, -1], [7, 6, 1, 2]]
```
"""

def findSubNumberSum(sum_till_now, 
                     targetSum,
                     sub_array,
                     remaining
                    ):

    if remaining == 0:
        if sum_till_now == targetSum:
            return True, [[]]
        else:
            return False, None
                        
    if remaining == len(sub_array):
        if sum_till_now + sum(sub_array) == targetSum:
            return True, [sub_array]
        else:
            return False, None

    elif remaining > len(sub_array):
        return False, None

    else:
        ans = []
        i = 0
        while i < len(sub_array)-remaining+1:
    
            bool_val, temp_ans = findSubNumberSum(sum_till_now + sub_array[i],
                                                 targetSum,
                                                 sub_array[i+1:],
                                                 remaining - 1)

            if bool_val == True:
                for ta in temp_ans:
                    ans.append([sub_array[i]] + ta)

            i+= 1

        if len(ans):
            return True, ans
        else:
            return False, None
                


def fourNumberSum(array, targetSum):
    """
    # 2+ dimensions. Let's say `x`
    # Don't use `x` for loops
    # Try recursion approach

    How to optimize?

    remaining = 4
    for i in range [0, len(array) - remaining]:

        if recurr_func(sum_till_now, targetSum, array[i+1:], remaining - 1) returns True and sub_array:
            return True and [[array[i], *sa] for sa in sub_array]
        else
            retturn False and None

    """
    remaining = 4
    
    if len(array) < remaining:
        return []

    elif len(array) == remaining:
        if sum(array) == targetSum:
            return [array]

    ans = list()
    for i in range(0,len(array)-remaining+1):

        sum_till_now = array[i]
        
        sub_array = array[i+1:]

        bool_val, temp_ans = findSubNumberSum(sum_till_now, 
                                             targetSum,
                                             sub_array,
                                             remaining - 1
                                            )
        
        if bool_val == True:
            for ta in temp_ans:
                ans.append([array[i]] + ta)

    return ans