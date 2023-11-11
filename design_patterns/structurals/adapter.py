"""
Adapter is a structural design pattern that allows collaboration between objects with incompatible interfaces.

# Use cases
- Use the adapter class when you want to use an existing class, but whose interface is not compatible with the rest of the code.

- Use the pattern when you want to reuse several existing subclasses that lack some common functionality that cannot be added to the superclass

# How to implement it
1. Make sure you have at least two classes with incompatible interfaces

2. Declare the interface to the client and describe how the client classes communicate with the service class.

3. Create the adapter class and make it follow the interface with the client. Leave all methods empty for now.

4. Add a field to the adapter class to store a reference to the service object. Common practice is to initialize this field through the
constructor, but sometimes it is appropriate to pass it to the adapter when its methods are invoked.

5. One by one, implement all the methods of the client interface in the adapter class. The adapter class should delegate most of the
actual work to the service object, managing only the interface or the format conversion of the data.

6. Client classes must use the adapter class through the interface with the client. This will allow you to change or extend classes
adapters without affecting the client code.


# Pros and cons
p- Principle of single responsibility. You can separate the interface or data conversion code from the primary business logic of the program.

p- Open/closed principle. You can introduce new types of adapters to the program without breaking existing client code, as long as
when working with adapters through the client interface.

c- The overall complexity of the code increases, since you must introduce a group of new interfaces and classes. Sometimes it is easier
change the service class so that it matches the rest of your code.
"""


class Target:
    def request(self) -> str:
        return "Target: The default target's behavior."


class Adaptee:
    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target, Adaptee):
    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"


def client_code(target: "Target") -> None:
    print(target.request(), end="")


if __name__ == "__main__":
    print("Client: I can work just fine with the Target objects:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Client: The Adaptee class has a weird interface. "
          "See, I don't understand it:")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Client: But I can work with it via the Adapter:")
    adapter = Adapter()
    client_code(adapter)
