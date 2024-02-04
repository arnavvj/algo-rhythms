def swap_child_nodes(node):
    temp = node.left
    node.left = node.right
    node.right = temp

def enqueue_next_level(node, level):
    if node.left != None:
        level.append(node.left)
    if node.right != None:
        level.append(node.right)
    return level

def invertBinaryTree(tree):
    level = [tree]
    while len(level) != 0:
        # get current node
        node = level.pop(0)
        # swap children
        swap_child_nodes(node)
        # add next level
        level = enqueue_next_level(node, level)
        
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
