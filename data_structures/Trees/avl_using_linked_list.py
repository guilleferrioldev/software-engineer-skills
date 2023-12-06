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
        """Method to insert a node"""
        self.root = self._insert(self.root, value)

    def _insert(self, root: Node, value: Any) -> Node:
        """Auxiliar method to insert a node"""
        if not root:
            return Node(value)  # If the tree or subtree is empty, add the new node here
        
        elif value < root.value:  # If the value is less, go to the left subtree
            root.left = self._insert(root.left, value)  # Recursively insert into the left subtree
        
        else:  # If the value is greater, go to the right subtree
            root.right = self._insert(root.right, value)  # Recursively insert into the right subtree

        # Update the height of the current node
        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))

        # Get the balance factor of the node
        balance_factor = self._get_balance_factor(root)

        # Checking for tree imbalance and performing rotations if necessary
        if balance_factor > 1 and value < root.left.value:
            return self._right_rotate(root)  # Right rotation
        
        if balance_factor > 1 and value > root.left.value:
            root.left = self._left_rotate(root.left)
            return self._right_rotate(root)  # Left-Right rotation
        
        if balance_factor < -1 and value > root.right.value:
            return self._left_rotate(root)  # Left rotation
        
        if balance_factor < -1 and value < root.right.value:
            root.right = self._right_rotate(root.right)
            return self._left_rotate(root)  # Right-Left rotation

        return root

    def _get_height(self, root: Node) -> int:
        """Auxiliar method to get the height of a node"""
        if not root:
            return 0  # If the node is empty, its height is 0
        return root.height  # Otherwise return the node's height

    def _get_balance_factor(self, root: Node) -> int:
        """Auxiliar method to get the balnce factor of a node"""
        if not root:
            return 0  # If the node is empty, its balance factor is 0
        return self._get_height(root.left) - self._get_height(root.right)  # The balance factor

    def _left_rotate(self, node: Node) -> Node:
        """Auxiliar method to rotate the tree to the left"""
        right_node = node.right
        left_of_right_node = right_node.left

        # Perform left rotation
        right_node.left = node
        node.right = left_of_right_node

        # Update heights
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        right_node.height = 1 + max(self._get_height(right_node.left), self._get_height(right_node.right))

        return right_node

    def _right_rotate(self, node: Node) -> Node:
        """Auxiliar method to rotate the tree to the right"""
        left_node = node.left
        right_of_left_node = left_node.right

        # Perform right rotation
        left_node.right = node
        node.left = right_of_left_node

        # Update heights
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        left_node.height = 1 + max(self._get_height(left_node.left), self._get_height(left_node.right))

        return left_node
    
    def delete(self, value: Any) -> None:
        """Method to delete a node"""
        self.root = self._delete(self.root, value)

    def _delete(self, root: Node, value: Any) -> Node:
        """Auxiliar method to delete a node"""
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
                    temporal = root.right
                else:
                    temporal = root.left

                # Case of one child or no child
                if not temporal:
                    temporal = root
                    root = None
                else:
                    root = temporal  # Copy the content of the non-empty child

                temporal = None
            else:  # Node with two children: Get the in-order successor
                temporal = self._find_minimum(root.right)

                # Copy the in-order successor's value to the current node
                root.value = temporal.value

                # Delete the in-order successor
                root.right = self._delete(root.right, temporal.value)

        # If the tree had only one node
        if not root:
            return root

        # Step 2: Update the height of the current node
        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))

        # Step 3: Get the balance factor of this node
        balance = self.get_balance(root)

        # Handling imbalance cases and performing rotations if necessary
        if balance > 1:
            if self.get_balance(root.left) >= 0:
                # Left-Left imbalance
                return self._right_rotate(root)
            else:
                # Left-Right imbalance
                root.left = self._left_rotate(root.left)
                return self._right_rotate(root)

        if balance < -1:
            if self.get_balance(root.right) <= 0:
                # Right-Right imbalance
                return self._left_rotate(root)
            else:
                # Right-Left imbalance
                root.right = self._right_rotate(root.right)
                return self._left_rotate(root)

        return root

    def _find_minimum(self, node: Node) -> Node:
        """Auxiliary method to find the minimum"""
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
    
    def __repr__(self) -> str:
        return f"{self.level_order_traversal()}"