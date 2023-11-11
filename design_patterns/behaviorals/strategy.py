"""
Strategy is a behavioral design pattern that allows you to define a family of algorithms, place each of them in
a separate class and make your objects interchangeable.

# Use cases
- Use the Strategy pattern when you want to use different variants of an algorithm within an object and be able to change from one
algorithm to another during runtime.

- Use the Strategy pattern when you have many similar classes that only differ in the way they execute a certain
behavior.

- Use the pattern to isolate the business logic of a class from the implementation details of algorithms that may not
be so important in the context of that logic.

- Use the pattern when your class has a huge conditional operator that switches between different variants of the same algorithm.

# How to implement it
1. In the context class, identify an algorithm that tends to undergo frequent changes. It can also be a huge conditional
that selects and executes a variant of the same algorithm at runtime.

2. Declare the strategy interface common to all variants of the algorithm.

3. One by one, extract all the algorithms and put them in their own classes. They must all implement the same interface strategy.

4. In the context class, add a field to store a reference to a strategy object. Provides a set modifier
to replace values ​​in that field. The context class must work with the strategy object only through the interface
strategy. The context class can define an interface that allows the strategy to access its data.

5. Clients of the context class must associate it with an appropriate strategy that matches how they expect it to be
The context class does its main work.

# Pros and cons
p- You can swap algorithms used within an object during runtime.

p- You can isolate the implementation details of an algorithm from the code that uses it.

p- You can replace inheritance with composition.

p- Open/closed principle. You can introduce new strategies without having to change the context.

c- If you only have a couple of algorithms that rarely change, there is no real reason to overcomplicate the program with new ones.
classes and interfaces that come with the pattern.

c- Clients must know the differences between strategies to be able to select the appropriate one.

c- Many modern programming languages ​​have functional type support that allows you to implement different versions of
an algorithm within a group of anonymous functions. Then you can use these functions exactly as you would have used
strategy objects, but without cluttering your code with additional classes and interfaces.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Context():
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def do_some_business_logic(self) -> None:
        print("Context: Sorting data using the strategy (not sure how it'll do it)")
        result = self._strategy.do_algorithm(["a", "b", "c", "d", "e"])
        print(",".join(result))

class Strategy(ABC):
    @abstractmethod
    def do_algorithm(self, data: List):
        pass

class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data: List) -> List:
        return sorted(data)


class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data: List) -> List:
        return reversed(sorted(data))


if __name__ == "__main__":
    context = Context(ConcreteStrategyA())
    print("Client: Strategy is set to normal sorting.")
    context.do_some_business_logic()
    print()

    print("Client: Strategy is set to reverse sorting.")
    context.strategy = ConcreteStrategyB()
    context.do_some_business_logic()













