"""
Command is a behavioral design pattern that converts a request into a standalone object that contains all the
information about the application. This transformation allows you to parameterize the methods with different requests, delay
or queue the execution of a request and support operations that cannot be performed.

# Use cases
- Use the Command pattern when you want to parameterize objects with operations.

- Use the Command pattern when you want to queue operations, schedule their execution, or execute them remotely.

- Use the Command pattern when you want to implement reversible operations.

# How to implement it
1. Declare the command interface with a single execute method.

2. Start by extracting requests and putting them inside concrete command classes that implement the command interface.
Each class must have a group of fields to store the arguments of the requests along with references to the object
receiver. All of these values ​​must be initialized through the command's constructor.

3. Identify classes that act as broadcasters. Add fields to store commands within these classes. The stations
They must communicate with their commands only through the command interface. Normally broadcasters do not create objects
on their own, but rather they get them from the client code.

4. Change the stations so that they execute the command instead of directly sending a request to the receiver.

5. The client must initialize objects in the following order:
- Create receivers.
- Create commands and associate them with receivers if necessary.
- Create emitters and associate them with specific commands

# Pros and cons
p- Principle of single responsibility. You can decouple classes that invoke operations from classes that perform those operations.

p- Open/closed principle. You can introduce new commands to the application without breaking existing client code.

p- You can implement undo/redo.

p- You can implement the deferred execution of operations.

p- You can assemble a group of simple commands to create a complex one.

c- The code can get complicated, since you are introducing a new layer between senders and receivers.


"""


from __future__ import annotations
from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


class SimpleCommand(Command):
    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"SimpleCommand: See, I can do simple things like printing"
              f"({self._payload})")


class ComplexCommand(Command):
    def __init__(self, receiver: Receiver, a: str, b: str) -> None:
        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self) -> None:
        print("ComplexCommand: Complex stuff should be done by a receiver object", end="")
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)


class Receiver:
    def do_something(self, a: str) -> None:
        print(f"\nReceiver: Working on ({a}.)", end="")

    def do_something_else(self, b: str) -> None:
        print(f"\nReceiver: Also working on ({b}.)", end="")


class Invoker:
    _on_start = None
    _on_finish = None

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def do_something_important(self) -> None:
        print("Invoker: Does anybody want something done before I begin?")
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print("Invoker: ...doing something really important...")

        print("Invoker: Does anybody want something done after I finish?")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


if __name__ == "__main__":
    invoker = Invoker()
    invoker.set_on_start(SimpleCommand("Say Hi!"))
    receiver = Receiver()
    invoker.set_on_finish(ComplexCommand(
        receiver, "Send email", "Save report"))

    invoker.do_something_important()



