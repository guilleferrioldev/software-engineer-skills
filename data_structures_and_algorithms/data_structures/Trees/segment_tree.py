from math import ceil, log2
from typing import List

class SegmentationTree():
    """Segment Tree implementation"""
    def __init__(self, input_list: List[int]) -> None:
        self._input_list = input_list
        self._build()
        self._is_propogated = True

    def _build(self) -> None: 
        """Build the tree"""
        self._length = len(self._input_list)
        height = ceil(log2(self._length))
        number_of_nodes = 2 * (2 ** height) - 1
    
        self._seg_tree = [None] * number_of_nodes
        
        self._propogate(left = 0, right = self._length - 1, index = 0)

    def _propogate(self, left: int, right: int, index: int) -> None:
        """This private method is used in the _build method to recursively build the 
        segment tree in a top-down manner."""
        if right < left:
            return

        if left == right: 
            value = self._input_list[left]
            self._seg_tree[index] = value
            return

        midpoint = (left + right) // 2
        # left side 
        self._propogate(left, midpoint, index * 2 + 1)
        # right side
        self._propogate(midpoint + 1, right, index * 2 + 2)

        # handle parent
        left_val  = self._seg_tree[index * 2 + 1]
        right_val = self._seg_tree[index * 2 + 2]
        self._seg_tree[index] = left_val + right_val

    def query(self, query_left: int, query_right: int) -> int:
        """Calculates the sum of values within a given range in the original array using the segment tree."""
        if not self._is_propogated:
            self._propogate(left = 0, right = self._length - 1, index = 0)

        return self._query_helper(query_left, query_right, left = 0, right = self._length - 1, index = 0)

    def _query_helper(self, query_left: int, query_right: int, left: int, right: int, index: int) -> int:
        """Method to recursively calculate the sum over a range."""
        if right < left: 
            return 0

        if query_right < left or right < query_left:
            return 0

        if query_left <= left and right <= query_right:
            return self._seg_tree[index]

        midpoint = (left + right) // 2 
        left_val = self._query_helper(query_left, query_right, left, midpoint, index * 2 + 1)
        right_val = self._query_helper(query_left, query_right, midpoint + 1, right, index * 2 + 2)

        return left_val + right_val 

    def update(self, index: int, new_value: int) -> None:
        """Change a value in the three"""
        old_value = self._input_list[index]
        if old_value != new_value:
            self._input_list[index] = new_value
            self._is_propogated = False