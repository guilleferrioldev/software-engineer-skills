"""
Chain of Responsibility is a behavioral design pattern that allows you to pass requests along a chain of
handlers. Upon receiving a request, each handler decides whether to process it or pass it to the next handler in the chain.

# Use cases
- Use the Chain of Responsibility pattern when your program must process different types of requests in several ways,
but the exact types of requests and their sequences are not known in advance.

- Use the pattern when it is essential to execute multiple handlers in a specific order.

- Use the Chain of Responsibility pattern when the group of handlers and their order must change during runtime.

# How to implement it
1. Declare the handler interface and describe the signature of a method for handling requests.

2. To eliminate duplicate boilerplate code in concrete handlers, it may be worth creating an abstract handler class
base, derived from the handler interface.

3. One by one, create concrete handler subclasses and implement the control methods. Each manager must make two decisions
when you receive a request:
- If you process the request
- If you pass the request to the next link in the chain.

4. The client can assemble chains on his own or receive ready-made chains from other objects. In the latter case, you must
implement some factory classes to create strings according to configuration or environment settings.

5. The client can activate any handler in the chain, not just the first one. The request will be passed along the chain
until some handler refuses to pass it or until it reaches the end of the chain.

6. Due to the dynamic nature of the chain, the client must be ready to manage the following scenarios:
- The chain can consist of a single link.
- Some requests may not reach the end of the chain.
- Others can reach the end of the chain without being managed.

# Pros and cons
p- You can control the order of request control.

p- Principle of single responsibility. You can decouple classes that invoke operations from classes that perform operations.

p- Open/closed principle. You can introduce new handlers into your application without breaking existing client code.

c- Some requests may end up not being managed.
"""


from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None

class MonkeyHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Banana":
            return f"Monkey: I'll eat the {request}"
        else:
            return super().handle(request)


class SquirrelHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Nut":
            return f"Squirrel: I'll eat the {request}"
        else:
            return super().handle(request)


class DogHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "MeatBall":
            return f"Dog: I'll eat the {request}"
        else:
            return super().handle(request)


def client_code(handler: Handler) -> None:
    for food in ["Nut", "Banana", "Cup of coffee"]:
        print(f"\nClient: Who wants a {food}?")
        result = handler.handle(food)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  {food} was left untouched.", end="")


if __name__ == "__main__":
    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()

    monkey.set_next(squirrel).set_next(dog)

    print("Chain: Monkey > Squirrel > Dog")
    client_code(monkey)
    print("\n")

    print("Subchain: Squirrel > Dog")
    client_code(squirrel)



