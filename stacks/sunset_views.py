"""
Sunset Views

Implement a function that, given an array of building heights and a facing direction ("EAST" or "WEST"), returns the indices of the buildings that can see the sunset.
A building can see the sunset if it’s taller than all buildings that appear after it in the direction it faces.
Return the indices in ascending order.

Example 1
Input:
buildings = [3, 5, 4, 4, 3, 1, 3, 2]
direction = "EAST"
# Visual representation of the input:
#              _
#            _| |
#          _| | |_
#        _| | | | |_
#  (E)  | | | | | | |  (W)
#
Output: [1, 3, 6, 7]

Example 2
Input:
buildings = [3, 5, 4, 4, 3, 1, 3, 2]
direction = "WEST"
Output: [0, 1]
"""

def get_indices_for_east_facing_buildings(buildings):
    l = len(buildings)

    max_height = float('-inf')
    ans = []
    for i in range (l-1, -1, -1):
        if buildings[i] > max_height:
            ans = [i] + ans
            max_height = buildings[i]

    return ans


def sunsetViews(buildings, direction):

    if direction == "EAST":
        return get_indices_for_east_facing_buildings(buildings)

    else:
        temp_ans = get_indices_for_east_facing_buildings(buildings[::-1])
        max_idx = len(buildings)-1
        ans = []
        for i in range(len(temp_ans) - 1, -1, -1):
            ans.append(max_idx - temp_ans[i])
        return ans