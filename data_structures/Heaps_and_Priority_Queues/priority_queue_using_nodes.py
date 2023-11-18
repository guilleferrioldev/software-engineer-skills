# PriorityQueue implementation using Nodes

from typing import Any

class Node:
    """class for Node with data and priority"""
    def __init__(self, info: Any, priority: int | float) -> None:
        self.info = info
        self.priority = priority
        
    def __repr__(self):
        return f"({self.info}, {self.priority})"

class PriorityQueue:
    """Implementation class using Nodes"""
    def __init__(self) -> None:
        self.elements = []
        
    def is_empty(self) -> bool:
        """Method to know if the Priority Queue has elements"""
        return not self.elements

    def put(self, info: Any, priority: int | float) -> None:
        """Method to insert elements """
        new_node = Node(info, priority)
        
        for index in range(len(self.elements)):
            if self.elements[index].priority > priority:
                self.elements.insert(index, new_node)
                return 
        self.elements.append(new_node)
                
    def get(self) -> Any:
        """Method to obtain elements and remove them from the priority queue"""
        if self.is_empty():
            return
        return self.elements.pop(0).info

    def __repr__(self) -> str:
        return f"{self.elements}"
