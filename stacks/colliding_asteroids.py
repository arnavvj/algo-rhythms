"""
Colliding Asteroids

Implement a function that simulates asteroid collisions.
Each integer in `asteroids` represents an asteroid’s size and direction (`+` = right, `-` = left).
When two collide:

* The smaller one is destroyed.
* If both are equal in size, both explode.
* Asteroids moving in the same direction never meet.

**Example**
Input:

```python
asteroids = [-3, 5, -8, 6, 7, -4, -7]
```

Output:

```python
[-3, -8, 6]
```
"""

def collide(asteroids):
    i = 0
    collision_happened = False
    while (i < len(asteroids) - 1):

        dir_i = -1 if asteroids[i] < 0 else 1
        dir_nxt_i = -1 if asteroids[i+1] < 0 else 1

        # collision happened
        if dir_i == 1 and dir_nxt_i == -1:
            if abs(asteroids[i]) > abs(asteroids[i+1]):
                asteroids.pop(i+1)
            elif abs(asteroids[i]) < abs(asteroids[i+1]):
                asteroids.pop(i)
            else:
                asteroids.pop(i+1)
                asteroids.pop(i)
            collision_happened = True

        # collision did not happen
        else:
            i += 1

    return asteroids, collision_happened


def collidingAsteroids(asteroids):
    """
    # assuming asteroids have non zero speeds

    while collisions happened == True
        find colisions and update the array

        if no collisions this time:
            break and return the asteroids at that iteration
    """

    collision_happened = True

    while collision_happened:

        asteroids, collision_happened = collide(asteroids)

        if not collision_happened:
            break

    return asteroids
