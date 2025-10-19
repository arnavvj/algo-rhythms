"""
Two-Colorable

Implement a function that checks if an undirected graph (given as an adjacency list) is two-colorable — meaning you can assign one of two colors to each node so that no connected nodes share the same color.
If the graph contains a self-loop, it is automatically not two-colorable.

Example
Input:
edges = [
  [1, 2],
  [0, 2],
  [0, 1]
]
Output: False
# Node 0 connects to both 1 and 2, but 1 and 2 also connect to each other,
# making it impossible to assign only two colors.
"""

def go_explore(edges, vtx, vtx_color, color_map, visited):

    try:
        # if already visited just verify once and move on
        if visited[vtx] == True:
            if color_map[vtx] == vtx_color:
                return True
            else:
                return False
            

    except KeyError: # continue exploration
        
        visited[vtx] = True
        color_map[vtx] = vtx_color

        next_list = edges[vtx]
        for next_v in next_list:
            exptd_next_color = not vtx_color
                
            ans = go_explore(edges, next_v, exptd_next_color, color_map, visited)
            if ans == False:
                return False

        return True


def twoColorable(edges):

    if len(edges) == 1:
        if len(edges[0]) == 0:
            return True
        else:
            return False

    color_map = dict()

    visited = dict()

    start = 0
    start_color = True
    color_map[start] = start_color
    visited[start] = True

    next_list = edges[start]
    for next_v in next_list:
        
        exptd_next_color = not start_color
        ans = go_explore(edges, next_v, exptd_next_color, color_map, visited)

        if ans == False:
            return False

    return True
