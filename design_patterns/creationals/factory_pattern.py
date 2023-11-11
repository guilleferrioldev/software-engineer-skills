"""
Factory Method is a creational design pattern that provides an interface for creating objects in a superclass, while allowing
Subclasses alter the type of objects to be created.

# Use cases
- Use the Factory Method when you do not know in advance the exact dependencies and types of the objects with which your code must work.

- Use the Factory Method when you want to offer users of your library or framework a way to extend its internal components.

- Use the Factory Method when you want to save system resources by reusing existing objects instead of
rebuild them every time.


# How to implement it
1. Make all products follow the same interface. This interface should declare methods that make sense across all products.

2.Add an empty Factory Method pattern inside the creator class. The return type of the method must match the common interface
of the products.

3. Find all references to product constructors in the code of the creator class. One by one, replace them with invocations
to the Factory Method, while extracting the product creation code to place it inside the Factory Method.

4. Now, create a group of creator subclasses for each product type listed in the Factory Method. Overrides the Factory Method in the
subclasses and extract the appropriate parts of the base method's constructor code.

5. If there are too many product types and it doesn't make sense to create subclasses for all of them, you can reuse the control parameter of the
base class in subclasses.

6. If, after all the extractions, the base Factory Method is empty, you can make it abstract. If there is anything left inside, you can turn it into
a default behavior of the method.


# Pros and cons
p- If, after all the extractions, the base Factory Method remains empty, you can make it abstract. If there is anything left inside, you can turn it into a
default behavior of the method.

p- Principle of single responsibility. You can move the product creation code to one place in the program, making the code more
easy to maintain.

p- Open/closed principle. You can incorporate new types of products into the program without breaking existing client code.

c- The code may become complicated, since you must incorporate a multitude of new subclasses to implement the pattern. The ideal situation
would be to introduce the pattern into an existing hierarchy of creator classes.
"""

from __future__ import annotations
from abc import ABC, abstractmethod


"""Abstract creators"""
class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:
        # Call the factory method to create a Product object.
        product = self.factory_method()

        # Now, use the product.
        result = f"Creator: The same creator's code has just worked with {product.operation()}"

        return result

# Creador 1 (concreto)
class ConcreteCreator1(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct1()

# Creador 2 (concreto)
class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()

"""Abstract product"""
class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass
    
# Product 1 (concreto)   
class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"

# Product 2 (concreto)  
class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"


def client_code(creator: Creator) -> None:
    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())