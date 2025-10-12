"""
Permutations

Implement a function that, given an array of distinct integers, returns all possible permutations of the array (order doesn’t matter).
Edge case: if the input is empty, return an empty array.

Example
Input: array = [1, 2, 3]
Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
"""

def all_possible_combos(array):

    if len(array) == 2:
        return ([
            array,
            [array[1], array[0]]
        ])
    
    ans = []
    for idx, num in enumerate(array):
        
        subset_combos = all_possible_combos(array[ : idx] + array[idx + 1 : ])

        for sc in subset_combos:
            ans.append([num] + sc)

    return ans
    
    


def getPermutations(array):

    if len(array) == 0:
        return array

    elif len(array) == 1:
        return [array]

    elif len(array) == 2:
        return ([
            array,
            [array[1], array[0]]
        ])

    ans = []
    for idx, num in enumerate(array):
        
        subset_combos = all_possible_combos(array[ : idx] + array[idx + 1 : ])

        for sc in subset_combos:
            ans.append([num] + sc)

    return ans