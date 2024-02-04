# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def lprint(node):
    while (node.next!=None):
        print(node.value, end = ' -> ')
        node = node.next
    print(node.value)

def removeKthNodeFromEnd(head, k):
    print(f"k = {k}")
    lprint(head)
    last = head
    trail = head
    trail_prev = None
    
    for i in range (0,k-1):
        last = last.next

    while (last.next != None):
        last = last.next
        trail_prev = trail
        trail = trail.next

    if trail_prev == None:
        head = trail.next
    else:
        trail_prev.next = trail.next
    del(trail)
    
    lprint(head)
    # return head