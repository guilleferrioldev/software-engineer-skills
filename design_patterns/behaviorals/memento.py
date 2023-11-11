"""
Memento is a behavioral design pattern that allows you to save and restore the previous state of an object without revealing
the details of its implementation.

# Use cases
- Use the Memento pattern when you want to produce snapshots of the object's state in order to restore a previous state of the object.
object.

- Use the pattern when direct access to the object's fields, consultants, or modifiers violates its encapsulation.

# How to implement it
1. Determine which class will play the role of the originator. It is important to know if the program uses a central object of this type
or several smaller ones.

2. Create the memento class. One by one, declare a group of fields that reflect the fields declared within the originating class.

3. Make the memento class immutable. A memento class must accept data only once, through the constructor. The class should not
have modifiers.

4. If your programming language supports nested classes, nest the memento class inside the originator. If not, extract a
blank interface of the memento class and have the rest of the objects use it to refer to it. You can add operations
metadata to the interface, but nothing that exposes the state of the originator.

5. Add a method to produce mementos to the originating class. The originator must pass its state to the memento class via
one or more arguments to the memento constructor.

6. Add a method to restore the originator state to your class. It must accept a memento object as an argument. If you extracted
an interface in the previous step, make it the type of the parameter. In this case, you must specify the type of the incoming object when
of the memento class, since the originator needs full access to that object.

7. The caregiver, regardless of whether it represents a command object, a history, or something totally different, must know
when to request new mementos from the originator, how to store them, and when to restore the originator with a particular memento.

8. The link between caregivers and originators can move within the memento class. In this case, each moment must connect
to the originator who created it. The restore method will also be moved to the memento class. However, all this will only
meaning if the memento class is nested within the originator or the originator class provides enough modifiers
to overwrite its state.

# Pros and cons
p- You can produce snapshots of the object's state without violating its encapsulation.

p- You can simplify the originator code by allowing the caregiver to maintain the history of the originator status.

c- The application can consume a lot of RAM if clients create mementos very often.

c- Caregivers must track the life cycle of the originator to be able to destroy obsolete items.

c- Most dynamic programming languages, such as PHP, Python and JavaScript, cannot guarantee that the state within
of the moment remains intact.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters

class Originator:
    _state = None

    def __init__(self, state: str) -> None:
        self._state = state
        print(f"Originator: My initial state is: {self._state}")

    def do_something(self) -> None:
        print("Originator: I'm doing something important.")
        self._state = self._generate_random_string(30)
        print(f"Originator: and my state has changed to: {self._state}")

    @staticmethod
    def _generate_random_string(length: int = 10) -> str:
        return "".join(sample(ascii_letters, length))

    def save(self) -> Memento:
        return ConcreteMemento(self._state)

    def restore(self, memento: Memento) -> None:
        self._state = memento.get_state()
        print(f"Originator: My state has changed to: {self._state}")


class Memento(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_date(self) -> str:
        pass


class ConcreteMemento(Memento):
    def __init__(self, state: str) -> None:
        self._state = state
        self._date = str(datetime.now())[:19]

    def get_state(self) -> str:
        return self._state

    def get_name(self) -> str:
        return f"{self._date} / ({self._state[0:9]}...)"

    def get_date(self) -> str:
        return self._date


class Caretaker:
    def __init__(self, originator: Originator) -> None:
        self._mementos = []
        self._originator = originator

    def backup(self) -> None:
        print("\nCaretaker: Saving Originator's state...")
        self._mementos.append(self._originator.save())

    def undo(self) -> None:
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(f"Caretaker: Restoring state to: {memento.get_name()}")
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def show_history(self) -> None:
        print("Caretaker: Here's the list of mementos:")
        for memento in self._mementos:
            print(memento.get_name())


if __name__ == "__main__":
    originator = Originator("Super-duper-super-puper-super.")
    caretaker = Caretaker(originator)

    caretaker.backup()
    originator.do_something()

    caretaker.backup()
    originator.do_something()

    caretaker.backup()
    originator.do_something()

    print()
    caretaker.show_history()

    print("\nClient: Now, let's rollback!\n")
    caretaker.undo()

    print("\nClient: Once more!\n")
    caretaker.undo()

