"""
Facade is a structural design pattern that provides a simplified interface to a library, framework, or any
another complex group of classes.

# Use cases
- Use the Facade pattern when you need a limited but direct interface to a complex subsystem.

- Use the Facade pattern when you want to structure a subsystem in layers.

# How to implement it
1. Checks if it is possible to provide a simpler interface than what an existing subsystem is providing. Are you OK
routed if this interface makes the client code independent of many of the subsystem classes.

2. Declare and implement this interface in a new facade class. The facade must redirect calls from the code
client to the appropriate subsystem objects. The facade must be responsible for initializing the subsystem and managing its
lifecycle, unless the client code already does so.

3. To take full advantage of the pattern, have all client code communicate with the subsystem only through the
facade. Now the client code is protected from any changes to the subsystem code. For example, when updating
a subsystem to a new version, you will only have to modify the facade code

4. If the facade gets too big, think about extracting some of its behavior and putting it inside a new class
refined facade.

# Pros and cons
p- You can isolate your code from the complexity of a subsystem.

c- A facade can become an all-powerful object coupled to all the classes of an application.
"""

from __future__ import annotations

class Facade:
    def __init__(self, subsystem1: Subsystem1, subsystem2: Subsystem2) -> None:
        self._subsystem1 = subsystem1 or Subsystem1()
        self._subsystem2 = subsystem2 or Subsystem2()

    def operation(self) -> str:
        results = []
        results.append("Facade initializes subsystems:")
        results.append(self._subsystem1.operation1())
        results.append(self._subsystem2.operation1())
        results.append("Facade orders subsystems to perform the action:")
        results.append(self._subsystem1.operation_n())
        results.append(self._subsystem2.operation_z())
        return "\n".join(results)


class Subsystem1:
    def operation1(self) -> str:
        return "Subsystem1: Ready!"

    def operation_n(self) -> str:
        return "Subsystem1: Go!"


class Subsystem2:
    def operation1(self) -> str:
        return "Subsystem2: Get ready!"

    def operation_z(self) -> str:
        return "Subsystem2: Fire!"


def client_code(facade: Facade) -> None:
    print(facade.operation(), end="")


if __name__ == "__main__":
    subsystem1 = Subsystem1()
    subsystem2 = Subsystem2()
    facade = Facade(subsystem1, subsystem2)
    client_code(facade)
