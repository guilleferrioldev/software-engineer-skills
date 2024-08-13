# Red-Black Tree implementation using linked list

from typing import Any, List
from collections import deque
from enum import Enum

class Color(Enum):
    RED = "red"
    BLACK = "black"

class Node:
    def __init__(self, value: Any) -> None:
        self.value = value
        self.left = None 
        self.right = None 
        self.parent = None
        self.color = Color.RED
        
class RedBlackTree:
    """Red-Black Tree implementation using linked list"""
    def __init__(self) -> None:
        self.NIL = Node(None)
        self.NIL.color = Color.BLACK
        self.root = self.NIL
        
    def insert(self, value: Any) -> None:
        """Method to insert a node"""
        node = Node(value)
        node.left = self.NIL
        node.right = self.NIL

        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if node.value < current.value:
                current = current.left
            else:
                current = current.right

        node.parent = parent
        if not parent:
            self.root = node
        elif node.value < parent.value:
            parent.left = node
        else:
            parent.right = node

        if not node.parent:
            node.color = Color.BLACK
            return

        if not node.parent.parent:
            return

        self._fix_insert(node)
        
    def _fix_insert(self, node: Node) -> None:
        """Auxiliary method to fix the tree when a node was inserted"""
        while node.parent.color == Color.RED:
            if node.parent == node.parent.parent.right:
                uncle = node.parent.parent.left
                if uncle.color == Color.RED:
                    uncle.color = Color.BLACK
                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)
                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    self._left_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.right
                if uncle.color == Color.RED:
                    uncle.color = Color.BLACK
                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)
                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    self._right_rotate(node.parent.parent)
            
            if node == self.root:
                break
        
        self.root.color = Color.BLACK
    
    def _left_rotate(self, node: Node) -> None:
        """Auxiliar method to rotate the tree to the left"""
        right = node.right
        node.right = right.left
        if right.left != self.NIL:
            right.left.parent = node

        right.parent = node.parent
        if not node.parent:
            self.root = right
        elif node == node.parent.left:
            node.parent.left = right
        else:
            node.parent.right = right
        right.left = node
        node.parent = right

    def _right_rotate(self, node: Node) -> None:
        """Auxiliar method to rotate the tree to the right"""
        left = node.left
        node.left = left.right
        if left.right != self.NIL:
            left.right.parent = node

        left.parent = node.parent
        if not node.parent:
            self.root = left
        elif node == node.parent.right:
            node.parent.right = left
        else:
            node.parent.left = left
        left.right = node
        node.parent = left
            
    def delete(self, value: Any) -> None:
        """Method to delete a node"""
        node = self._search_to_delete(value)

        if node == self.NIL:
            return "Key not found!"

        reference_node = node
        reference_node_color = reference_node.color 
        
        if node.left == self.NIL:
            node_that_replaces = node.right 
            self._transplant(node, node.right)
  
        elif node.right == self.NIL:
            node_that_replaces = node.left
            self._transplant(node, node.left)
            
        else:
            reference_node = self._find_minimum(node.right)
            reference_node_color = reference_node.color
            node_that_replaces = reference_node.right 
            
            if reference_node.parent == node:
                node_that_replaces.parent = reference_node
            else:
                self._transplant(reference_node, reference_node.right)
                reference_node.right = node.right
                reference_node.right.parent = reference_node
            
            self._transplant(node, reference_node)
            reference_node.left = node.left 
            reference_node.left.parent = reference_node
            reference_node.color = node.color 
        
        if reference_node_color == Color.BLACK:
            self._delete_fixup(node_that_replaces)
            
    def _search_to_delete(self, value: Any) -> Node:
        """Auxiliar method to search for a node that can be deleted"""
        current = self.root
        while current != self.NIL and value != current.value:
            if value < current.value: 
                current = current.left 
            else:
                current = current.right
        return current
    
    def _transplant(self, replaced_node: Node , node_that_replaces: Node) -> None:
        """Helps us move subtrees within the red-black tree"""
        if not replaced_node.parent: 
            self.root = node_that_replaces
        elif replaced_node == replaced_node.parent.left: 
            replaced_node.parent.left = node_that_replaces   
        else: 
            replaced_node.parent.right = node_that_replaces 
        node_that_replaces.parent = replaced_node.parent 
        
    def _find_minimum(self, node: Node) -> Node:
        """Auxiliary method to find the minimum"""
        while node.left != self.NIL:
            node = node.left
        return node
            
    def _delete_fixup(self, node: Node) -> None:
        """Auxiliary method to fix the tree when a node was deleted"""
        while node != self.root and node.color == Color.BLACK:
            if node == node.parent.left:
                brother = node.parent.right
                
                if brother.color == Color.RED:
                    brother.color = Color.BLACK
                    node.parent.color = Color.RED
                    self._left_rotate(node.parent)
                    brother = node.parent.right
                    
                if brother.left.color == Color.BLACK and brother.right.color == Color.BLACK:
                    brother.color = Color.RED 
                    node = node.parent
                else:
                    if brother.right.color == Color.BLACK:
                        brother.left.color = Color.BLACK
                        brother.color = Color.RED
                        self._right_rotate(brother)
                        brother = node.parent.right 
                        
                    brother.color = node.parent.color 
                    node.parent.color = Color.BLACK
                    brother.right.color = Color.BLACK
                    self._left_rotate(node.parent)
                    node = self.root
                    
            else:
                brother = node.parent.left

                if brother.color == Color.RED:
                    brother.color = Color.BLACK
                    node.parent.color = Color.RED
                    self._right_rotate(node.parent)
                    brother = node.parent.left
                    
                if brother.right.color == Color.BLACK and brother.left.color == Color.BLACK:
                    brother.color = Color.RED
                    node = node.parent
                else:
                    if brother.left.color == Color.BLACK:
                        brother.right.color = Color.BLACK
                        brother.color = Color.RED
                        self._left_rotate(brother)
                        brother = node.parent.Left
                        
                    brother.color = node.parent.color 
                    node.parent.color = Color.BLACK
                    brother.left.color = Color.BLACK
                    self._right_rotate(node.parent)
                    node = self.root
                    
        node.color = Color.BLACK
        
    def level_order_traversal(self) -> List[Any]:
        result = []
        queue = deque()
        
        if self.root:
            queue.append(self.root)
            
        while queue:
            node = queue.popleft()
            if not node.value:
                continue
            
            result.append(node.value)
                        
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        return result
    
    def __repr__(self) -> str:
        return f"{self.level_order_traversal()}" 