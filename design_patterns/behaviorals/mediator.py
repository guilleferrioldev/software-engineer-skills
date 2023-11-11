"""
Mediator is a behavioral design pattern that allows you to reduce chaotic dependencies between objects. The boss
It restricts direct communications between objects, forcing them to collaborate only through a mediating object.

# Use cases
- Use the Mediator pattern when it is difficult to change some of the classes because they are tightly coupled to a handful
of other classes.

- Use the pattern when you cannot reuse a component in a different program because it is too dependent on others
components.

- Use the Mediator pattern when you find yourself creating hundreds of component subclasses just to reuse a behavior
basic in various contexts.

# How to implement it
1. Identify a group of tightly coupled classes that would benefit from being more independent (e.g., for maintenance
simpler or simpler reuse of those classes).

2. Declare the mediator interface and describe the desired communication protocol between mediators and various other components. In the
In most cases, a single method of receiving notifications from components is sufficient.

3. Implement the mediating concrete class. This class will benefit from storing references to all the components it manages.

4. You can go further and make the mediator interface responsible for the creation and destruction of component objects. Behind this,
The mediator can resemble a factory or a facade.
"""

from __future__ import annotations
from abc import ABC

class Mediator(ABC):
    def notify(self, sender: object, event: str) -> None:
        pass

class ConcreteMediator(Mediator):
    def __init__(self, component1: Component1, component2: Component2) -> None:
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def notify(self, sender: object, event: str) -> None:
        if event == "A":
            print("Mediator reacts on A and triggers following operations:")
            self._component2.do_c()
        elif event == "D":
            print("Mediator reacts on D and triggers following operations:")
            self._component1.do_b()
            self._component2.do_c()


class BaseComponent:
    def __init__(self, mediator: Mediator = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator

class Component1(BaseComponent):
    def do_a(self) -> None:
        print("Component 1 does A.")
        self.mediator.notify(self, "A")

    def do_b(self) -> None:
        print("Component 1 does B.")
        self.mediator.notify(self, "B")


class Component2(BaseComponent):
    def do_c(self) -> None:
        print("Component 2 does C.")
        self.mediator.notify(self, "C")

    def do_d(self) -> None:
        print("Component 2 does D.")
        self.mediator.notify(self, "D")


if __name__ == "__main__":
    c1 = Component1()
    c2 = Component2()
    mediator = ConcreteMediator(c1, c2)

    print("Client triggers operation A.")
    c1.do_a()

    print("\n", end="")

    print("Client triggers operation D.")
    c2.do_d()

