# Bidirectional prefix array implementation using linked list

from typing import List

class Node:
    """Node implementation"""
    def __init__(self, value: int | float) -> None:
        self.value = value 
        self.next = None 

class BidirectionalPrefixArray:
    """Bidirectional prefix array implementation using linked list"""
    def __init__(self, array: List[int | float]) -> None:
        self.forward_head = None
        self.backwrd_head = None
        self.calculate_prefix_array_forward(array)
        self.calculate_prefix_array_backward(array)
        self.count = len(array)
       
    def calculate_prefix_array_forward(self, array: List[int | float]) -> None:
        """Create forward prefix array"""
        if not array:
            return 
        
        self.forward_head = Node(array[0])
        current = self.forward_head
        for index in range(1, len(array)):
            new_node = Node(array[index] + current.value)
            current.next = new_node
            current = new_node
            
    def calculate_prefix_array_backward(self, array: List[int | float]) -> None:
        """Create backward prefix array"""
        if not array:
            return 
        
        self.backward_head = Node(array[-1])
        current = self.backward_head
        for index in range(len(array) -2, -1, -1):
            new_node = Node(array[index] + current.value)
            current.next = new_node
            current = new_node
            
    def __getitem__(self, index: int) -> int | float:
        """Obtain the sum up to the position that is entered in forward and backward"""
        if index >= self.count:
            return
        
        current_forward = self.forward_head
        count = 0
        while current_forward and count < index:
            current_forward = current_forward.next
            count += 1
            
        current_backward = self.backward_head
        count = 0
        while current_backward and count < index:
            current_backward = current_backward.next
            count += 1
        
        return f"forward={current_forward.value}, backward={current_backward.value}"
            
    def __repr__(self) -> str:
        current = self.forward_head
        result_forward = "["

        while current:
            result_forward += f"{current.value} ,"
            current = current.next
            
        current = self.backward_head
        result_backward = "["

        while current:
            result_backward += f"{current.value} ,"
            current = current.next
        
        return  f"forward= {result_forward[:-2] + ']' if len(result_forward) > 2 else '[0]'}, \
                backward= {result_backward[:-2] + ']' if len(result_backward) > 2 else '[0]'}"
                
