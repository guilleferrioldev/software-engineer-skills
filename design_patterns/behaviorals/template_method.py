"""
Template Method is a behavioral design pattern that defines the skeleton of an algorithm in the superclass but allows
that subclasses override steps of the algorithm without changing its structure.

# Use cases
- Use the Template Method pattern when you want to allow your clients to extend only particular steps of a
algorithm, but not the entire algorithm or its structure.

- Use the pattern when you have many classes that contain almost identical algorithms, but with some minor differences.
As a result, you may have to modify all classes when the algorithm changes.

# How to implement it
1. Analyze the target algorithm to see if you can break it down into steps. Consider which steps are common to all subclasses and
which will always be unique.

2. Create the abstract base class and declare the template method and a group of abstract methods that represent the steps of the
algorithm. Outlines the structure of the algorithm in the template method by executing the corresponding steps. Consider declaring
the template method as final to prevent subclasses from overriding it.

3. There is no problem if all the steps end up being abstract. However, some steps could benefit from having a
default implementation. Subclasses do not have to implement those methods.

4. Consider adding hooks between crucial steps of the algorithm.

5. For each variation of the algorithm, create a new concrete subclass. This must implement all the abstract steps, but
You can also override some of the optional ones.

# Pros and cons
p- You can allow clients to overwrite only certain parts of a large algorithm, so that they are less affected by the
changes that take place in other parts of the algorithm.

p- You can place the duplicate code inside a superclass.

c-Some clients may be limited by the provided skeleton of an algorithm.

c- You may violate the Liskov substitution principle by suppressing a default implementation of a pass through a
subclass.

c- Template methods tend to be more difficult to maintain the more steps they have.
"""

from abc import ABC, abstractmethod

class AbstractClass(ABC):
    def template_method(self) -> None:
        self.base_operation1()
        self.required_operations1()
        self.base_operation2()
        self.hook1()
        self.required_operations2()
        self.base_operation3()
        self.hook2()

    def base_operation1(self) -> None:
        print("AbstractClass says: I am doing the bulk of the work")

    def base_operation2(self) -> None:
        print("AbstractClass says: But I let subclasses override some operations")

    def base_operation3(self) -> None:
        print("AbstractClass says: But I am doing the bulk of the work anyway")

    @abstractmethod
    def required_operations1(self) -> None:
        pass

    @abstractmethod
    def required_operations2(self) -> None:
        pass

    def hook1(self) -> None:
        pass

    def hook2(self) -> None:
        pass


class ConcreteClass1(AbstractClass):
    def required_operations1(self) -> None:
        print("ConcreteClass1 says: Implemented Operation1")

    def required_operations2(self) -> None:
        print("ConcreteClass1 says: Implemented Operation2")


class ConcreteClass2(AbstractClass):
    def required_operations1(self) -> None:
        print("ConcreteClass2 says: Implemented Operation1")

    def required_operations2(self) -> None:
        print("ConcreteClass2 says: Implemented Operation2")

    def hook1(self) -> None:
        print("ConcreteClass2 says: Overridden Hook1")


def client_code(abstract_class: AbstractClass) -> None:
    abstract_class.template_method()


if __name__ == "__main__":
    print("Same client code can work with different subclasses:")
    client_code(ConcreteClass1())
    print("")

    print("Same client code can work with different subclasses:")
    client_code(ConcreteClass2())
