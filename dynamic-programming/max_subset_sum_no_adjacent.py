############## description ##############
#                                       #
# maximum sum of non adjacent elements  #
#                                       #
# array = [70, 100, 120, 70, 60, 140]   #
#           ^        ^            ^     #
# ans = 330 => 70 + 120 + 140           #
#                                       #
############### test case ###############


# Write your code here.
def maxSubsetSumNoAdjacent(array):
    if len(array) == 0:
        return 0
    elif len(array) == 1:
        return array[-1]
    elif len(array) == 2:
        return max(array[-2], array[-1])    

    i = len(array) - 1
    max_sum_dict = {
        i: array[i],
        i-1: max(array[i-1], array[i])
    }
    ans = max(float('-inf'), max_sum_dict[i], max_sum_dict[i-1])
    
    i -= 2
    while(i >= 0):
        max_sum_dict[i] = max(array[i] + max_sum_dict[i+2], max_sum_dict[i+1])
        ans = max(ans, max_sum_dict[i])
        i -= 1

    return ans
