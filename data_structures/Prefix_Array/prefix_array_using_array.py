# Prefix array implementation using array

from typing import List

class PrefixArray:
    """Prefix array implementation using array"""
    def __init__(self, array: List[int | float]) -> None:
        self.array = array
        self.prefix_sum = self.__calculate_prefix_array()

    def __calculate_prefix_array(self) -> List[int | float]:
        """Create the prefix array"""
        if not self.array:
            return [0]
        
        prefix_sum = [self.array[0]]
        
        for index in range(1, len(self.array)):
            prefix_sum.append(prefix_sum[-1] + self.array[index])
        
        return prefix_sum

    def __getitem__(self, end_index: int) -> int | float:
        """Obtain the sum up to the position entered"""
        if end_index >= len(self.prefix_sum):
            return
        return self.prefix_sum[end_index]
            
    def __repr__(self) -> str:
        return f"{self.prefix_sum}"
