"""
Split Binary Tree

Implement a function that determines whether a binary tree can be split into two parts with **equal sums** by removing exactly one edge.
If possible, return the sum of each resulting subtree; otherwise, return `0`.

**Example**
Input:

```python
tree = 
        1
       / \
      3  -2
     / \  / \
    6 -5 5  2
   /
  2
```

Output:

```python
6
# Removing the left edge of the root creates two trees,
# both with a total sum of 6.
```
"""

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def level_and_split(node):
    queue = list()
    queue.append(node)


    while len(queue) != 0:
        temp = queue.pop(0)

        if temp.left != None:
            if node.sum == 2 * temp.left.sum:
                return temp.left.sum
            queue.append(temp.left)


        if temp.right != None:
            if node.sum == 2 * temp.right.sum:
                return temp.right.sum
            queue.append(temp.right)

    return 0

def tree_sum(node):
    if node == None:
        return 0

    node.sum = node.value

    left_sum = 0
    if hasattr(node.left, 'sum'):
        left_sum = node.left.sum
    else:
        left_sum = tree_sum(node.left)
    node.sum += left_sum

    right_sum = 0
    if hasattr(node.right, 'sum'):
        right_sum = node.right.sum
    else:
        right_sum = tree_sum(node.right)
    node.sum += right_sum

    return node.sum
    


def splitBinaryTree(tree):
    
    # recursive tree traversal
    # that gets eachnode its sum
    left_sum = 0
    if hasattr(tree.left, 'sum'):
        left_sum = tree.left.sum
    else:
        left_sum = tree_sum(tree.left)
    
    right_sum = 0
    if hasattr(tree.right, 'sum'):
        right_sum = tree.right.sum
    else:
        right_sum = tree_sum(tree.right)
    
    tree.sum = tree.value + left_sum + right_sum

    
    # level order tree traversal
    # find split
    return level_and_split(tree)

    
