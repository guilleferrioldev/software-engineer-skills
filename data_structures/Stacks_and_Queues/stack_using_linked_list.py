### Stacks implementation using single linked lists

from typing import Any

class StackOverflowError(Exception):
    pass

class Node:
    """Node implementation"""
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next = None

class Stack:
    """Stack implementation using single linked lists"""
    def __init__(self, maxsize: int = float("inf")) -> None:
        self.top: Node = None
        self.size = 0
        self.maxsize = maxsize

    def is_empty(self) -> bool:
        """Method to know if the stack is empty"""
        return self.top is None

    def push(self, data: Any) -> None | Exception:
        """Method to add an element """
        node = Node(data)
        
        if self.size >= self.maxsize:
            raise StackOverflowError()
    
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
        
        self.size += 1
    
    def pop(self) -> Node:
        """Method to delete an element"""
        if not self.top:
            return
        
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data
    
    def peek(self) -> Node:
        """Method to check the top element"""
        if not self.top:
            return     
        return self.top.data
    
    def __repr__(self) -> str:
        current = self.top
        result = "["
        while current:
            result = result + str(current.data) + ", "
            current = current.next
        return result[:-2] + "]" if len(result) > 1 else result + "]"
    