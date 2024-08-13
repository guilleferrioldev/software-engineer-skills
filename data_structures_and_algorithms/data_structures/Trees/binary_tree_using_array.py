# Binary Tree implementation using array

from collections import deque
from typing import Any, List

class BinaryTree:
    """Binary Tree implementation using array"""
    def __init__(self) -> None:
        self.size = 100
        self.array = [None] * self.size
        
    def insert(self, value: Any) -> None:
        """Insert value into"""
        if self.array[0] is None:
            self.array[0] = value
        else:
            self._insert_recursive(value, 0)

    def _insert_recursive(self, value: Any, current_index: int) -> None:
        """Auxiliary method to insert"""
        left_index = 2 * current_index + 1
        right_index = 2 * current_index + 2

        if left_index < self.size and self.array[left_index] is None:
            self.array[left_index] = value
        
        elif right_index < self.size and self.array[right_index] is None:
            self.array[right_index] = value
        
        else:
            self._insert_recursive(value, left_index)

    def search(self, value: Any) -> bool:
        return self._search_recursive(value, 0)

    def _search_recursive(self, value: Any, current_index: int) -> bool:    
        if current_index < self.size and self.array[current_index] is not None:
            if self.array[current_index] == value:
                return True
            left_index = 2 * current_index + 1
            right_index = 2 * current_index + 2
            return self._search_recursive(value, left_index) or self._search_recursive(value, right_index)
        return False
    
    def preorder_traversal(self) -> List[Any]:
        """Method to traverse 'preorder traversal'"""
        traversal_result = []
        self._preorder_recursive(0, traversal_result)
        return traversal_result

    def _preorder_recursive(self, current_index: int, traversal_result: List[Any]) -> None:
        """Auxiliary method to traverse 'preorder traversal'"""
        if current_index < self.size and self.array[current_index] is not None:
            traversal_result.append(self.array[current_index]) 
            left_index = 2 * current_index + 1
            right_index = 2 * current_index + 2
            self._preorder_recursive(left_index, traversal_result) 
            self._preorder_recursive(right_index, traversal_result)
            
    def inorder_traversal(self) -> List[Any]:
        """Method to traverse 'inorder traversal'"""
        traversal_result = []
        self._inorder_recursive(0, traversal_result)
        return traversal_result

    def _inorder_recursive(self, current_index: int, traversal_result: List[Any]) -> None:
        """Auxiliary method to traverse 'inorder traversal'"""
        if current_index < self.size and self.array[current_index] is not None:
            left_index = 2 * current_index + 1
            right_index = 2 * current_index + 2
            self._inorder_recursive(left_index, traversal_result) 
            traversal_result.append(self.array[current_index]) 
            self._inorder_recursive(right_index, traversal_result) 
            
    def postorder_traversal(self) -> List[Any]:
        """Method to traverse 'postorder traversal'"""
        traversal_result = []
        self._postorder_recursive(0, traversal_result)
        return traversal_result

    def _postorder_recursive(self, current_index: int, traversal_result: List[Any]) -> None:
        """Auxiliary method to traverse 'postorder traversal'"""
        if current_index < self.size and self.array[current_index] is not None:
            left_index = 2 * current_index + 1
            right_index = 2 * current_index + 2
            self._postorder_recursive(left_index, traversal_result)  
            self._postorder_recursive(right_index, traversal_result)  
            traversal_result.append(self.array[current_index]) 
            
    def level_order_traversal(self) -> List[Any]:
        """Method to traverse 'level order traversal'"""
        traversal_result = []
        if self.array[0] is None: 
            return traversal_result
        queue = deque([0])  
        while queue:
            current_index = queue.popleft()
            traversal_result.append(self.array[current_index]) 
            left_index = 2 * current_index + 1
            right_index = 2 * current_index + 2
            if left_index < self.size and self.array[left_index] is not None:
                queue.append(left_index)  
            if right_index < self.size and self.array[right_index] is not None:
                queue.append(right_index)  
        return traversal_result
    
    def delete(self, value: Any) -> None:
        """Method to delete nodes"""
        if self.array[0] == value:
            self.array[0] = None
        else:
            self._delete_recursive(value, 0)

    def _delete_recursive(self, value: Any, current_index: int) -> None:
        """Auxiliar method to delete nodes"""
        if current_index < self.size and self.array[current_index] is not None:
            if self.array[current_index] == value:
                left_index = 2 * current_index + 1
                right_index = 2 * current_index + 2
                if left_index < self.size and self.array[left_index] is not None:
                    self.array[current_index] = self.array[left_index]
                    self._delete_recursive(value, left_index)
                elif right_index < self.size and self.array[right_index] is not None:
                    self.array[current_index] = self.array[right_index]
                    self._delete_recursive(value, right_index)
                else:
                    self.array[current_index] = None
            else:
                left_index = 2 * current_index + 1
                right_index = 2 * current_index + 2
                self._delete_recursive(value, left_index)
                self._delete_recursive(value, right_index)