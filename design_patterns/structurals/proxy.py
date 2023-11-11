"""
Proxy is a structural design pattern that allows you to provide a substitute or placeholder for another object.
A proxy controls access to the original object, allowing you to do something before or after the request reaches the object
original.

# Use cases
- Lazy initialization (virtual proxy). It is when you have a very heavy duty object that uses a lot of resources of the
system by always being running, even if you only need it from time to time.

- Access control (proxy protection). This is when you want only specific clients to be able to use the
service object, for example, when your objects are fundamental parts of an operating system and the clients are several
launched applications (including malicious ones).

- Local execution of a remote service (remote proxy). It is when the service object is located on a remote server.

- Registration requests (registration proxy). It is when you want to maintain a history of requests to the service object.

- Cached request results (cache proxy). This is when you need to cache results of client requests
and manage the life cycle of that cache, especially if the results are many.

- Smart reference. This is when you should be able to dispose of a heavy object once there are no customers using it.

# How to implement it
1. If there is no pre-existing service interface, create one so that the proxy and service objects are interchangeable.
It is not always possible to extract the interface from the service class, because you have to change all the clients of the service
to use that interface. Plan B consists of converting the proxy into a subclass of the service class, so that it inherits the
service interface.

2. Create the proxy class. You must have a field to store a reference to the service. Typically proxies create and manage
the complete life cycle of your services. In rare cases, the client passes a service to the proxy through a constructor.

3. Implement the proxy methods according to your purposes. In most cases, after doing some work, the proxy
You should delegate the work to a service object.

4. Consider introducing a create method that decides whether the client gets a proxy or a real service. It may be a
Simple static method in the proxy class or a whole factory method.

5. Consider implementing lazy initialization for the service object.

# Pros and cons
p- You can control the service object without the clients knowing.

p- You can manage the life cycle of the service object when customers don't care.

p- The proxy works even if the service object is not ready or available.

p- Open/closed principle. You can introduce new proxies without changing the service or clients.

c- The code can get complicated since you must introduce a large number of new classes.

c- The service response may be delayed.
"""


from abc import ABC, abstractmethod

class Subject(ABC):

    @abstractmethod
    def request(self) -> None:
        pass


class RealSubject(Subject):
    def request(self) -> None:
        print("RealSubject: Handling request.")


class Proxy(Subject):
    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def request(self) -> None:
        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self) -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self) -> None:
        print("Proxy: Logging the time of request.", end="")


def client_code(subject: Subject) -> None:
    subject.request()


if __name__ == "__main__":
    print("Client: Executing the client code with a real subject:")
    real_subject = RealSubject()
    client_code(real_subject)

    print("")

    print("Client: Executing the same client code with a proxy:")
    proxy = Proxy(real_subject)
    client_code(proxy)