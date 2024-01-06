from typing import List

class FenwickTree:
    """Fenwick Tree implementation"""
    def __init__(self, array: List[int]) -> None:
        self.size = len(array)
        self.tree = [0] * (self.size + 1)
        
        for index in range(len(array)):
            self._update(index + 1, array[index])

    def _update(self, index: int, delta: int) -> None:
        """Method updates the tree based on the array elements."""
        while index <= self.size:
            self.tree[index] += delta
            index += index & - index

    def __getitem__(self, index: int, ) -> int:
        """Method allows you to use the indexing syntax to retrieve values from the tree."""
        return self._query(index)

    def _query(self, index: int) -> int:
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & - index
        return result

    def range_query(self, start_index: int, end_index: int) -> int:
        """Method can be used to find the sum of elements within a given range"""
        return self._query(end_index) - self._query(start_index - 1)
    
    def __repr__(self) -> str:
        return f"{self.tree}"
