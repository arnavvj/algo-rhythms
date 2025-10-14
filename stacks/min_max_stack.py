"""
Min Max Stack Construction

Implement a MinMaxStack class that supports constant-time operations for:

pushing and popping elements,

checking the top element, and

retrieving both the current minimum and maximum values in the stack.

Each method should be efficient and operate in O(1) time and O(1) additional space.

Example Usage

# All operations below are performed sequentially.
MinMaxStack()   # instantiate a MinMaxStack

push(5)
getMin()  # 5
getMax()  # 5
peek()    # 5

push(7)
getMin()  # 5
getMax()  # 7
peek()    # 7

push(2)
getMin()  # 2
getMax()  # 7
peek()    # 2

pop()     # 2
pop()     # 7
getMin()  # 5
getMax()  # 5
peek()    # 5
"""

# Feel free to add new properties and methods to the class.
class MinMaxStack:

    def __init__(self):
        self.stack = list()
        self.max_stack = list()
        self.min_stack = list()
    
    def peek(self):
        # Write your code here.
        try:
            return self.stack[-1]
        except IndexError:
            return None
        
    def pop(self):
        try:
            ans = self.stack.pop(-1)

            if ans == self.max_stack[-1]:
                self.max_stack.pop(-1)
            if ans == self.min_stack[-1]:
                self.min_stack.pop(-1)
            
        except IndexError:
            ans = None

        print(self.stack)
        print(self.min_stack)
        print(self.max_stack)
        
        return ans

    def push(self, number):
        # Write your code here.
        self.stack.append(number)

        try:
            if number >= self.max_stack[-1]:
                self.max_stack.append(number)
        except IndexError:
            self.max_stack.append(number)

        try:
            if number <= self.min_stack[-1]:
                self.min_stack.append(number)
        except IndexError:
            self.min_stack.append(number)

        print(self.stack)
        print(self.min_stack)
        print(self.max_stack)
        

    def getMin(self):
        try:
            return self.min_stack[-1]
        except IndexError:
            return None

    def getMax(self):
        try:
            return self.max_stack[-1]
        except IndexError:
            return None
