"""
Reverse Polish Notation (RPN) Evaluator

Implement a function that evaluates a mathematical expression given in Reverse Polish Notation.
Each operator acts on the two previous operands, and integer division should truncate toward zero.
Supported operators: `+`, `-`, `*`, `/`.

**Example**
Input:

```python
tokens = ["50", "3", "17", "+", "2", "-", "/"]
```

Output:

```python
2
# (50 / ((3 + 17) - 2))
```
"""

def reversePolishNotation(tokens):
    """
    travel the list left to right:
        push if number appears
        if operator appears:
            pop -> pop -> perform -> push

    pop and return ans
    """
    
    stack = list()
    for t in tokens:
        if t == "+":
            stack.append(
                stack.pop() + stack.pop()
            )
        elif t == "-":
            stack.append(
                (-1) * stack.pop() + stack.pop()
            )
        elif t == "*":
            stack.append(
                stack.pop() * stack.pop()
            )
        elif t == "/":
            d = stack.pop()
            n = stack.pop()
            stack.append(int(n/d))
        else:
            # push
            stack.append(int(t))

    ans = stack.pop()
    return ans
