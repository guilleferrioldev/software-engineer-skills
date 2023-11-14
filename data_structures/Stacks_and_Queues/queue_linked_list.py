# Queue mplementation using linked lists
from typing import Any, Self

class Node:
    """Implementation of the node"""
    def __init__(self, data: Any = None, next: Self = None, prev: Self = None) -> None:
        self.data = data
        self.next = next
        self.prev = prev

class Queue:
    """Implementation using linked lists"""
    def __init__(self) -> None:
        self.front = None
        self.rear = None
        self.size = 0
    
    def enqueue(self, data: Any) -> None:
        """Method to eneque an element"""
        new_node = Node(data)
        
        if self.front is None:
            self.front = new_node
            self.rear = self.front
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node
        
        self.size += 1
        
    def dequeue(self) -> Node:
        """Method to dequeue an element"""
        if self.size < 1:
            return "Queue is empty"
        
        data = self.front.data
        
        if self.size == 1:
            self.front = self.rear = None
        elif self.size > 1:
            self.front = self.front.next
            self.front.prev = None
        
        self.size -= 1 
        return data

    def __repr__(self) -> str:
        current = self.front
        result = "["
        while current:
            result = result + str(current.data) + ", "
            current = current.next
        return result[:-2] + "]" if len(result) > 1 else result + "]"
