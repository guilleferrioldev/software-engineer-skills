# Adjacency lists
"""
An adjacency list representation is based on a linked list. In this, we represent the graph by maintaining a list of neighbors 
(also called an adjacent node) for every vertex (or node) of the graph.

In this representation, all the nodes directly connected to a node x are listed in its adjacent list of nodes. The graph is 
represented by displaying the adjacent list for all the nodes of the graph.
"""



#  Dictionary representation
"""
Using a list for the representation is quite restrictive, because we lack the ability to directly use the vertex labels. 
So, to implement a graph efficiently using Python, a dictionary data structure is used since it is more suitable to represent the graph.
To implement the same graph using a dictionary data structure, we can use the following code snippet:
"""

graph = dict()
graph['A'] = ['B', 'C']
graph['B'] = ['E','C', 'A']
graph['C'] = ['A', 'B', 'E','F']
graph['E'] = ['B', 'C']
graph['F'] = ['C']



# Adjacency matrix
"""
Another approach to representing a graph is to use an adjacency matrix. In this, the graph is represented by showing the nodes and 
their interconnections through edges. Using this method, the dimensions (V x V) of a matrix are used to represent the graph, where each cell
denotes an edge in the graph. A matrix is a two-dimensional array. So, the idea here is to represent the cells of the matrix with a 1 or a 0,
depending on whether two nodes are connected by an edge or not.
"""
def adjacency_matrix(graph):
    # get the key elements by sorting the keys of the graph.
    matrix_elements = sorted(graph.keys())
    #  the length of the keys of the graph will be the dimensions of the adjacency matrix
    cols = rows = len(matrix_elements)
    # create an empty adjacency matrix of the dimensions cols by rows, initially filling all the values with zeros
    adjacency_matrix = [[0 for x in range(rows)] for y in range(cols)]
# variable to store the tuples that form the edges in the graph.
    edges_list = []
   
    for key in matrix_elements:
        for neighbor in graph[key]:
            edges_list.append((key, neighbor))

    for edge in edges_list:
        index_of_first_vertex = matrix_elements.index(edge[0])
        index_of_second_vertex = matrix_elements.index(edge[1])
        adjacency_matrix[index_of_first_vertex][index_of_second_vertex] = 1
    
    return adjacency_matrix
