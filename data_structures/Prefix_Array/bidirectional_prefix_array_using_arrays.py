# Bidirectional prefix array implementation using array

from typing import List

class BidirectionalPrefixArray:
    """Bidirectional prefix array implementation using array"""
    def __init__(self, array: List[int | float]) -> None:
        self.array = array
        self.prefix_sum_forward = self.calculate_prefix_array_forward()
        self.prefix_sum_backward = self.calculate_prefix_array_backward()
        
    def calculate_prefix_array_forward(self) -> List[int | float]:
        """Create forward prefix array"""
        if not self.array:
            return [0]
        
        prefix_array_forward = [self.array[0]]
        
        for index in range(1, len(self.array)):
            prefix_array_forward.append(prefix_array_forward[-1] + self.array[index])
        return prefix_array_forward
    
    def calculate_prefix_array_backward(self) -> List[int | float]:
        """Create backward prefix array"""
        if not self.array:
            return [0]
        
        prefix_sum_backward = [self.array[-1]]
        
        for index in range(len(self.array) -2, -1, -1):
            prefix_sum_backward.append(prefix_sum_backward[-1] + self.array[index])
        return prefix_sum_backward
    
    def __getitem__(self, index: int) -> int | float:
        """Obtain the sum up to the position that is entered in forward and backward"""
        if index >= len(self.array):
            return 
        return f"forward={self.prefix_sum_forward[index]}, backward={self.prefix_sum_backward[index]}"
    
    def __repr__(self) -> str:
        return f"forward={self.prefix_sum_forward}, backward={self.prefix_sum_backward}"
