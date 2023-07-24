# Kruskal’s Minimum Spanning Tree algorithm

"""
Kruskal’s algorithm is a widely used algorithm for finding the spanning tree from a given weighted, connected, and undirected graph.
It is based on the greedy approach, as we firstly find the edge with the lowest weight and add it to the tree, and then in each iteration, 
we add the edge with the lowest weight to the spanning tree so that we do not form a cycle. In this algorithm, initially, we treat all the 
vertices of the graph as a separate tree, and then in each iteration we select edge with the lowest weight in such a way that it does not 
form a cycle. These separate trees are combined, and it grows to form a spanning tree. We repeat this process until all the nodes are processed.

The algorithm works as follows:
- 1. Initialize an empty MST (M) with zero edges
- 2. Sort all the edges according to their weights
- 3. For each edge from the sorted list, we add them one by one to the MST (M) in such a way that it does not form a cycle
"""

# Class to represent a graph
class Graph:
    def __init__(self,n):
        self.vertices = n  #number of vertices
        self.graph = []
    
    # Methofd to add an edge to graph
    def add_edge(self,from_vertice,to,weight):
        self.graph.append([from_vertice,to,weight])
    
    # A utility function to find set of an element i
    # (truly uses path compression technique)
    def find(self, parent, i):
        if parent[i] == i:
            return i
        # Reassignment of node's parent
        # to root node as
        # path compression requires
        return self.find(parent,parent[i])
    
    # Method that does union of two sets of x and y
    # (uses union by rank)
    def union(self, parent, rank, a, b):
        a_root = self.find(parent, a)
        b_root = self.find(parent, b)
        # Attach smaller rank tree under root of
        # high rank tree (Union by Rank)
        if rank[a_root] < rank[b_root]:
            parent[a_root] = b_root
        elif rank[a_root] > rank[b_root]:
            parent[b_root] = a_root
        # If ranks are same, then make one as root
        # and increment its rank by one
        else: 
            parent[b_root] = a_root
            rank[a_root] += 1
   
    # The main function to construct MST
    # using Kruskal's algorithm   
    def KruskalMTS(self):
        MST = [] # This will store the resultant MST
        e = 0 # An index variable, used for sorted edges
        r = 0 # An index variable, used for result[]
        
        # Sort all the edges in
        # non-decreasing order of their
        # weight
        self.graph = sorted(self.graph, key = lambda item : item[2]) 
        
        parent = []
        rank = []
        
        # Create V subsets with single elements
        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)
        
        # Number of edges to be taken is less than to V-1
        while r < self.vertices - 1:
            # Pick the smallest edge and increment
            # the index for next iteration
            from_vertice = self.graph[e][0]
            to = self.graph[e][1]
            weight = self.graph[e][2]
            e += 1
            a = self.find(parent, from_vertice)
            b = self.find(parent, to)
            # If including this edge doesn't
            # cause cycle, then include it in result
            # and increment the index of result
            # for next edge
            if a != b:
                r += 1
                MST.append([from_vertice,to,weight])
                self.union(parent, rank, a, b)
            # Else discard the edge
        
        minimumCost = 0
        
        
        print("The edges of the MST are:")
        for from_vertice,to,weight in MST:
            minimumCost += weight
            print(from_vertice,to,weight)
        print("Minimum Spanning Tree", minimumCost)
