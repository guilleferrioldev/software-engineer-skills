"""
Composite is a structural design pattern that allows you to compose objects into tree structures and work with those structures as if they were
individual objects.

# Use cases
- Use the Composite pattern when you have to implement a tree-shaped object structure.

- Use the pattern when you want the client code to treat simple and complex elements the same way.

# How to implement it
1. Make sure your application's core model can be represented as a tree structure. Try to break it down into simple elements and
containers. Remember that containers must be able to hold both simple items and other containers.

2. Declare the component interface with a list of methods that make sense for simple and complex components.

3. Create a leaf class to represent simple elements. A program can have several different leaf classes.

4. Create a wrapper class to represent complex elements. Include an array field in this class to store references to subelements.
The array must be able to store sheets and containers, so be sure to declare it with the type of the component interface.

5. Finally, define the methods to add and remove child elements within the container.

#  Pros and cons
p- You can work with complex tree structures more comfortably: use polymorphism and recursion to your advantage.

p- Open/closed principle. You can introduce new item types to the app without breaking existing code, which now works with
the object tree.

c- It may be difficult to provide a common interface for classes whose functionality differs too much. In some cases, you will have to generalize in
overload the component interface, making it more difficult to understand.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        self._parent = parent

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def operation(self) -> str:
        pass


class Leaf(Component):
    def operation(self) -> str:
        return "Leaf"


class Composite(Component):
    def __init__(self) -> None:
        self._children: List[Component] = []

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Branch({'+'.join(results)})"


def client_code(component: Component) -> None:
    print(f"RESULT: {component.operation()}", end="")


def client_code2(component1: Component, component2: Component) -> None:
    if component1.is_composite():
        component1.add(component2)

    print(f"RESULT: {component1.operation()}", end="")


if __name__ == "__main__":
    # This way the client code can support the simple leaf components...
    simple = Leaf()
    print("Client: I've got a simple component:")
    client_code(simple)
    print("\n")

    # ...as well as the complex composites.
    tree = Composite()

    branch1 = Composite()
    branch1.add(Leaf())
    branch1.add(Leaf())

    branch2 = Composite()
    branch2.add(Leaf())

    tree.add(branch1)
    tree.add(branch2)

    print("Client: Now I've got a composite tree:")
    client_code(tree)
    print("\n")

    print("Client: I don't need to check the components classes even when managing the tree:")
    client_code2(tree, simple)




