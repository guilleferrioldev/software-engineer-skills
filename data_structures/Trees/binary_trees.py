### Binary Trees

# Implementation of tree nodes
class Node:
    def __init__(self,data):
        self.data = data
        self.right_child = None
        self.left_child = None


# Tree traversal
"""
The method to visit all the nodes in a tree is called tree traversal.There are multiple ways to process and traverse the tree that depend upon the
sequence of visiting the root node, left subtree, or right subtree. There are three possible variations of this method, namely, in-order, pre-order, and post-order.

 1- In-oreder traversal
 In-order tree traversal works as follows: we start traversing the left subtree recursively, and once the left subtree is visited, the root node
is visited, and then finally the right subtree is visited recursively. It has the following three steps:
- We start traversing the left subtree and call an ordering function recursively 
- Next, we visit the root nodes 
- Finally, we traverse the right subtree and call an ordering function recursively
"""

def inorder(root_node):
    # Check if the root node is null or empty
    if root_node is None:
        return
    inorder(root_node.left_child)
    print(root_node.data)
    inorder(root_node.right_child)


# Pre-order traversal
"""
Pre-order tree traversal traverses the tree in the order of the root node, the left subtree, and then the right subtree. It works as follows:
- We start traversing with the root node
- Next, we traverse the left subtree and call an ordering function with the left subtree recursively
- Next, we visit the right subtree and call an ordering function with the right subtree recursively
"""

def preorder(root_node):
    if root_node is None:
        return
    print(root_node.data)
    preorder(root_node.left_child)
    preorder(root_node.right_child)


# Post-order traversal
"""
Post-order tree traversal works as follows:
- We start traversing the left subtree and call an ordering function recursively
- Next, we traverse the right subtree and call an ordering function recursively
- Finally, we visit the root node
"""
def postorder(root_node):
    if root_node is None:
        return
    postorder(root_node.left_child)
    postorder(root_node.right_child)
    print(root_node.data)


# Level order traversal
"""
We start by visiting the root of the tree before visiting every node on the next level of the tree. Then, we move on to the next
level in the tree, and so on. This kind of tree traversal is how breadth-first traversal in a graph works, as it broadens the tree
by traversing all the nodes in a level before going deeper into the tree. 

This level-order tree traversal is implemented using a queue data structure. We start by visiting the root node, and we push it into
a queue. The node at the front of the queue is accessed (dequeued), which can then be either printed or stored for later use. After 
adding the root node, the left child node is added to the queue, followed by the right node. Thus, when traversing at any given level
of the tree, all the data items of that level are firstly inserted in the queue from left to right. After that, all the nodes are
visited from the queue one by one. This process is repeated for all the levels of the tree.
"""
        

from collections import deque 

def level_order_traversal(root_node):
    list_of_nodes = []
    traversal_queue = deque([root_node])
    
    while len(traversal_queue) > 0:
        node = traversal_queue.popleft()
        list_of_nodes.append(node.data)
        if node.left_child:
            traversal_queue.append(node.left_child)
            if node.right_child:
                traversal_queue.append(node.right_child)
    return list_of_nodes


"""
# Test 

n1 = Node("root node")
n2 = Node("left child node")
n3 = Node("right child node")
n4 = Node("left grandchild node")

n1.left_child = n2
n1.right_child = n3
n2.left_child = n4


#inorder(n1)
#preorder(n1)
#postorder(n1)
#print(level_order_traversal(n1))
"""




# Expression trees 
"""
An expression tree is a special kind of binary tree that can be used to represent arithmetic expressions. An arithmetic 
expression is represented by a combination of operators and operands, where the operators can be unary or binary

An arithmetic expression can also be represented using a binary tree, which is also known as an expression tree.

The arithmetic expression is shown using three notations: infix, postfix, or prefix.

Prefix notation is commonly referred to as Polish notation.

Postfix, or reverse Polish notation (RPN), places the operator after its operands
"""




# Implementation of Binary tree using arrays
class Tree_Array:

    def __init__(self, tree):
        self.tree = [None] * tree
 
    def root(self, key):
        if self.tree[0] != None:
            print("Tree already had root")
        else:
            self.tree[0] = key
 
 
    def set_left(self, key, parent):
        if self.tree[parent] == None:
            print("Can't set child at", (parent * 2) + 1, ", no parent found")
        else:
            self.tree[(parent * 2) + 1] = key
 
 
    def set_right(self, key, parent):
        if self.tree[parent] == None:
            print("Can't set child at", (parent * 2) + 2, ", no parent found")
        else:
            self.tree[(parent * 2) + 2] = key
 
 
    def print_tree(self):
        for i in range(len(self.tree)):
            if self.tree[i] != None:
                print(self.tree[i], end="")
            else:
                print("-", end="")
        print()

"""
# Example 

tree = Tree_Array(10)
tree.root('A')
tree.set_left('B', 0)
tree.set_right('C', 0)
tree.set_left('D', 1)
tree.set_right('E', 1)
tree.set_right('F', 2)
tree.print_tree()

# Output -> ABCDE-F---
"""

