# MaxHeap implementation using array

from typing import Any, List

class MaxHeap:
    """MaxHeap implementation using array"""
    def __init__(self, array: List = None) -> None:
        self.__build_max_heap(array)
    
    def __build_max_heap(self, array: List) -> None:
        """Construct maximum heap whether there is array or not when class is instantiated"""
        if array is None:
            self.heap = []
        else: 
            self.heap = array

        for index in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(index)
        
    def parent(self, index: int) -> int:
        """Get parent"""
        return (index - 1) // 2
    
    def left_child(self, index: int) -> int:
        """Get left child in a position"""
        return 2 * index + 1

    def right_child(self, index: int) -> int:
        """Get right child in a position"""
        return 2 * index + 2
    
    def swap(self, i: int, j: int) -> None:
        """Swap positions"""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        
    def push(self, value: Any) -> None:
        """Insert a value in the heap"""
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)
        
    def _heapify_up(self, index: int) -> None:
        """Auxiliar method to add a new value. Organize the heap from bottom to top to add the element correctly"""
        while index > 0 and self.heap[self.parent(index)] < self.heap[index]:
            self.swap(index, self.parent(index))
            index = self.parent(index)
            
    def pop(self) -> Any:
        """Extract and delete the max value"""
        if len(self.heap) == 0:
            return 
        
        max_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self._heapify_down(0)
        return max_value
    
    def _heapify_down(self, index: int) -> None:
        """Auxiliar method to remove the max value. Organize the heap from top to bottom"""
        left = self.left_child(index)
        right = self.right_child(index)
        largest = index
        
        if (left < len(self.heap) and self.heap[left] > self.heap[largest]):
            largest = left
        
        if (right < len(self.heap) and self.heap[right] > self.heap[largest]):
            largest = right
        
        if largest != index:
            self.swap(index, largest)
            self._heapify_down(largest)
            
    def __repr__(self) -> str:
        return f"{self.heap}"
    
heap = MaxHeap([4, 10, 3, 5, 1])
print(heap)
heap.push(6)
heap.push(11)
heap.push(7)
print(heap)
print(heap.pop())  # Output: 10
print(heap)
print(heap.pop())  # Output: 5
print(heap)
print(heap.pop()) 