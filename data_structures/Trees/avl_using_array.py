# AVL Tree implementation using array

from collections import deque
from typing import List, Any

class AVLTree:
    """AVL Tree implementation using array"""
    def __init__(self) -> None:
        self.tree = []

    def insert(self, value: Any, index: int = 0) -> None:
        """Insert value into"""
        if index < len(self.tree):
            if value < self.tree[index]:
                self.insert(value, 2 * index + 1)
            else:
                self.insert(value, 2 * index + 2)
        else:
            self.tree += [None] * (index - len(self.tree) + 1)
            self.tree[index] = value
            
            self.rebalance_tree(index)
            
    def rebalance_tree(self, index: int) -> None:
        left_height = self.get_height(2 * index + 1)
        right_height = self.get_height(2 * index + 2)
        balance_factor = left_height - right_height

        if balance_factor > 1:
            if self.tree[index] < self.tree[2 * index + 1]:
                self.rotate_right(2 * index + 1)
            self.rotate_left(index)
        elif balance_factor < -1:
            if self.tree[index] > self.tree[2 * index + 2]:
                self.rotate_left(2 * index + 2)
            self.rotate_right(index)
            
    def get_height(self, index: int) -> int:
        if index < len(self.tree) and self.tree[index] is not None:
            left_height = self.get_height(2 * index + 1)
            right_height = self.get_height(2 * index + 2)
            return max(left_height, right_height) + 1
        else:
            return 0

    def rotate_left(self, index: int = 0) -> None:
        """Method to rotate to the left"""
        temp = self.tree[index]
        self.tree[index] = self.tree[2 * index + 2]
        self.tree[2 * index + 2] = self.tree[2 * (2 * index + 2) + 1]
        self.tree[2 * (2 * index + 2) + 1] = self.tree[2 * index + 1]
        self.tree[2 * index + 1] = temp

    def rotate_right(self, index: int = 0) -> None:
        """Method to rotate to the right"""
        temp = self.tree[index]
        self.tree[index] = self.tree[2 * index + 1]
        self.tree[2 * index + 1] = self.tree[2 * (2 * index + 1) + 2]
        self.tree[2 * (2 * index + 1) + 2] = self.tree[2 * index + 2]
        self.tree[2 * index + 2] = temp
        
    def level_order_traversal(self) -> List[Any]:
        """Method to traverse 'level order traversal'"""
        result = []
        
        if self.tree[0] is None:
            return result
        
        queue = deque([0])
        while queue:
            current_index= queue.popleft()
            result.append(self.tree[current_index])
            left_index = 2 * current_index + 1
            right_index = 2 * current_index + 2 
            if left_index < len(self.tree) and self.tree[left_index] is not None:
                queue.append(left_index)  
            if right_index < len(self.tree) and self.tree[right_index] is not None:
                queue.append(right_index)
        return result
    
    def delete(self, value: Any, index: int = 0) -> None:
        if index < len(self.tree) and self.tree[index] is not None:
            if value == self.tree[index]:
                if self.tree[2 * index + 1] is None and self.tree[2 * index + 2] is None:
                    self.tree[index] = None
                elif self.tree[2 * index + 1] is not None and self.tree[2 * index + 2] is not None:
                    # Caso en el que el nodo a eliminar tiene dos hijos
                    min_right = self.find_min(2 * index + 2)
                    self.tree[index] = min_right
                    self.delete(min_right, 2 * index + 2)
                else:
                    # Caso en el que el nodo a eliminar tiene un solo hijo
                    if self.tree[2 * index + 1] is not None:
                        self.tree[index] = self.tree[2 * index + 1]
                    else:
                        self.tree[index] = self.tree[2 * index + 2]
                self.rebalance_tree(index)
            elif value < self.tree[index]:
                self.delete(value, 2 * index + 1)
            else:
                self.delete(value, 2 * index + 2)

    def find_min(self, index: int) -> Any:
        while self.tree[2 * index + 1] is not None:
            index = 2 * index + 1
        return self.tree[index]
