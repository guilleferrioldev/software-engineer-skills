# DFS
"""
Depth-first search (DFS) or traversal algorithm traverses the graph similar to how the preorder traversal algorithm works in trees. 
In the DFS algorithm, we traverse the tree in the depth of any particular path in the graph. As such, child nodes are visited first
before sibling nodes.

In this, we start with the root node; firstly we visit it, and then we see all the adjacent vertices of the current node. We start 
visiting one of the adjacent nodes. If the edge leads to a visited node,we backtrack to the current node. And, if the edge leads to 
an unvisited node, then we go to that node and continue processing from that node. We continue the same process until we reach a dead 
end when there is no unvisited node; in that case, we backtrack to previous nodes, and we stop when we reach the root node while backtracking
"""

# Time complexity = O(V+E)
# Space complexity = O(V)


def depth_first_search(graph, root):
    visited_vertices = list()
    graph_stack = list()
    graph_stack.append(root)
    node = root

    while graph_stack:
        if node not in visited_vertices:
            visited_vertices.append(node)
        adj_nodes = graph[node]
        if set(adj_nodes).issubset(set(visited_vertices)):
            graph_stack.pop()
            if len(graph_stack) > 0:
                node = graph_stack[-1]
            continue
        else:
            remaining_elements = set(adj_nodes).difference(set(visited_vertices))
        
        first_adj_node = sorted(remaining_elements)[0]
        graph_stack.append(first_adj_node)
        node = first_adj_node
    
    return visited_vertices
