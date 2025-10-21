"""
Number of Ways to Traverse Graph

Implement a function that calculates the number of unique ways to move from the top-left corner of a grid to the bottom-right corner.
You may only move **right** or **down** at each step.

For example, for a grid of size `width = 2` and `height = 3`, there are **3 ways** to reach the destination:

```
 _ _
|_|_|
|_|_|
|_|_|
```

Paths:

1. Down, Down, Right
2. Down, Right, Down
3. Right, Down, Down

**Example Input**

```python
width = 4
height = 3
```

** Sample Output**

```python
10
```
"""


def numberOfWaysToTraverseGraph(width, height):
    ans = []

    for h in range(height):
        ans.append([0 for w in range(width)])

    for h in range(1, height):
        ans[h][0] = 1

    for w in range(1, width):
        ans[0][w] = 1

    for h in range(1, height):
        for w in range(1, width):
            ans[h][w] = ans[h-1][w] + ans[h][w-1]

    return ans[-1][-1]
