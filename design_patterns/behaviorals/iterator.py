"""
Iterator is a behavioral design pattern that allows you to iterate through elements of a collection without exposing their representation
underlying (list, stack, tree, etc.).

# Use cases
- Use the Iterator pattern when your collection has a complex data structure internally, but you want to hide its
complexity to customers (whether for convenience or security reasons).

- Use the pattern to reduce duplication in code traversal throughout your application.

- Use the Iterator pattern when you want your code to be able to traverse different data structures, or when data types
These structures are not known in advance.

# How to implement it
1. Declare the iterator interface. At a minimum, you should have a method to extract the next element from a collection. By
For convenience, you can add a couple of different methods, such as extracting the previous element, locating the current position, or
check the end of the iteration.

2. Declare the collection interface and describe a method to search for iterators. The return type must be the same as the
iterator interface. You can declare similar methods if you plan to have several different groups of iterators.

3. Implement concrete iterator classes for the collections that you want to be traversed by iterators. An iterator object
must be linked to a single instance of the collection. Typically, this link is established through the constructor of the
iterator.

4. Implement the collection interface in your collection classes. The main idea is to provide the client with a shortcut to
create custom iterators for a particular collection class. The collection object must be passed to the
iterator constructor to establish a link between them.

5. Review the client code to replace all collection traversal code with the use of iterators. The client searches
a new iterator object every time you need to loop through the elements of the collection.

# Pros and cons
p- Principle of single responsibility. You can clean up client code and collections by extracting traversal algorithms
bulky and placing them in separate classes.

p- Open/closed principle. You can implement new types of collections and iterators and pass them to existing code without
break down anything.

p- You can iterate through the same collection in parallel because each iterator object contains its own iteration state.

p- For the same reason, you can delay an iteration and continue when necessary.

c- Applying the pattern may be excessive if your application works only with simple collections.

c- Using an iterator may be less efficient than directly traversing the elements of some specialized collections.
"""


from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List


class AlphabeticalOrderIterator(Iterator):
    _position: int = None
    _reverse: bool = False

    def __init__(self, collection: WordsCollection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value

class WordsCollection(Iterable):
    def __init__(self, collection: List[Any] = []) -> None:
        self._collection = collection

    def __iter__(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection)

    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection, True)

    def add_item(self, item: Any):
        self._collection.append(item)


if __name__ == "__main__":
    collection = WordsCollection()
    collection.add_item("First")
    collection.add_item("Second")
    collection.add_item("Third")

    print("Straight traversal:")
    print("\n".join(collection))
    print("")

    print("Reverse traversal:")
    print("\n".join(collection.get_reverse_iterator()), end="")