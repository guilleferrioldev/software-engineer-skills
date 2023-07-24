#Tree sort 

# Time complexity = O(nlogn)
# Space complexity = O(n)


"""
Tree sort is a sorting algorithm that is based on Binary Search Tree data structure. It first creates a binary search tree from the elements 
of the input list or array and then performs an in-order traversal on the created binary search tree to get the elements in sorted order. 

Algorithm: 
- 1. Take the elements input in an array.
        
- 2. Create a Binary search tree by inserting data items from the array into the binary search tree.

- 3. Perform in-order traversal on the tree to get the elements in sorted order.

"""


class node:
    # BST data structure
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
 
    def insert(self, val):
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = node(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = node(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val

def inorder(root, res):
    # Recursive traversal
    if root:
        inorder(root.left, res)
        res.append(root.val)
        inorder(root.right, res)


def tree_sort(arr):
    # Build BST
    if len(arr) == 0:
        return arr
    root = node(arr[0])
    for i in range(1, len(arr)):
        root.insert(arr[i])
    # Traverse BST in order.
    res = []
    inorder(root, res)
    return res
