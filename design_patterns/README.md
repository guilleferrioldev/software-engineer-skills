# Design Patterns
Design patterns are reusable solutions to common problems that arise when designing software. These patterns represent best practices, proven schemes, and general solutions for recurring situations in software development. Design patterns are not code or libraries that can be copied and pasted into an application, but rather guidelines that help developers address common design problems in a structured and efficient way.

## Creationals
- [Factory Design Pattern](./creationals/factory_pattern.py): Used to create objects of a specific type without exposing the creation logic to the client, without specifying the exact class of the object to be created. In essence, it provides an interface for creating instances of a class, but allows subclasses to alter the type of objects to be created. It focuses on creating an instance of a specific class, delegating implementation to subclasses. 
    1. **Product:** It is the interface or base class of the objects that the Factory pattern can create.

    2. **Producer:** It is the class that contains the factory method. This method is responsible for instantiating the concrete object based on certain criteria.

    3. **Concrete Product:** These are the actual classes that implement the Product interface and are created by the Producer.

- [Abstract Factory Design Pattern](./creationals/abstract_factory_pattern.py): Provides an interface for creating families of related or dependent objects without specifying their concrete classes. This means that the client does not need to worry about how the objects are created, but simply interacts with the interface provided by the abstract factory.

    1. **Abstract Factory**: Defines an interface to create different types of objects within a product family.

    2. **Concrete factories**: They implement the Abstract Factory interface to create concrete objects of the product family.

    3. **Abstract products**: These are the interfaces for different types of products that will be created by the abstract factory.

    4. **Concrete products**: These are the concrete implementations of the defined abstract products. Each product family has its own specific product implementations.


- [Builder Design Pattern](./creationals/builder_pattern.py): Used to build a complex object step by step. It allows the creation of different variants of an object without the need to expose its internal representation. Instead of using a constructor with a large number of parameters, the Builder pattern uses a builder object to build the object step by step and then return the final product. 
    1. **Product**: It is the complex object that is being built. In the context of the Builder pattern, this is the final product you get after applying all the builds and configurations.

    2. **Builder**: It is an interface or an abstract class that defines the steps necessary to build the product. This interface or class provides methods to build the different parts of the product.

    3. **ConcreteBuilder**: This is a concrete implementation of the Builder interface. The ConcreteBuilder class implements the methods defined in the Builder interface to build and assemble the different parts of the product.

    4. **Director**: Optionally, a Director can be used to oversee the build process, providing a specific flow to build the product.

    5. **Client**: It is the code that the Builder pattern uses to build the product. The client interacts with the Builder and, optionally, the Director to build the complex object.


- [Singleton Design Pattern](./creationals/singleton_pattern.py): Ensures that a class has a single instance and provides a global access point to that instance.
    1. **Singleton Class**: It is the class for which it is guaranteed that there is only one instance. This class usually provides a static method to obtain the single instance, and the constructor of the class is usually private to avoid creating additional instances.

    2. **Single instance**: It is the only instance of the Singleton class that the pattern guarantees. This instance is shared by all clients that request it.

    3. **Global hotspot**: The static method provided by the Singleton class that allows clients to obtain the single instance of the class.


- [Prototype Design Pattern](./creationals/prototype_pattern.py): Used to create new objects by duplicating an existing object, known as a prototype. This pattern focuses on creating new objects by cloning existing objects, which avoids creating objects using a constructor.
    1. **Prototype**: It is the interface that declares the cloning method. It can be an interface or an abstract class that defines the clone or duplicate method.

    2. **Prototype Concrete Class**: Implements the Prototype interface and provides the implementation for the clone method.

    3. **Client**: Use the prototype to create new objects by invoking the clone method. This client may be part of the application that needs to create new objects based on existing prototypes.


## Structurals
- [Adapter Design Pattern](./structurals/adapter.py): Allows incompatible interfaces to work together.
    1. **Target**: Defines the domain-specific interface that the client uses. In other words, it is the interface that the client expects the adapter to adapt to.

    2. **Client**: It is the one that uses the Target interface to interact with the adapter object.

    3. **Adaptee**: It is the existing interface that needs to be adapted to work with the client. In general, the client cannot directly use this interface due to incompatibilities.

    4. **Adapter**: Implements the "Target" interface and maintains a reference to the "Adapter" object. It acts as an intermediary that translates the client's calls to the corresponding operations on the adapter.

- [Bridge Design Pattern](./structurals/bridge.py): Separates an abstraction from its implementation so that they can vary independently.
    1. **Abstraction**: Defines the high-level interface that the client uses to interact. This interface contains references to objects of type Implementor and is independent of the concrete implementation.

    2. **RefinedAbstraction**: Extends the Abstraction interface by defining more refined behaviors.

    3. **Implementor**: Defines the interface for the implementation of the concrete implementation classes. This interface does not have to match the Abstraction interface. Instead, both interfaces can differ and therefore completely separate the abstraction from the implementation.

    4. **ConcreteImplementor**: Implements the Implementor interface and provides a concrete implementation of the interface.

- [Composite Design Pattern](./structurals/composite.py): Combine objects into tree structures to represent part-whole hierarchies. It allows clients to treat both individual objects and compositions of objects uniformly.
    1. **Component**: Defines the interface for simple and compound objects in the structure. It can be an interface or an abstract class that declares operations common to all elements in the structure.

    2. **Leaf**: Represents the final nodes in the structure. It implements the component interface and has no children.

    3. **Composite**: Represents the internal nodes in the structure. Contains leaves and/or other composites. Implements the component interface

- [Decorator Design Pattern](./structurals/decorator.py): Allows adding additional behavior to objects individually, dynamically and transparently to the client.
    1. **Component**: Defines the interface for objects that can receive decorations.

    2. **Concrete Component**: Implements the component interface and defines the base object to which decorations can be added.

    3. **Decorator**: It is an abstract class that also implements the component interface. Contains a reference to a component object. This class has the ability to wrap or nest an operation with additional behavior before or after the call to the wrapped component.

    4. **Concrete Decorator**: Extends the decorator and adds additional behavior to objects.

- [Facade Design Pattern](./structurals/facade.py): Provides a unified interface for a set of interfaces of a subsystem. This makes the subsystem easier to use by providing a higher-level interface.
    1. **Facade**: Provides a unified interface for a set of interfaces in a subsystem. This facade knows which subsystem classes are responsible for making a request and delegates the request to the corresponding subsystem object.

    2. **Subsystem**: Consists of one or more classes that implement specific functionality. The facade does not directly implement the functionality, but instead delegates requests to subsystem objects.

- [Flyweight Design Pattern](./structurals/flyweight.py): Used when we need to minimize memory or processing usage when handling a large number of objects that share identical characteristics.
    1. **Flyweight**: It is an interface or abstract class that defines the operations that can be shared. Flyweight objects represent the intrinsic (shared) characteristics of the object.

    2. **Concrete Flyweight**: Implements the flyweight interface and stores the intrinsic state part. This object must be shared and reused.

    3. **Flyweight Factory**: It is a factory that manages flyweight objects. It ensures that flyweights are shared efficiently, meaning that when a client requests a flyweight, the factory provides it if it already exists, or creates a new one if not.

    4. **Client**: Uses flyweight objects, but can also contain extrinsic state (that is, the part that is not shared and is specific to the client instance).
    

- [Proxy Design Pattern](./structurals/proxy.py): Introduces an intermediary or substitute to control access to an object, allowing additional functionality to be added, such as late creation management, access control, registration, among others:
    1. **Subject**: Defines the common interface for both the real object and the proxy, so that the proxy can be used anywhere the real object is expected.

    2. **Proxy**: Maintains a reference to the real object so that additional tasks can be performed when the real object is accessed. It implements the same interface as the subject, allowing it to be used in place of the actual object.
        - Remote Proxy: Manages communication with a remote object.
   
        - Virtual Proxy: Controls the late creation of a heavy object until it is absolutely necessary.
   
        - Protection Proxy: Controls access to the real object based on permissions or access restrictions.

    3. **Real Object**: It is the original object to which the proxy provides controlled access.

## Behaviorals
- [Chain of Responsibility Design Pattern](./behaviorals/chain_of_responsibility.py): Allows multiple objects to handle a request without explicitly knowing the details of the request or the other handlers.
    1. **Handler**: Defines an interface to handle requests and maintain a reference to the next handler in the chain. This can be an abstract class or an interface.

    2. **Concrete Handler**: Implements the handler interface and contains the logic to handle the request or passes the request to the next handler in the chain.

    3. **Request**: Represents the request to be handled by the handlers.

- [Command Design Pattern](./behaviorals/command.py): Encapsulates a request as an object, allowing you to parameterize clients with operations, queue requests, or perform logging operations.
    1. **Command**: Defines a common interface for all commands with a run method that executes the action associated with the command and optionally provides methods to undo the action.

    2. **Concrete Command**: Implements the command interface and stores the information necessary to execute the action. It contains a reference to one or more receivers (objects that perform the action), and makes the call to the receiver's methods when it is executed.

    3. **Invoker**: Requests that a command be executed, without knowing what specific command will be executed. Maintains a reference to the command and optionally maintains a list of executed commands.

    4. **Receiver**: Knows how to perform the action associated with a command. It performs the action when called by the specific command.

    5. **Client**: Creates a command and associates a receiver with that command before passing it to the caller to be executed.

- [Iterator Design Pattern](./behaviorals/iterator.py): Provides a way to sequentially access elements in a collection without exposing their underlying representation.
    1. **Iterator**: Defines an interface to access and traverse the elements of a collection.

    2. **Concrete Iterator**: Implements the iterator interface and keeps track of the current element in the collection during traversal.

    3. **Aggregate**: Defines an interface to create an iterator that allows iterating through the elements of the collection.

    4. **Concrete Aggregate**: Implements the aggregate interface and returns an instance of the appropriate concrete iterator.

    5. **Element**: Represents the individual elements within the collection being looped.

- [Mediator Design Pattern](./behaviorals/mediator.py): It is a behavior pattern used to reduce direct connections between components of a system, instead promoting strong coupling and allowing components to communicate through a central mediator object. This helps increase code reusability and simplify communication between components.
    1. **Mediator**: Defines an interface that components use to communicate with each other. The mediator knows and coordinates the interactions between the components.

    2. **Concrete Mediator**: Implements the mediator interface and coordinates interactions between components. This particular mediator knows the specific components that must be coordinated.

    3. **Colleague**: Represents the individual components of the system that need to communicate with each other, but do so through the mediator rather than directly communicating with each other.

- [Memento Design Pattern](./behaviorals/memento.py): Used to capture the state of an object at a certain time, so that it is possible to restore the object to that state later without violating its encapsulation. This is achieved through capturing and storing snapshots of the object's internal state, thus allowing rollback to a previous state if necessary.
    1. **Originator**: It is the object whose state you want to preserve. The Originator creates a Memento that contains a snapshot of its internal state.

    2. **Memento**: It is an object that stores the state of an Originator at a given moment. It usually contains all the data necessary to restore the Originator's state to that point in time.

    3. **Caretaker**: You are responsible for maintaining the Mementos, but do not modify them or access their content. The Caretaker acts as a kind of savings bank for the Mementos. It can also coordinate the interaction between the Originator and the Memento, although the Originator is the one that actually performs the saving and restoring state operation.

- [Observer Design Pattern](./behaviorals/observer.py): Used to define a one-to-many relationship between objects so that when an object changes state, all its dependents are automatically notified and updated. This helps maintain consistency between objects and reduce coupling in the system.
    1. **Subject**: Defines an interface for adding, deleting, and notifying observers. The Subject also maintains a list of observers to whom he notifies of any changes.

    2. **Observer**: Defines an interface to receive notifications from the Subject when its state changes. Observers register with the Subject to receive notifications.

    3. **Concrete Observer**: Implements the Observer interface to receive notifications and perform specific actions when the Subject's state changes.

    4. **Concrete Subject**: Implements the Subject interface and maintains the current state. Additionally, it notifies observers when their status changes.

- [State design pattern](./behaviorals/state.py): Allows an object to change its behavior when its internal state changes. This is achieved by defining different classes that represent the different possible states of an object, and delegating the behavior to an object that represents the current state.
    1. **Context**: Defines the interface used to interact with the state. Maintains a reference to a concrete state instance that defines the current state.

    2. **State**: Defines a common interface for all concrete states and encapsulates the behavior associated with a particular state.

    3. **Concrete States**: They implement the state interface and represent the different states in which the context can be found. Each concrete state provides the behavioral implementation associated with that particular state.

- [Strategy Design Pattern](./behaviorals/strategy.py): Allows you to define a family of algorithms, encapsulate each of them and make them interchangeable. This allows the algorithm to vary independently of the clients that use it.
    1. **Context**: It is the object that maintains a reference to a Strategy object and uses it to perform a particular operation. The context delegates the execution of the algorithm to the strategy.

    2. **Strategy**: Defines a common interface for all supported algorithms. Strategies encapsulate the specific algorithms and make them interchangeable within the context.

    3. **Concrete Strategies**: They implement the Strategy interface and provide the implementation of specific algorithms.

- [Template Method Design Pattern](./behaviorals/template_method.py): Defines the structure of an algorithm in a base class, but allows subclasses to redefine certain steps of the algorithm without changing its overall structure. This promotes code reuse and allows common behavior to be shared between classes.
    1. **Abstract Class**: Defines a template method that establishes the structure of the algorithm, including common steps and steps that can be redefined by subclasses.

    2. **Template Method**: It is a method defined in the abstract class that establishes the sequence of steps of the algorithm. This method makes use of other methods, some of which may be abstract or with the option of redefinition by subclasses.

    3. **Concrete Methods**: These are methods implemented in the abstract class or its subclasses that are used by the template method to build the algorithm.

- [Visitor Design Pattern](./behaviorals/visitor.py): Used to separate algorithms from the structure of an object on which they operate. Allows you to define a new operator or method without changing the classes of the elements on which that method operates.
    1. **Visitor**: Defines an interface that declares a visit method for each element type.

    2. **Element**: Defines an interface that allows the visitor to visit the element. Typically, this element provides a method that accepts a visitor as a parameter.

    3. **Concrete Element**: Implements the Element interface and defines a specific visitor acceptance implementation.

    4. **Object Structure**: It is a collection or structure of elements that can be visited by the visitor. Provides an interface to access its elements.


#### Credits to https://refactoring.guru/