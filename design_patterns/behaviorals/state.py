"""
State is a behavioral design pattern that allows an object to alter its behavior when its internal state changes.
It looks like the object changes its class.

# Use cases
- Use the State pattern when you have an object that behaves differently depending on its current state, the number of
states is huge and the state-specific code changes frequently.

- Use the pattern when you have a class contaminated with huge conditionals that alter the way the class behaves
according to the current values ​​of the class fields.

- Use the State pattern when you have a lot of code duplicated by similar states and state machine transitions
based on conditions.

# How to implement it
1. Decide which class will act as context. It can be an existing class that already has the state-dependent code, or a new one
class, if the state-specific code is distributed across several classes.

2. Declare the state interface. Although you can replicate all methods declared in the context, focus on the ones that can.
contain state-specific behaviors.

3. For each current state, create a class derived from the state interface. Then go through the context methods and extract everything
the code related to that state to put it in your newly created class.

When you move your code to the state class, you may discover that it depends on private members of the context. There are several solutions
alternatives:
- Make those fields or methods public.
- Convert the behavior you are extracting to a public method in the context and call it from the class
state. This way is unpleasant but fast and you can always fix it later.
- Nest state classes in the context class, but only if your programming language supports nested classes.

4. In the context class, add a reference field of the state interface type and a public setter that allows
overwrite the value of that field.

5. Go through the context method again and replace empty state conditionals with corresponding method calls
of the state object.

6. To change the state of the context, create an instance of one of the state classes and pass it to the context class. Can
Do this within the context class itself, in different states, or on the client. Whether it is done one way or another, the class
becomes dependent on the concrete state class it instantiates.

# Pros and cons
p- Principle of single responsibility. Organizes code related to particular states into separate classes.

p- Open/closed principle. Introduces new states without changing existing state classes or the context class.

p- Simplifies the context code by eliminating bulky state machine conditionals.

c- Applying the pattern may be excessive if a state machine only has a few states or rarely changes.
"""

from __future__ import annotations
from abc import ABC, abstractmethod

class Context:
    _state = None    

    def __init__(self, state: State) -> None:
        self.transition_to(state)

    def transition_to(self, state: State):
        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    def request1(self):
        self._state.handle1()

    def request2(self):
        self._state.handle2()


class State(ABC):
    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def handle1(self) -> None:
        pass

    @abstractmethod
    def handle2(self) -> None:
        pass

class ConcreteStateA(State):
    def handle1(self) -> None:
        print("ConcreteStateA handles request1.")
        print("ConcreteStateA wants to change the state of the context.")
        self.context.transition_to(ConcreteStateB())

    def handle2(self) -> None:
        print("ConcreteStateA handles request2.")


class ConcreteStateB(State):
    def handle1(self) -> None:
        print("ConcreteStateB handles request1.")

    def handle2(self) -> None:
        print("ConcreteStateB handles request2.")
        print("ConcreteStateB wants to change the state of the context.")
        self.context.transition_to(ConcreteStateA())


if __name__ == "__main__":
    context = Context(ConcreteStateA())
    context.request1()
    context.request2()



