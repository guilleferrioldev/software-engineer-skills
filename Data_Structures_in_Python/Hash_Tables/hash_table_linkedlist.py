# Separate chaining
"""
Separate chaining is another method to handle the problem of collision in hash tables. 
It solves this problem by allowing each slot in the hash table to store a reference to many items
at the position of a collision. So, at the index of a collision, we are allowed to store
multiple items in the hash table.
"""

#  Implementation using linked list (Binary search trees)
class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

# Define a single linked list
class SinglyLinkedList:
    def __init__ (self):
        self.tail = None
        self.head = None
    
    # method to append new nodes
    def append(self, key, value):
        node = Node(key, value)

        if self.tail:
            self.tail.next = node
            self.tail = node 
        else:
            self.head = node
            self.tail = node
    
    # method which prints all the data records with key-value pairs
    def traverse(self):
        current = self.head
        
        while current:
            print( current.key, "->", current.value)
            current = current.next

    # method that matches the key that we want to search in the linked list
    def search(self, key):
        current = self.head

        while current:
            if current.key == key:
                print(current.key, "->", current.value)
                return True
            current = current.next
        return False



class HashTableChaining:
    def __init__(self):
        self.size = 6
        self.slots = [None for i in range(self.size)]
        for x in range(self.size) :
            self.slots[x] = SinglyLinkedList()

    
    # Hash fucntion
    def _hash(self, key):
        mult = 1
        hv = 0
    
        for ch in key:
            hv += mult * ord(ch)
            mult += 1
        return hv % self.size

    
    # method to insert a new data record in the hash table.
    def put(self, key, value):
        node = Node(key, value)
        h = self._hash(key)
        self.slots[h].append(key, value)
    
    # method to retrieve the data elements given the key value
    def get(self, key):
        h = self._hash(key)
        v = self.slots[h].search(key)
    
    # Method to print the complete hash table
    def print(self) :
        for x in range(self.size) :
            print(x, end = "\n")
            self.slots[x].traverse()

# Test
"""
ht = HashTableChaining()
ht.put("good", "eggs")
ht.put("better", "ham")
ht.put("best", "spam")
ht.put("ad", "do not")
ht.put("ga", "collide")
ht.put("awd", "do not")
ht.print()
"""
