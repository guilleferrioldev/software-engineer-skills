"""
Bridge is a structural design pattern that allows you to split a large class, or a group of closely related classes, into two hierarchies.
separate (abstraction and implementation) that can be developed independently of each other.

# Use cases
- Use the Bridge pattern when you want to split and organize a monolithic class that has many variants of a single functionality (e.g.
whether the class can work with multiple database servers).

- Use the pattern when you need to extend a class in several orthogonal (independent) dimensions.

- Use the Bridge pattern when you need to be able to change implementations during runtime.

# How to implement it
1. Identify the orthogonal dimensions of your classes. These independent concepts can be: abstraction/platform, domain/infrastructure,
front end/back end, or interface/implementation.

2. Check what operations the client needs and define them in the abstraction base class.

3. Determine the operations available on all platforms. Declare those that the abstraction needs in the general implementation interface.

4. Create concrete implementation classes for all platforms in your domain, but make sure they all follow the implementation interface.

5. Inside the abstraction class add a reference field for the implementation type. Abstraction delegates most of the work to
implementation object referenced in that field.

6. If you have many variants of high-level logic, create refined abstractions for each variant by extending the abstraction base class.

7. The client code must pass an implementation object to the abstraction's constructor to associate one with the other. The client can then
ignore the implementation and work only with the object of the abstraction.


# Pros and cons
p- You can create platform-independent classes and applications.

p- The client code works with high-level abstractions. You are not exposed to the details of the platform.

p- Open/closed principle. You can introduce new abstractions and implementations independent of each other.

p- Principle of single responsibility. You can focus on high-level logic in the abstraction and platform details in the implementation.

c- The code may become complicated if you apply the pattern to a very cohesive class.
"""

from __future__ import annotations
from abc import ABC, abstractmethod

class Abstraction:
    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation

    def operation(self) -> str:
        return (f"Abstraction: Base operation with:\n"
                f"{self.implementation.operation_implementation()}")


class ExtendedAbstraction(Abstraction):
    def operation(self) -> str:
        return (f"ExtendedAbstraction: Extended operation with:\n"
                f"{self.implementation.operation_implementation()}")


class Implementation(ABC):
    @abstractmethod
    def operation_implementation(self) -> str:
        pass 

class ConcreteImplementationA(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationA: Here's the result on the platform A."


class ConcreteImplementationB(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationB: Here's the result on the platform B."


def client_code(abstraction: Abstraction) -> None:
    print(abstraction.operation(), end="")


if __name__ == "__main__":
    implementation = ConcreteImplementationA()
    abstraction = Abstraction(implementation)
    client_code(abstraction)

    print("\n")

    implementation = ConcreteImplementationB()
    abstraction = ExtendedAbstraction(implementation)
    client_code(abstraction)







