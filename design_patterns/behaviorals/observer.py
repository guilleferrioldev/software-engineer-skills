"""
Observer is a behavioral design pattern that allows you to define a subscription mechanism to notify multiple
objects about any event that happens to the object they are observing.

# Use cases
- Use the Observer pattern when changes to the state of one object may need to change other objects and the group of objects.
objects be unknown in advance or change dynamically.

- Use the pattern when some objects in your application must observe others, but only for a limited time or in cases
specific.

# How to implement it
1. Review your business logic and try to divide it into two parts: the core functionality, independent of the rest of the code,
will act as notifier; the rest will become a group of subscriber classes.

2. Declare the subscriber interface. At a minimum, you must declare a single update method.

3. Declare the notifier interface and describe a pair of methods to add and remove a subscriber object from the list. Remember
that notifiers should work with subscribers only through the subscriber interface

4. Decide where to place the subscription list and the implementation of subscription methods. Typically, this code has the
same look for all notifier types, so the obvious place to put it is in a derived abstract class
directly from the notifying interface. Concrete notifiers extend that class, inheriting the behavior of
subscription.

5. Create concrete notifier classes. Every time something important happens within a notifier, you must notify everyone
their subscribers.

6. Implement the update notification methods in specific subscriber classes. The majority of subscribers
They will need some context information about the event, which can be passed as an argument to the notify method.

# Pros and cons
p- Open/closed principle. You can introduce new subscriber classes without having to change the notifier code
(and vice versa if there is a notifying interface).

p- You can establish relationships between objects during runtime.

c- Subscribers are notified in a random order.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class ConcreteSubject(Subject):
    _state: int = None
    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        print("\nSubject: I'm doing something important.")
        self._state = randrange(0, 10)

        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()


class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass

class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state < 3:
            print("ConcreteObserverA: Reacted to the event")


class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 0 or subject._state >= 2:
            print("ConcreteObserverB: Reacted to the event")


if __name__ == "__main__":
    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(observer_a)

    subject.some_business_logic()










