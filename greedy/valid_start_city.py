"""
Valid Starting City

You’re given two arrays — `distances` and `fuel` — representing a set of cities arranged in a circular route.
Each city `i` has `fuel[i]` gallons available, and the distance to the next city is `distances[i]`.
Your car can travel `mpg` miles per gallon.

Find the **index** of the city where you can start such that you can complete the full circle without running out of fuel.
Exactly one such valid starting city always exists.

**Example**
Input:

```python
distances = [5, 25, 15, 10, 15]
fuel = [1, 2, 1, 0, 3]
mpg = 10
```

Output:

```python
4
```
"""

def check_round_trip(start, distances, fuel_dis):

    num_cities = len(distances)
    i = start
    
    total_dis = 0
    max_dis = 0
    while(True):
        total_dis += distances[i]
        max_dis += fuel_dis[i]

        if max_dis < total_dis:
            return False

        i = (i + 1) % num_cities

        if i == start:
            break

    return True
        


def validStartingCity(distances, fuel, mpg):
    
    contenders = list()
    fuel_dis = list()
    
    for i in range (0, len(distances)):
        if fuel[i] * mpg >= distances[i]:
            contenders.append(i)

        fuel_dis.append(fuel[i] * mpg)
        

    for i, city in enumerate(contenders):
        if check_round_trip(city, distances, fuel_dis):
            return city

    return -1
