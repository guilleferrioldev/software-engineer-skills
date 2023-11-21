# AVL Tree implementation using linked list

from typing import Any, List
from collections import deque 

class Node:
    """Node implementation"""
    def __init__(self, value: Any) -> None:
        self.value = value
        self.left = None
        self.right = None
        self.height = 1  # Height of the node

class AVLTree:
    """AVL Tree implementation using linked list"""
    def __init__(self) -> None:
        self.root = None  # Initializing AVL tree with no root initially

    def insert(self, value: Any) -> None:
        self.root = self._insert(self.root, value)

    def _insert(self, root: Node, value: Any) -> Node:
        if not root:
            return Node(value)  # If the tree or subtree is empty, add the new node here
        
        elif value < root.value:  # If the value is less, go to the left subtree
            root.left = self._insert(root.left, value)  # Recursively insert into the left subtree
        
        else:  # If the value is greater, go to the right subtree
            root.right = self._insert(root.right, value)  # Recursively insert into the right subtree

        # Update the height of the current node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Get the balance factor of the node
        balance = self.get_balance(root)

        # Checking for tree imbalance and performing rotations if necessary
        if balance > 1 and value < root.left.value:
            return self.right_rotate(root)  # Right rotation
        
        if balance > 1 and value > root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)  # Left-Right rotation
        
        if balance < -1 and value > root.right.value:
            return self.left_rotate(root)  # Left rotation
        
        if balance < -1 and value < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)  # Right-Left rotation

        return root

    def get_height(self, root: Node) -> int:
        if not root:
            return 0  # If the node is empty, its height is 0
        return root.height  # Otherwise return the node's height

    def get_balance(self, root: Node) -> int:
        if not root:
            return 0  # If the node is empty, its balance factor is 0
        return self.get_height(root.left) - self.get_height(root.right)  # The balance factor

    def left_rotate(self, z: Node) -> Node:
        y = z.right
        T2 = y.left

        # Perform left rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def right_rotate(self, y: Node) -> Node:
        x = y.left
        T2 = x.right

        # Perform right rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x
    
    def delete(self, value: Any) -> None:
        self.root = self._delete(self.root, value)

    def _delete(self, root: Node, value: Any) -> Node:
        # Step 1: Perform standard binary search tree deletion
        if not root:
            return root  # If the tree is empty, return null

        if value < root.value:
            root.left = self._delete(root.left, value)  # Recursively delete from the left subtree
        elif value > root.value:
            root.right = self._delete(root.right, value)  # Recursively delete from the right subtree
        else:  # Node to be deleted is found
            if not root.left or not root.right:  # If the node has only one child or no child
                if not root.left:
                    temp = root.right
                else:
                    temp = root.left

                # Case of one child or no child
                if not temp:
                    temp = root
                    root = None
                else:
                    root = temp  # Copy the content of the non-empty child

                temp = None
            else:  # Node with two children: Get the in-order successor
                temp = self.getMinValueNode(root.right)

                # Copy the in-order successor's value to the current node
                root.value = temp.value

                # Delete the in-order successor
                root.right = self._delete(root.right, temp.value)

        # If the tree had only one node
        if not root:
            return root

        # Step 2: Update the height of the current node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Step 3: Get the balance factor of this node
        balance = self.get_balance(root)

        # Handling imbalance cases and performing rotations if necessary
        if balance > 1:
            if self.get_balance(root.left) >= 0:
                # Left-Left imbalance
                return self.right_rotate(root)
            else:
                # Left-Right imbalance
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        if balance < -1:
            if self.get_balance(root.right) <= 0:
                # Right-Right imbalance
                return self.left_rotate(root)
            else:
                # Right-Left imbalance
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root

    def getMinValueNode(self, node: Node) -> Node:
        current = node
        while current.left:
            current = current.left
        return current  
            
    def level_order_traversal(self) -> List[Any]:
        result = []
        queue = deque()
        
        if self.root:
            queue.append(self.root)
            
        while queue:
            node = queue.popleft()
            result.append(node.value)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        return result