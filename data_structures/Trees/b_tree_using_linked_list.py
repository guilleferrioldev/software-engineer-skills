from collections import deque
from typing import List

class Node:
    def __init__(self, leaf = True) -> None:
        self.leaf = leaf
        self.keys = []
        self.children  = []
        
class BTree:
    def __init__(self, degree: int) -> None:
        self.degree = degree 
        self.root = None
        
    def insert(self, key: int | float) -> None:
        if not self.root:
            self.root = Node(True)
            self.root.keys.append(key)
        else:
            if len(self.root.keys) == (2 * self.degree) - 1:
                new_root = Node()
                new_root.children.append(self.root)
                self._split_child(new_root, 0)
                self.root = new_root
            self._insert_non_full(self.root, key)
            
    def _insert_non_full(self, node: Node, key: int | float) -> None:
        """Auxiliary function used in the implementation of insertion in a B-tree. This function 
        is called recursively to insert a new key into a node that is not full, that is, has fewer
        keys than allowed according to the B-tree rules."""
        i = len(node.keys) - 1
        if node.leaf:
            node.keys.append(0)
            while i >= 0 and key < node.keys[i]:
                node.keys[i+1] = node.keys[i]
                i -= 1
            node.keys[i+1] = key
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2 * self.degree) - 1:  
                self.split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self.insert_non_full(node.children[i], key)
            
    def _split_child(self, parent: Node, index: int) -> None:
        degree = self.degree
        child = parent.children[index]
        new_child = Node(child.leaf)
        parent.keys.insert(index, child.keys[degree - 1])
        parent.children.insert(index + 1, new_child)
        new_child.keys = child.keys[degree: (2 * degree) - 1]
        child.keys = child.keys[0: degree - 1]
        if not child.leaf:
            new_child.children = child.children[degree: 2 * degree]
            child.children = child.children[0: degree - 1]
            
    def search(self, key, node=None):
        if node is None:
            node = self.root
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and key == node.keys[i]:
            return True
        elif node.leaf:
            return False
        else:
            return self.search(key, node.children[i])
        
    def delete(self, key):
        if self.root is None:
            return 
        else:
            self.delete_recursive(self.root, key)
    
    def delete_recursive(self, node, key):
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        
        if i < len(node.keys) and key == node.keys[i]:  # Caso 1: La clave está en el nodo actual
            if node.leaf:
                del node.keys[i]
            else:
                # Caso 2: La clave está en un nodo interno
                key_to_swap = self.find_predecessor(node, i)
                node.keys[i] = key_to_swap
                self.delete_recursive(node.children[i], key_to_swap)
        else:
            if node.leaf:
                return False
            else:
                # Caso 4: La clave está en un nodo interno
                if len(node.children[i].keys) < self.degree:  # Necesitamos asegurarnos de que el nodo tiene al menos t claves
                    self.borrow_or_merge(node, i)
                if i > len(node.keys):  # Determinar en qué subárbol continuar la búsqueda
                    i -= 1
                self.delete_recursive(node.children[i], key)
    
    def find_predecessor(self, node, i):
        current = node.children[i]
        while not current.leaf:
            current = current.children[len(current.keys)]
        return current.keys[-1]
    
    def borrow_or_merge(self, parent, index):
        if index != 0 and len(parent.children[index-1].keys) >= self.degree:
            # Borrow from left sibling
            self.borrow_from_left(parent, index)
        elif index != len(parent.children) - 1 and len(parent.children[index+1].keys) >= self.degree:
            # Borrow from right sibling
            self.borrow_from_right(parent, index)
        else:
            # Merge with a sibling
            self.merge_with_sibling(parent, index)

    def borrow_from_left(self, parent, index):
        child = parent.children[index]
        left_sibling = parent.children[index-1]
        child.keys.insert(0, parent.keys[index-1])
        parent.keys[index-1] = left_sibling.keys.pop()
        if not left_sibling.leaf:
            child.children.insert(0, left_sibling.children.pop())
    
    def borrow_from_right(self, parent, index):
        child = parent.children[index]
        right_sibling = parent.children[index+1]
        child.keys.append(parent.keys[index])
        parent.keys[index] = right_sibling.keys.pop(0)
        if not right_sibling.leaf:
            child.children.append(right_sibling.children.pop(0))

    def merge_with_sibling(self, parent, index):
        child = parent.children[index]
        right_sibling = parent.children[index+1]
        child.keys.append(parent.keys.pop(index))
        child.keys.extend(right_sibling.keys)
        if not right_sibling.leaf:
            child.children.extend(right_sibling.children)
        del parent.children[index+1]
        
        
    def level_order_traversal(self) -> List:
        if self.root is None:
            return 

        result = []
        queue = deque([self.root])

        while queue:
            level_result = []
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                level_result.extend(node.keys)

                if not node.leaf:
                    queue.extend(node.children)

            result.append(level_result)

        return result
    
    def __repr__(self) -> str:
        return f"{self.level_order_traversal()}"