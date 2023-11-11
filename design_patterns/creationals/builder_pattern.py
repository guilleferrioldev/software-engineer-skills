"""
Builder is a creational design pattern that allows us to build complex objects step by step. The pattern allows us to produce different types
and representations of an object using the same construction code.

# Use cases
- Use the Builder pattern to avoid a “telescopic builder” (with many parameters)

- Use the Builder pattern when you want the code to be able to create different representations of certain products.

- Use the Builder pattern to build trees with the Composite pattern or other complex objects.


# How to implement it
1. Make sure you can clearly define common build steps for all available product representations. Otherwise,
you will not be able to proceed to implement the pattern.

2. Declare these steps in the base constructor interface.

3. Create a concrete constructor class for each of the product representations and implement its construction steps.

4. Consider creating a director class. You can encapsulate multiple ways to build a product using the same builder object.

5. The client code creates both the constructor and director objects. Before construction begins, the client must pass a constructor object
to the Director. Typically, the client does this only once, using the director's constructor parameters. The director uses the object
builder for the rest of the construction. There is an alternative way, in which the constructor object is passed directly to the method.
director construction.

6. The build result can only be obtained directly from the manager if all products follow the same interface. Otherwise,
the client must extract the result from the constructor.


# Pros and cons
p- You can build objects step by step, defer construction steps or execute steps recursively.

p- You can reuse the same build code when building multiple product representations.

p- Principle of single responsibility. You can isolate complex construction code from the product's business logic.

c- The overall complexity of the code increases, since the pattern requires the creation of several new classes.
"""


from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Car(ABC):
    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def car_body(self) -> None:
        pass

    @abstractmethod
    def autopilot(self) -> None:
        pass

    @abstractmethod
    def battery(self) -> None:
        pass


class ConcreteCar(Car):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Tesla()

    @property
    def product(self) -> Tesla:
        product = self._product
        self.reset()
        return product

    def car_body(self) -> None:
        self._product.add("Car body")

    def autopilot(self) -> None:
        self._product.add("Autopilot")

    def battery(self) -> None:
        self._product.add("Battery")


class Tesla():
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")


class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Car:
        return self._builder

    @builder.setter
    def builder(self, builder: Car) -> None:
        self._builder = builder

    def build_minimal_viable_product(self) -> None:
        self.builder.car_body()

    def build_full_featured_product(self) -> None:
        self.builder.car_body()
        self.builder.autopilot()
        self.builder.battery()


if __name__ == "__main__":
    director = Director()
    builder = ConcreteCar()
    director.builder = builder

    print("Standard basic product: ")
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print("\n")

    print("Standard full featured product: ")
    director.build_full_featured_product()
    builder.product.list_parts()

    print("\n")

    # Remember, the Builder pattern can be used without a Director class.
    print("Custom product: ")
    builder.car_body()
    builder.autopilot()
    builder.product.list_parts()




