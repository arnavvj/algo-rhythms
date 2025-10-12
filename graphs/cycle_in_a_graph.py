"""
Cycle in Graph

Implement a function that determines whether a directed graph (given as an adjacency list) contains a cycle.
Each index in the list represents a vertex, and each sub-list contains the vertices it points to.
A cycle is any path where the traversal eventually returns to the starting vertex — self-loops count as valid cycles.

Example
Input:
edges = [
  [1, 3],
  [2, 3, 4],
  [0],
  [],
  [2, 5],
  [],
]
Output: True
# Example cycles:
# 0 → 1 → 2 → 0
# 1 → 4 → 2 → 0 → 1
# ...
"""

def is_there_a_cycle_from_vertex(v, edges, visited):

    for next_v in edges[v]:

        try:
            if visited[next_v] == True:
                return True

        except KeyError:
            visited[next_v] = True
            
            cycle_present = is_there_a_cycle_from_vertex(next_v, edges, visited)
            
            if cycle_present:
                return True
            else:
                visited[next_v] = False

    return False
        


def cycleInGraph(edges):
    
    for v, edge_list in enumerate(edges): # go through all vertices
        
        visited = dict()
        visited[v] = True

        for next_v in edge_list: # depth first search

            visited[next_v] = True
            cycle_present = is_there_a_cycle_from_vertex(next_v, edges, visited) 
    
            if cycle_present:
                return True
            else:
                visited[next_v] = False

    return False