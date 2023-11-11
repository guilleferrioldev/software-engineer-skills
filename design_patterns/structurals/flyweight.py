"""
Flyweight is a structural design pattern that allows you to keep more objects within the available amount of RAM
sharing common parts of state between multiple objects instead of keeping all information in each object

# Use cases
- use the Flyweight pattern only when your program must support a huge number of objects that barely fit in the
Available RAM.

# How to implement it
1. Split the fields of a class that will be converted to flyweight into two parts:
-intrinsic state: fields that contain invariant information duplicated across multiple objects
-extrinsic state: fields that contain contextual information unique to each object

2. Leave the fields that represent intrinsic state in the class, but make sure they are immutable. They must bring their
initial values only within the constructor.

3. Review methods that use extrinsic state fields. For each field used in the method, enter a new
parameter and use it instead of the field.

4. Optionally, create a factory class to manage the group of flyweight objects, searching for an existing one before creating one
new. Once the factory is in place, customers will only need to order flyweight items through it. They must
describe the desired flyweight by passing its intrinsic state to the factory.

5. The client must store or calculate values of the extrinsic state (context) in order to invoke methods of flyweight objects.
For convenience, the extrinsic state can be moved to a separate context class along with the flyweight referrer field.

# Pros and cons
p- You can save a lot of RAM, as long as your program has tons of similar objects.

c- You may be exchanging RAM for CPU cycles when some context information must be recalculated each time.
Someone invoke a flyweight method.

c- The code becomes very complicated. New team members will always be wondering why the state of an entity is
separated in such a way.
"""

import json
from typing import Dict

class Flyweight():
    def __init__(self, shared_state: str) -> None:
        self._shared_state = shared_state

    def operation(self, unique_state: str) -> None:
        s = json.dumps(self._shared_state)
        u = json.dumps(unique_state)
        print(f"Flyweight: Displaying shared ({s}) and unique ({u}) state.", end="")


class FlyweightFactory():
    _flyweights: Dict[str, Flyweight] = {}

    def __init__(self, initial_flyweights: Dict) -> None:
        for state in initial_flyweights:
            self._flyweights[self.get_key(state)] = Flyweight(state)

    def get_key(self, state: Dict) -> str:
        return "_".join(sorted(state))

    def get_flyweight(self, shared_state: Dict) -> Flyweight:
        key = self.get_key(shared_state)

        if not self._flyweights.get(key):
            print("FlyweightFactory: Can't find a flyweight, creating new one.")
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print("FlyweightFactory: Reusing existing flyweight.")

        return self._flyweights[key]

    def list_flyweights(self) -> None:
        count = len(self._flyweights)
        print(f"FlyweightFactory: I have {count} flyweights:")
        print("\n".join(map(str, self._flyweights.keys())), end="")


def add_car_to_police_database(factory: FlyweightFactory, plates: str, owner: str,
                                brand: str, model: str, color: str) -> None:
    print("\n\nClient: Adding a car to database.")
    flyweight = factory.get_flyweight([brand, model, color])
    flyweight.operation([plates, owner])


if __name__ == "__main__":
    factory = FlyweightFactory([
        ["Chevrolet", "Camaro2018", "pink"],
        ["Mercedes Benz", "C300", "black"],
        ["Mercedes Benz", "C500", "red"],
        ["BMW", "M5", "red"],
        ["BMW", "X6", "white"],
    ])

    factory.list_flyweights()

    add_car_to_police_database(
        factory, "CL234IR", "James Doe", "BMW", "M5", "red")

    add_car_to_police_database(
        factory, "CL234IR", "James Doe", "BMW", "X1", "red")

    print("\n")

    factory.list_flyweights()

