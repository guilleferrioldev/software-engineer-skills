### Deque implementation using Array

from typing import Any, List, Iterable

class Deque:
    """Implementation using Array"""
    def __init__(self, items: List = None) -> None:
        if items is not None:
            self.items = items
        else:
            self.items = []
    
    def __len__(self):
        return len(self.items)
        
    def append(self, item: Any) -> None:
        """Method to add an item to the end of the array"""
        self.items.append(item)
        
    def appendleft(self, item: Any) -> None:
        """Method to add an item to the beginning of the array"""
        self.items.insert(0, item)
        
    def pop(self) -> Any:
        """Method to remove an element at the end of the array"""
        return self.items.pop()
        
    def popleft(self) -> Any:
        """Method to remove an element at the beginning of the array"""
        return self.items.pop(0)
    
    def extend(self, items: Iterable) -> Any:
        """Method to add several elements to the array"""
        self.items.extend(items)
        
    def rotate(self, number: int) -> None:
        """Method to rotate the array"""
        number = number % len(self.items)
        self.items = self.items[-number:] + self.items[:-number]
             
    def __getitem__(self, item: int) -> Any:
        return self.items[item]
        
    def __repr__(self):
        return str(self.items)
    