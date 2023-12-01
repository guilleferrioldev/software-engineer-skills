# Red-Black Tree implementation using linked list

from typing import Any, List
from collections import deque

class Node:
    def __init__(self, value: Any) -> None:
        self.value = value
        self.left = None 
        self.right = None 
        self.parent = None
        self.color = "red"
        
class RedBlackTree:
    def __init__(self) -> None:
        self.NIL = Node(None)
        self.NIL.color = "black"
        self.root = self.NIL
        
    def insert(self, value: Any) -> None:
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
            node.color = "black"
            return

        if not node.parent.parent:
            return

        self.fix_insert(node)
        
    def fix_insert(self, node: Node) -> None:
        while node.parent.color == "red":
            if node.parent == node.parent.parent.right:
                parent_sibling = node.parent.parent.left
                if parent_sibling.color == "red":
                    parent_sibling.color = "black"
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.left_rotate(node.parent.parent)
            else:
                parent_sibling = node.parent.parent.right
                if parent_sibling.color == "red":
                    parent_sibling.color = "black"
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.right_rotate(node.parent.parent)
            
            if node == self.root:
                break
        
        self.root.color = "black"
        
    def left_rotate(self, node: Node) -> None:
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

    def right_rotate(self, node: Node) -> None:
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
    
tree = RedBlackTree()
tree.insert(10)
tree.insert(18)
tree.insert(7)
tree.insert(15)
tree.insert(16)
tree.insert(30)
tree.insert(25)
tree.insert(40)
tree.insert(60)
tree.insert(2)
tree.insert(1)
tree.insert(70)
print(tree)    