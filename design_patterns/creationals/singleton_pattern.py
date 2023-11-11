"""
Singleton is a creational design pattern that allows us to ensure that a class has a single instance, while also providing a
global access point to said instance.

# Applicability
- Use the Singleton pattern when a class in your program should only have one instance available to all clients; For example,
a single database object shared by different parts of the program.

- Use the Singleton pattern when you need stricter control of global variables.

# How to implement it
1. Add a private static field to the class to store the Singleton instance.

2. Declare a public static create method to get the Singleton instance.

3. Implement lazy initialization inside the static method. You should create a new object on your first call and place it inside the
static field. The method must always return that instance in all subsequent calls.

4. Declare the class constructor as private. The static method of the class will still be able to invoke the constructor, but not the
other objects.

5. Review the client code and replace all direct calls to the Singleton instance's constructor with calls to its static creation method.

# Pros and cons
p- You can be certain that a class has a single instance.

p- You get a global access point to said instance.

p- The Singleton object is only initialized when it is required for the first time.

c- Violates the Principle of single responsibility. The pattern solves two problems at the same time.

c- The Singleton pattern can mask bad design, for example, when program components know too much about each other.

c- The pattern requires special treatment in an environment with multiple threads of execution, so that multiple threads do not create a Singleton object
repeatedly.

c- It can be difficult to unit test Singleton client code because many testing frameworks depend on inheritance
when creating mock objects. Because the Singleton class is private and in most languages ​​it is impossible to
overriding static methods, you'll have to think of an original way to simulate the Singleton. Or, just don't write the tests. Or don't use
the Singleton pattern.
"""

# Java implementation
class User(object):
    __instance = None
    
    def __new__(cls):
        if User.__instance is None:
            print("Nueva instancia")
            User.__instance = object.__new__(cls)

        return User.__instance 


# Pythonic implementation
def singleton(cls):
    __instances = dict()
    
    def wrapper(*args, **kwargs):
        if cls not in __instances:
            __instances[cls] = cls(*args, **kwargs)
        return __instances[cls]

    return wrapper


@singleton
class Usuario(object):
    def __init__(self, username):
        self.username = username



# Implementation with metaclasses
class SingletonMeta(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            instance = super().__call__(*args, **kwargs)
            cls.__instances[cls] = instance
        return cls.__instances[cls]


class Businessman(metaclass=SingletonMeta):
    def __init__(self, amount: int) -> None:
        self.amount = amount
    
    def some_business_logic(self):
        pass

if __name__ == "__main__":
    User1 = User()
    User2 = User()
    
    print(User1 == User2)

    Usuario1 =  Usuario("G")
    Usuario2 =  Usuario("F")
    
    print(Usuario1.username)
    print(Usuario2.username)
    
    s1 = Businessman(500)
    s2 = Businessman(200)
    
    print(s1.amount)
    print(s2.amount)

    


