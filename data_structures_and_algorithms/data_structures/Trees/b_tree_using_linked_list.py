from collections import deque
from typing import List, Any

class Node:
    def __init__(self, leaf = True) -> None:
        self.leaf = leaf
        self.keys = []
        self.children  = []
        
class BTree:
    def __init__(self, degree: int) -> None:
        self.degree = degree 
        self.root = None
        
    def insert(self, key: Any) -> None:
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
            
    def _insert_non_full(self, node: Node, key: Any) -> None:
        """Auxiliary function used in the implementation of insertion in a B-tree. This function 
        is called recursively to insert a new key into a node that is not full, that is, has fewer
        keys than allowed according to the B-tree rules."""
        index = len(node.keys) - 1
        if node.leaf:
            node.keys.append(0)
            while index >= 0 and key < node.keys[index]:
                node.keys[index + 1] = node.keys[index]
                index -= 1
            node.keys[index + 1] = key
        else:
            while index >= 0 and key < node.keys[index]:
                index -= 1
            index += 1
            if len(node.children[index].keys) == (2 * self.degree) - 1:  
                self.split_child(node, i)
                if key > node.keys[index]:
                    index += 1
            self.insert_non_full(node.children[index], key)
            
    def _split_child(self, parent: Node, index: int) -> None:
        child = parent.children[index]
        new_child = Node(child.leaf)
        parent.keys.insert(index, child.keys[self.degree - 1])
        parent.children.insert(index + 1, new_child)
        new_child.keys = child.keys[self.degree: (2 * self.degree) - 1]
        child.keys = child.keys[0: self.degree - 1]
        if not child.leaf:
            new_child.children = child.children[self.degree: 2 * self.degree]
            child.children = child.children[0: self.degree - 1]
            
    def search(self, key: Any , node: Node = None) -> bool:
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
        
    def delete(self, key: Any) -> None:
        if self.root is None:
            return 
        else:
            self.delete_recursive(self.root, key)
    
    def delete_recursive(self, node: Node, key: Any) -> Non:
        index = 0
        while index < len(node.keys) and key > node.keys[index]:
            index += 1
        
        if index < len(node.keys) and key == node.keys[index]:  # Case 1: The key is on the current node
            if node.leaf:
                del node.keys[index]
            else:
                # Case 2: The key is on an internal node
                key_to_swap = self.find_predecessor(node, index)
                node.keys[index] = key_to_swap
                self.delete_recursive(node.children[index], key_to_swap)
        else:
            if node.leaf:
                return False
            else:
                # Case 4: The key is on an internal node
                if len(node.children[index].keys) < self.degree:  # We need to ensure that the node has at least t keys
                    self.borrow_or_merge(node, index)
                if index > len(node.keys):  # Determine which subtree to continue searching in
                    index -= 1
                self.delete_recursive(node.children[index], key)
    
    def find_predecessor(self, node: Node, index: int) -> Any:
        current = node.children[index]
        while not current.leaf:
            current = current.children[len(current.keys)]
        return current.keys[-1]
    
    def borrow_or_merge(self, parent: Node, index: int) -> None:
        if index != 0 and len(parent.children[index - 1].keys) >= self.degree:
            # Borrow from left sibling
            self.borrow_from_left(parent, index)
        elif index != len(parent.children) - 1 and len(parent.children[index+1].keys) >= self.degree:
            # Borrow from right sibling
            self.borrow_from_right(parent, index)
        else:
            # Merge with a sibling
            self.merge_with_sibling(parent, index)

    def borrow_from_left(self, parent: Node, index: int) -> None:
        child = parent.children[index]
        left_sibling = parent.children[index-1]
        child.keys.insert(0, parent.keys[index-1])
        parent.keys[index-1] = left_sibling.keys.pop()
        if not left_sibling.leaf:
            child.children.insert(0, left_sibling.children.pop())
    
    def borrow_from_right(self, parent: Node, index: int) -> None:
        child = parent.children[index]
        right_sibling = parent.children[index+1]
        child.keys.append(parent.keys[index])
        parent.keys[index] = right_sibling.keys.pop(0)
        if not right_sibling.leaf:
            child.children.append(right_sibling.children.pop(0))

    def merge_with_sibling(self, parent: Node, index: int) -> None:
        child = parent.children[index]
        right_sibling = parent.children[index+1]
        child.keys.append(parent.keys.pop(index))
        child.keys.extend(right_sibling.keys)
        if not right_sibling.leaf:
            child.children.extend(right_sibling.children)
        del parent.children[index+1]
        
    def _print_helper(self, node: Node, level: int = 0, result = []):
        if node:
            result.append((level, node.keys))
            for child in node.children:
                self._print_helper(child, level + 1)

        return result
    
    def __repr__(self) -> str:
        result = self._print_helper(self.root)
        return f"{result}"