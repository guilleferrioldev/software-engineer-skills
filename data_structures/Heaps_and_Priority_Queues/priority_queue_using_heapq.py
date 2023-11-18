# Priority Queue implementation using heapq librarys

import heapq
from typing import Any

class PriorityQueue:
    """Priority Queue using heapq librarys"""
    def __init__(self) -> None:
        self.elements = []
        
    def is_empty(self) -> bool:
        """Method to know if the Priority Queue has elements"""
        return not self.elements 
    
    def put(self, item: Any, priority: int) -> None:
        """Method to insert elements according to priority"""
        heapq.heappush(self.elements, (priority, item))

    def get(self) -> Any:
        """Method to obtain elements and remove them from the priority queue"""
        return heapq.heappop(self.elements)[1]
    
    def __repr__(self) -> str:
        return f"{self.elements}"