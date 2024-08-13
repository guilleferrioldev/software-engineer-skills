# Prefix array implementation using linked list

from typing import List

class Node:
    """Node implementation"""
    def __init__(self, value: int | float) -> None:
        self.value = value
        self.next = None
        
class PrefixArray:
    """Prefix array implementation using linked list"""
    def __init__(self, values: List[int | float]) -> None:
        self.head = None
        self.__calculate_prefix_array(values)
        
    def __calculate_prefix_array(self, values: List[int | float]) -> None:
        """Create the prefix array"""
        if not values:
            return 
        
        self.head = Node(values[0])
        current = self.head 
        for value in values[1:]:
            new_node = Node(value + current.value)
            current.next = new_node
            current = new_node
            
    def __getitem__(self, index: int) -> int | float:
        """Obtain the sum up to the position entered"""
        if not self.head:
            return
        
        current = self.head 
        count = 0
        while current and count < index:
            current = current.next 
            count += 1
        
        return current.value
            
    def __repr__(self) -> str:
        current = self.head
        result = "["

        while current:
            result += f"{current.value} ,"
            current = current.next
        
        return result[:-2] + "]" if len(result) > 2 else "[0]"

            
            
        
        
        
            
        