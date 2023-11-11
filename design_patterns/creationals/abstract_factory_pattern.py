"""
Abstract Factory is a creational design pattern that allows us to produce families of related objects without specifying their concrete classes.

# Use cases
- Use the Abstract Factory pattern when your code needs to work with multiple families of related products, but you don't want it to depend on classes
specifics of those products, since you may not know them beforehand or simply want to allow for future extensibility.

- Consider implementing the Abstract Factory pattern when you have a class with a group of factory methods that cloud its primary responsibility.

# How to implement it
1. Map a matrix of different types of products against variants of those products.

2. Declare abstract product interfaces for all product types. Then have all concrete product classes implement those
interfaces.

3. Declare the abstract factory interface with a set of creation methods for all abstract products.

4. Implement a group of concrete factory classes, one for each product variant.

5. Create a factory initialization code somewhere in the application. You will need to instantiate one of the factory's concrete classes, depending on
of the application configuration or current environment. Pass this factory object to all classes that build products.

6. Explore the code and find all direct calls to product constructors. Replace them with calls to the appropriate creation method inside
of the factory object.

# Pros and cons
p- You can be sure that the products you get from a factory are compatible with each other.

p- You avoid a strong coupling between specific products and the client code.

p- Principle of single responsibility. You can move product creation code to one place, making the code easier to maintain.

p- Open/closed principle. You can introduce new product variants without breaking existing client code.

c- It may be that the code becomes more complicated than it should, since many new interfaces and classes are introduced along with the pattern.
"""

from __future__ import annotations
from abc import ABC, abstractmethod


"""Abstraccion de las fabricas"""
class AbstractFactory(ABC):
    @abstractmethod
    def create_chair(self) -> AbstractChair:
        pass

    @abstractmethod
    def create_sofa(self) -> AbstractSofa:
        pass

# Fabrica Moderna (concreta)
class ModernFactory(AbstractFactory):
    def create_chair(self) -> AbstractChair:
        return ModernChair()

    def create_sofa(self) -> AbstractSofa:
        return ModernSofa()

# Vieja fabrica (concreta)
class OldFactory(AbstractFactory):
    def create_chair(self) -> AbstractChair:
        return OldChair()

    def create_sofa(self) -> AbstractSofa:
        return OldSofa()

"""Abstraccion de las silla"""
class AbstractChair(ABC):
    @abstractmethod
    def create_a_chair(self) -> str:
        pass

# Silla moderna (concreta)
class ModernChair(AbstractChair):
    def create_a_chair(self) -> str:
        return "Modern Chair"

# Silla vieja (concreta)
class OldChair(AbstractChair):
    def create_a_chair(self) -> str:
        return "Old Chair"


"""Abstracciones de los sofas"""
class AbstractSofa(ABC):
    @abstractmethod
    def create_a_sofa(self) -> None:
        pass

    @abstractmethod
    def another_create_a_sofa(self, collaborator: AbstractChair) -> None:
        pass

# Sofa moderno (concreto)
class ModernSofa(AbstractSofa):
    def create_a_sofa(self) -> str:
        return "The result of the product Modern Sofa."

    def another_create_a_sofa(self, collaborator: AbstractChair) -> str:
        result = collaborator.create_a_chair()
        return f"The result of the Modern Sofa collaborating with the ({result})"

# Sofa viejo (concreto)
class OldSofa(AbstractSofa):
    def create_a_sofa(self) -> str:
        return "The result of the product Old Chair."

    def another_create_a_sofa(self, collaborator: AbstractChair):
        result = collaborator.create_a_chair()
        return f"The result of the Old Sofa collaborating with the ({result})"


def client_code(factory: AbstractFactory) -> None:
    product_a = factory.create_chair()
    product_b = factory.create_sofa()

    print(f"{product_b.create_a_sofa()}")
    print(f"{product_b.another_create_a_sofa(product_a)}", end="")


if __name__ == "__main__":
    print("Client: Testing client code with the first factory type:")
    client_code(ModernFactory())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(OldFactory())
