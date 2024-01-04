# Skip List implementation

from random import randint, seed
from typing import Any, List

class Node:
    """Node implementation"""
    def __init__(self, height: int = 0, value: Any = None) -> None:
        self.value = value
        self.next = [None] * height
        
class SkipList:
    """Skip List implementation"""
    def __init__(self):
        self.sentinel = Node()
        self._len = 0
        self._maxHeight = 0
        
    def __len__(self):
        """Return the len of the skip list"""
        return self._len
    
    def _random_height(self) -> int:
        """Generates a random height for a new node"""
        height = 1
        while randint(1, 2) != 1:
            height += 1
        return height
    
    def _find(self, element: Any, update: List = None) -> Node:
        """Find element in the skip list"""
        if not update:
            update = self._update(element)
        if len(update) > 0:
            item = update[0].next[0]
            if item and item.value == element:
                return item
        return

    def _update(self, element: Any) -> List[Node]:
        """It returns a list of nodes in each level that contains the greatest
        value that is smaller than element"""
        update = [None] * self._maxHeight
        
        current = self.sentinel
        for i in reversed(range(self._maxHeight)):
            while current.next[i] and current.next[i].value < element:
                current = current.next[i]
            update[i] = current
        return update
    
    def insert(self, element: Any) -> None:
        """The insertion consists in deciding the height of the new node, using 
        _random_height() and for each of the levels up to this height, insert this 
        new node after the node specified in update."""
        node = Node(self._random_height(), element)

        self._maxHeight = max(self._maxHeight, len(node.next))
        while len(self.sentinel.next) < len(node.next):
            self.sentinel.next.append(None)

        update = self._update(element)            
        
        if not self._find(element, update):
            for i in range(len(node.next)):
                node.next[i] = update[i].next[i]
                update[i].next[i] = node
            self._len += 1
            
    def remove(self, element: Any) -> None:
        """Delete the node found using find() from all levels in which it appears."""
        update = self._update(element)
        
        node = self._find(element, update)
        if node:
            for i in reversed(range(len(node.next))):
                update[i].next[i] = node.next[i]
                if not self.sentinel.next[i]:
                    self._maxHeight -= 1
            self._len -= 1   
    
    def __repr__(self) -> str:
        """Return a string representation of the skip list in ascending order"""
        values = []
        current = self.sentinel.next[0]
        while current:
            values.append(current.value)
            current = current.next[0]
        return f"{values}"                  