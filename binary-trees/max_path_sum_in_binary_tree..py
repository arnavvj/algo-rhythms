############ example ############
#                               #
#  nodes marked with `*` give   #
#  maximum path sum             #
#                               #
#                               #
#  tree/node                    #
#  |---- value                  #
#  |---- left                   #
#  |---- right                  #
#                               #
#                               #
#  test case:                   #
#                               #
#            -1  <--- tree      #
#            / \                #
#           /   \               #
#          /     \              #
#        -9       3*            #
#        / \     / \            #
#       /   \   /   \           #
#      4     5 6*    7*         #
#                   / \         #
#                  /   \        #
#                 1*   -1       #
#                               #
################################# 


class TreeProc:
    def __init__(self):
        self.ans = float('-inf')
        self.max_sum_till_node = {
            None: float('-inf')     # None: for terminating condition 
        }

    def recurr_sum(self, node):
        try:
            max_sum_till_left_child = self.max_sum_till_node[node.left]
        except KeyError:
            self.recurr_sum(node.left)
            max_sum_till_left_child = self.max_sum_till_node[node.left]
        
        try:
            max_sum_till_right_child = self.max_sum_till_node[node.right]
        except KeyError:
            self.recurr_sum(node.right)
            max_sum_till_right_child = self.max_sum_till_node[node.right]
        
        self.max_sum_till_node[node] = max(
            node.value, 
            node.value + max_sum_till_left_child,
            node.value + max_sum_till_right_child
        )
        
        self.ans = max(
            self.ans,
            self.max_sum_till_node[node],
            node.value + max_sum_till_left_child + max_sum_till_right_child
        )

def maxPathSum(tree):
    if tree == None:
        return None

    tp = TreeProc()
    tp.recurr_sum(tree)
    return tp.ans