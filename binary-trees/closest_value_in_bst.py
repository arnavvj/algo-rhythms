"""
Find Closest Value in BST

Implement a function that takes a Binary Search Tree (BST) and a target integer, and returns the value in the tree that’s closest to the target.
You can assume there’s exactly one closest value.

Each BST node contains a value, and optional left and right children.
A valid BST satisfies these conditions:

A node’s value is greater than all nodes in its left subtree.

A node’s value is less than or equal to all nodes in its right subtree.

Child nodes are either valid BST nodes or None.

Example
Input:
tree =        10
             /  \
            5    15
           / \   / \
          2   5 13 22
         /        \
        1          14

target = 12
Output: 13
"""
def preorder_traversal(node, target, ans, min_diff):

    if node.left == None and node.right == None:
        return node.value, abs(target - node.value)

    ans_left, left_min_diff = None, float('inf')
    if node.left != None:
        ans_left, left_min_diff = preorder_traversal(node.left, target, ans, min_diff)

    
    ans_self, self_min_diff = node.value, abs(target - node.value)

    ans_right, right_min_diff = None, float('inf')
    if node.right != None:
        ans_right, right_min_diff = preorder_traversal(node.right, target, ans, min_diff)

    
    subtree_min_diff = min(min_diff, left_min_diff, self_min_diff, right_min_diff)
    if subtree_min_diff == min_diff:
        return ans, min_diff
    elif subtree_min_diff == left_min_diff:
        return ans_left, left_min_diff
    elif subtree_min_diff == self_min_diff:
        return ans_self, self_min_diff
    elif subtree_min_diff == right_min_diff: 
        return ans_right, right_min_diff


def findClosestValueInBst(tree, target):
    if tree == None:
        return None
    
    min_diff = float('inf')
    ans = None

    ans_left, left_min_diff = preorder_traversal(tree.left, target, ans, min_diff)

    ans_root, root_min_diff = tree.value, abs(target - tree.value)

    ans_right, right_min_diff = preorder_traversal(tree.right, target, ans, min_diff)

    min_diff  = min(left_min_diff, root_min_diff, right_min_diff)

    if min_diff == left_min_diff:
        return ans_left
    elif min_diff == root_min_diff:
        return  ans_root
    elif min_diff == right_min_diff:
        return ans_right


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

