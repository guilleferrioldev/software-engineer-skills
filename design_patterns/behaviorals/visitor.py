"""
Visitor is a behavioral design pattern that allows you to separate algorithms from the objects they operate on.

# Use cases
- Use the Visitor pattern when you need to perform an operation on all the elements of a complex object structure
(for example, a tree of objects).

- Use the Visitor pattern to clean the business logic of auxiliary behaviors.

- Use the pattern when a behavior only makes sense in some classes in a class hierarchy, but not in others.

# How to implement it
1. Declare the visitor interface with a group of “visitor” methods, one for each concrete element class existing in the
 program.

2. Declare the element interface. If you are working with an existing feature class hierarchy, add the abstract method
 of “acceptance” to the base class of the hierarchy. This method must accept a visitor object as an argument.

3. Implement the acceptor methods in all concrete element classes. These methods should simply redirect the
Call a visitor method on the incoming visitor object that matches the class of the current element.

4. Feature classes should only work with visitors through the visitor interface. Visitors, however, must
know all the concrete element classes, referenced as parameter types of the visit methods.

5. For each behavior that cannot be implemented within the element hierarchy, create a new visitor concrete class
and implements all visitor methods.

6. The client must create visitor objects and pass them into elements via “accept” methods.

# Pros and cons
p- Open/closed principle. You can introduce new behavior that can work with objects of different classes without
change those classes.

p- Principle of single responsibility. You can take multiple versions of the same behavior and put them in the same class.

p- A visitor object can accumulate some useful information while working with various objects. This can be useful when
You want to traverse a complex object structure, such as an object tree, and apply the visitor to each object in that
structure.

c- You must update all visitors every time a class is added or removed from the element hierarchy.

c- Visitors may lack necessary access to the private fields and methods of the elements they are supposed to interact with.
they must work.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass


class ConcreteComponentA(Component):
    def accept(self, visitor: Visitor) -> None:
        visitor.visit_concrete_component_a(self)

    def exclusive_method_of_concrete_component_a(self) -> str:
        return "A"


class ConcreteComponentB(Component):
    def accept(self, visitor: Visitor):
        visitor.visit_concrete_component_b(self)

    def special_method_of_concrete_component_b(self) -> str:
        return "B"


class Visitor(ABC):
    @abstractmethod
    def visit_concrete_component_a(self, element: ConcreteComponentA) -> None:
        pass

    @abstractmethod
    def visit_concrete_component_b(self, element: ConcreteComponentB) -> None:
        pass

class ConcreteVisitor1(Visitor):
    def visit_concrete_component_a(self, element) -> None:
        print(f"{element.exclusive_method_of_concrete_component_a()} + ConcreteVisitor1")

    def visit_concrete_component_b(self, element) -> None:
        print(f"{element.special_method_of_concrete_component_b()} + ConcreteVisitor1")


class ConcreteVisitor2(Visitor):
    def visit_concrete_component_a(self, element) -> None:
        print(f"{element.exclusive_method_of_concrete_component_a()} + ConcreteVisitor2")

    def visit_concrete_component_b(self, element) -> None:
        print(f"{element.special_method_of_concrete_component_b()} + ConcreteVisitor2")


def client_code(components: List[Component], visitor: Visitor) -> None:
    for component in components:
        component.accept(visitor)

if __name__ == "__main__":
    components = [ConcreteComponentA(), ConcreteComponentB()]

    print("The client code works with all visitors via the base Visitor interface:")
    visitor1 = ConcreteVisitor1()
    client_code(components, visitor1)

    print("It allows the same client code to work with different types of visitors:")
    visitor2 = ConcreteVisitor2()
    client_code(components, visitor2)
