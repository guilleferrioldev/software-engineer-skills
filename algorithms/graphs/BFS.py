# BFS

"""
Breadth-first search (BFS) works very similarly to how a level order traversal algorithm works in a tree data structure.
The BFS algorithm also works level by level; it starts by visiting the root node at level 0, and then all the nodes at the
first level directly connected to the root node are visited at level 1. The level 1 node has a distance of 1 from the root
node. After visiting all the nodes at level 1, the level 2 nodes are visited next. Likewise, all the nodes in the graph are
traversed level by level until all the nodes are visited. So, breadth-first traversal algorithms work breadthwise in the graph.

A queue data structure is used to store the information of vertices that are to be visited in a graph. We begin with the
starting node. Firstly, we visit that node, and then we look up all of its neighboring, or adjacent, vertices. We first visit 
these adjacent vertices one by one, while adding their neighbors to the list of vertices that are to be visited. We follow this
process until we have visited all the vertices of the graph, ensuring that no vertex is visited twice.
"""

# Time complexity = O(n)
# Space complexity = O(n)

from collections import deque

def breadth_first_search(graph, root):
    visited_vertices = list()
    graph_queue = deque([root])
    visited_vertices.append(root)
    node = root

    while len(graph_queue) > 0:
        node = graph_queue.popleft()
        adj_nodes = graph[node]
        remaining_elements = set(adj_nodes).difference(set(visited_vertices))
        
        if len(remaining_elements) > 0:
            for elem in sorted(remaining_elements):
                visited_vertices.append(elem)
                graph_queue.append(elem)
    
    return visited_vertices
