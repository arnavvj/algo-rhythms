"""
Task Assignment

Implement a function that assigns pairs of tasks to `k` workers so that the time to finish all tasks is minimized.
Each worker must complete two unique tasks, and all tasks are worked on in parallel.
The total time to finish equals the duration of the **longest task pair**.

Return the task index pairs `[task1, task2]`.
If multiple optimal assignments exist, any correct one is fine.

**Example**
Input:

```python
k = 3
tasks = [1, 3, 5, 3, 1, 4]
```

Output:

```python
[[0, 2], [4, 5], [1, 3]]
# Longest pair time = 6
```
"""

def taskAssignment(k, tasks):
  sorted_tasks = sorted(
        enumerate(tasks), 
        key=lambda x: x[1]
    )

  ans = [
    [sorted_tasks[i][0], sorted_tasks[-i - 1][0]]
    for i in range(k)
  ]

  return ans