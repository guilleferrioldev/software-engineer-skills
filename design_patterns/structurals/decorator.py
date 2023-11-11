"""
Decorator is a structural design pattern that allows you to add functionality to objects by placing these objects inside encapsulating objects.
specials that contain these functionalities.

#Use cases
- Use the Decorator pattern when you need to assign additional functionality to objects at runtime without breaking the code that
use those objects.

- Use the pattern when it is strange or it is not possible to extend the behavior of an object using inheritance.

# How to implement it
1. Make sure your business domain can be represented as a parent component with several optional layers on top.

2. Decide which methods are common to the parent component and optional layers. Create a component interface and declare those methods in it

3. Create a concrete component class and define the base behavior in it.

4. Create a decorator base class. You must have a field to store a reference to a wrapped object. The field must be declared with the interface type
component to allow linking to specific components as well as decorators. The base decorator class must delegate all operations
to the wrapped object.

5. Make sure all classes implement the component interface.

6. Create concrete decorators by extending them from the base decorator. A particular decorator must execute its behavior before or after the
call to the parent method (which always delegates to the wrapped object).

7. The client code should be responsible for creating decorators and composing them in the way the client needs.

# Pros and cons
p- You can extend the behavior of an object without creating a new subclass.

p- You can add or remove responsibilities from an object during runtime.

p- You can combine several behaviors by wrapping an object with several decorators.

p- Principle of single responsibility. You can split a monolithic class that implements many possible variants of behavior into multiple classes.
smaller.

c- It is difficult to remove a specific wrapper from the wrapper stack.

c- It is difficult to implement a decorator in such a way that its behavior does not depend on the order in the decorator stack.

c- The initial configuration code for the layers may have an unpleasant appearance.
"""


class Component():
    def operation(self) -> str:
        pass


class ConcreteComponent(Component):
    def operation(self) -> str:
        return "ConcreteComponent"


class Decorator(Component):
    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:
        return self._component

    def operation(self) -> str:
        return self._component.operation()


class ConcreteDecoratorA(Decorator):
    def operation(self) -> str:
        return f"ConcreteDecoratorA({self.component.operation()})"


class ConcreteDecoratorB(Decorator):
    def operation(self) -> str:
        return f"ConcreteDecoratorB({self.component.operation()})"


def client_code(component: Component) -> None:
    print(f"RESULT: {component.operation()}", end="")


if __name__ == "__main__":
    simple = ConcreteComponent()
    print("Client: I've got a simple component:")
    client_code(simple)
    print("\n")

   
    decorator1 = ConcreteDecoratorA(simple)
    decorator2 = ConcreteDecoratorB(decorator1)
    print("Client: Now I've got a decorated component:")
    client_code(decorator2)
