# Splay Tree implementation using linked list

from typing import Any, List, Self, Tuple
from collections import deque

class Node:
    def __init__(self, value: Any) -> None:
        self.value = value 
        self.parent = None
        self.left = None 
        self.right = None

class SplayTree:
    def __init__(self) -> None:
        self.root = None
        
    def _zig(self, node: Node) -> None: 
        """Right rotation"""
        left = node.left
        node.left = left.right
        
        if left.right != None:
            left.right.parent = node

        left.parent = node.parent
        if node.parent == None:
            self.root = left
        elif node == node.parent.right:
            node.parent.right = left
        else:
            node.parent.left = left

        left.right = node
        node.parent = left
    
    def _zag(self, node: Node) -> None: 
        """Left rotation"""
        right = node.right 
        node.right = right.left
        
        if right.left != None:
            right.left.parent = node
            
        right.parent = node.parent
        if node.parent == None:
            self.root = right
        elif node == node.parent.left:
            node.parent.left = right 
        else:
            node.parent.right = right
        
        right.left = node
        node.parent = right
        
    def _splay(self, node: Node) -> None:
        """Reorganization after performing a search, insertion or deletion of a node in the tree. 
        The expansion function moves the newly accessed node toward the root of the tree 
        through a series of rotations."""
        
        # node is not root
        while node.parent != None:
            # node is child of root, one rotation
            if node.parent.parent == None:
                if node == node.parent.left:
                    self._zig(node.parent)
                else:
                    self._zag(node.parent)

            else:
                parent = node.parent
                grandparent = parent.parent 

                if parent.left == node and grandparent.left == parent:  # both are left children
                    self._zig(grandparent)
                    self._zig(parent)

                elif parent.right == node and grandparent.right == parent:  # both are right children
                    self._zag(grandparent)
                    self._zag(parent)

                elif parent.right == node and grandparent.left == parent:
                    self._zag(parent)
                    self._zig(grandparent)

                elif parent.left == node and grandparent.right == parent:
                    self._zig(parent)
                    self._zag(grandparent)

    def insert(self, value: Any) -> None:
        """Insert a new node"""
        node = Node(value) # New node
        
        y = None
        temp = self.root
        while temp != None:
            y = temp
            if node.value < temp.value:
                temp = temp.left
            else:
                temp = temp.right

        node.parent = y

        if y == None:  # newly added node is root
            self.root = node
        elif node.value < y.value:
            y.left = node
        else:
            y.right = node

        self._splay(node)
        
    def _search(self, data: Any) -> List[Any]:
        node, not_exist = self._search_helper(self.root, data)
        
        if not_exist:
            return 
         
        self._splay(node)
        return node
        
    def _search_helper(self, node: Node, data: Any) -> Node:
        """Auxiliary method search for a node, if it does not exist, the tree is 
        reorganized by the last node that is not null when it is being deleted"""
        if data == node.value:
            return node, False
        
        if data < node.value:
            if not node.left:
                return node, True
            return self._search_helper(node.left, data)
        elif data > node.value:
            if not node.right:
                return node, True
            return self._search_helper(node.right, data)
        
    def __getitem__(self, value: Any) -> bool:
        """Method to see if the element is in the tree"""
        return bool(self._search(value))
    
    def delete(self, data: Any) -> None:
        """Delete the node with the given value"""
        node, last_not_null_node = self._search_helper(self.root, data)
        if last_not_null_node:
            self._splay(node)
            return 
       
        # If the node is leaf or only exists the root
        if not node.left and not node.right:
            if not node.parent:
                self.root = None
                return
            self._delete_leaf(node)
            self._splay(node.parent)    
            
        # If it is an internal node or the root node
        else:
            if node.right:
                minimum = self._find_min(node.right)
                node.value = minimum.value
                self._delete_leaf(minimum) 
            else:
                if not node.parent:
                    self._zig(node)
                    self.root.right = None
                    return 
                maximum = self._find_max(node.left)
                node.value = maximum.value
                self._delete_leaf(maximum) 
            
            self._splay(node)
            
    def _delete_leaf(self, node: Node) -> None:
        if node.value >= node.parent.value:
            node.parent.right = None
        else:
            node.parent.left = None 
    
    def _find_min(self, node: Node) -> Node:
        while node.left:
            node = node.left
        return node
    
    def _find_max(self, node: Node) -> Node:
        while node.right:
            node = node.right
        return node

    def _level_order_traversal(self) -> List[Any]:
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
        return f"{self._level_order_traversal()}"