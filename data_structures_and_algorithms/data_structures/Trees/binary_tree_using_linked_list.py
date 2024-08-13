# Binary Tree implementation using linked list 

from typing import Any , List
from collections import deque

class Node:
    """Node implementation"""
    def __init__(self, value: Any) -> None:
        self.value = value
        self.left = None 
        self.right = None
    
class BinaryTree:
    """Binary Tree implementation using linked list """
    def __init__(self, values: List[Any] | Any = None, *more_values) -> None:
        self.root = None
        
        if len(more_values) > 0:
            values = (values,) + more_values
        
        if values:
            for value in values:
                self.insert(value)
        
    def insert(self, value):
        """Insert value into"""
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, current_node: Node, value: Any) -> None:
        """Auxiliary method to insert"""
        new_node = Node(value)
        
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self._insert_recursive(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self._insert_recursive(current_node.right, value)
                
    def search(self, value: Any) -> bool:
        """Method to know if a value exist in the tree"""
        return self._search_recursively(self.root, value)

    def _search_recursively(self, current_node: Node, value: Any) -> bool:
        """Auxiliary method to search"""
        if current_node is None:
            return False

        if current_node.value == value:
            return True
        elif value < current_node.value:
            return self._search_recursively(current_node.left, value)
        else:
            return self._search_recursively(current_node.right, value)
    
    def preorder_traveral(self) -> List[Any]:
        """Method to traverse 'preorder traversal'"""
        result = []
        self._preorder_traversal_recursive(self.root, result)
        return result    

    def _preorder_traversal_recursive(self, current_node: Node, result: List[Any])-> None:
        """Auxiliary method to traverse 'preorder traversal'"""
        if current_node:
            result.append(current_node.value)
            self._preorder_traversal_recursive(current_node.left, result)
            self._preorder_traversal_recursive(current_node.right, result)
             
    def inorder_traversal(self) -> List[Any]:
        """Method to traverse 'inorder traversal'"""
        result = []
        self._inorder_traversal_recursive(self.root, result)
        return result        
    
    def _inorder_traversal_recursive(self, current_node: Node, result: List[Any])-> None:
        """Auxiliary method to traverse 'inorder traversal'"""
        if current_node:
            self._inorder_traversal_recursive(current_node.left, result)
            result.append(current_node.value)
            self._inorder_traversal_recursive(current_node.right, result)
            
    def postorder_traveral(self) -> List[Any]:
        """Method to traverse 'postorder traversal'"""
        result = []
        self._postorder_traversal_recursive(self.root, result)
        return result    

    def _postorder_traversal_recursive(self, current_node: Node, result: List[Any])-> None:
        """Auxiliary method to traverse 'postorder traversal'"""
        if current_node:
            self._postorder_traversal_recursive(current_node.left, result)
            self._postorder_traversal_recursive(current_node.right, result)
            result.append(current_node.value)
            
    def level_order_traversal(self): # BFS
        """Method to traverse 'level order traversal'"""
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
            
    def delete(self, value: Any) -> None:
        """Method to delete nodes"""
        self.root = self._delete_recursively(self.root, value)
        
    def _delete_recursively(self, current_node: Node, value: Any):
        """Auxiliar method to delete nodes"""
        if current_node is None:
            return current_node 
        
        if value < current_node.value:
            current_node.left = self._delete_recursively(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self._delete_recursively(current_node.right, value)
        else:
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left
            #The in-order successor (the smallest value in the right subtree) is found, its value is copied 
            # to the current node, and then the in-order successor is deleted.
            temp = self._find_min(current_node.right)
            current_node.value = temp.value
            current_node.right = self._delete_recursively(current_node.right, temp.value)
        
        return current_node
            
    def _find_min(self, node: Node) -> Node:
        """Auxiliar method to find the in-order successor (the smallest value in the right subtree)"""
        current = node
        while current.left is not None:
            current = current.left
        return current
