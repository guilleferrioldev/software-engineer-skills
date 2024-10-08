# General Concepts

---
## 1- Programming languages
###  Basic concepts
- **Syntax**: Syntax refers to the rules and grammatical structures of the language that define how things should be written instructions in the code.

- **Semantics**: Semantics refers to the meaning of the instructions written in the code.

- **Data types**: Programming languages ​​have different data types such as integers, floats, strings, booleans, etc.

- **Control structures**: Control structures, such as loops and conditionals, allow you to control the flow of program execution.

- **Functions**: Functions allow a set of instructions to be encapsulated so that they can be reused in different parts of the program.

- **Data structures**: Programming languages ​​offer various data structures, such as arrays, lists, dictionaries, sets, among others, that allow you to organize and manipulate data efficiently.

- **Variables and assignment**: Variables allow you to store and manipulate data in the code. Assignment refers to the action of assign a value to a variable.

- **Operators**: Operators are special symbols that perform operations on data. These include arithmetic operators (addition, subtraction, multiplication, division), comparison operators (equality, greater than, less than), logical operators (AND, OR, NOT), among others

- **Error handling**: Programming languages ​​allow you to control and handle errors through the use of mechanisms such as exceptions, try-catch, or error handling in a more controlled way.

- **Input/Output**: How the language handles input of data from the user or from a file, and output of data to the screen or a file.

- **Reference counting**: Refers to the number of times a given entity (such as an object, a variable, or a piece of information) is referenced in a given context. In the context of programming, reference counting can be applied to variables, objects, or other elements within the code.

### Typing
- **Typing**: Refers to the concept of assigning data types to variables, function parameters, expressions, among other elements in a programming language.

- **Static typing**: Refers to the declaration and verification of data types at compile time. This means that in a statically typed programming language, data types must be specified before using a variable or function, and the compiler will check whether they are being used according to their declared types. If there are any type errors, the compiler will detect them before the program is executed.

- **Dynamic typing**: Refers to the ability of a language to automatically determine the data type of a variable at run time. In a dynamically typed language, it is not necessary to explicitly declare the type of a variable before using it, since the type is automatically inferred based on the value assigned to it.

- **Strong typing**: Refers to restricting operations between different types of data in a programming language. In a strongly typed language, conversions between data types are not done implicitly, which means that operations between incompatible types generate errors. This helps prevent errors and ensures that operations are performed only between compatible data types.

- **Weak typing**: Refers to the flexibility to perform operations between different types of data in a programming language. In a weakly typed language, implicit data type conversions can be performed, which means that operations between incompatible types can be performed without errors, as the language will attempt to automatically convert data types as necessary, resulting in which can lead to unexpected results if you are not careful.

- **Type inference**: It is a process in which a programming language automatically deduces the type of an expression rather than requiring the programmer to specify it explicitly.

- **Duck typing**: "If it walks like a duck and quacks like a duck, then it must be a duck" sums up the concept well. In programming terms, this means that if an object has specific methods or behaviors, it can be treated as if it belongs to a certain interface or type, even if it does not explicitly inherit from that type. The idea is that if an object behaves in a certain way, then it can be treated as if it were of a particular type, regardless of its actual type.

### Compilation
- **Compiler**: A compiler is a tool that translates the source code of a programming language into object code in the target language. The compiler performs lexical analysis, syntactic analysis, semantic analysis, code optimization, and code generation as part of this process. During lexical analysis, the compiler breaks the code into tokens such as identifiers, keywords, operators, etc. Grammatical analysis checks whether the program structure follows the syntactic rules of the language. Semantic analysis verifies that the language rules are followed and makes certain optimizations to improve the performance of the code. Finally, the compiler generates machine code based on the result of all these analyzes

- **Compiled language**: It is a type of programming language whose source code is directly translated into executable code before execution.

- **Interpreter**: It is a computer program that reads and executes instructions written in a high-level programming language. It works by reading the source code line by line and translating it into a low-level executable format. Unlike a compiler, which translates the entire program at once, an interpreter performs the translation and execution of instructions in real time. The interpreter usually includes a runtime environment that facilitates interaction with the source code, error handling, and system resource management.

- **Interpreted language**: is a type of programming language whose source code is not compiled directly into executable code, but is instead interpreted and executed line by line by an interpreter. In other words, instead of compiling the code into an executable file, the interpreter reads the source code and executes it directly.

- **Linker**: It is a compilation process tool in programming that is used to combine multiple object files generated during compilation into a single executable program. This involves resolving references to functions, variables, and other symbols defined in separate modules and binding them to specific memory addresses in the final program. It is responsible for taking all the previously compiled code fragments and assembling them into a single executable that can be loaded and executed by the operating system.

- **Compilation errors**: These are problems found during the process of translating source code into machine code. These errors occur when the compiler encounters instructions that violate the syntax of the programming language or when there are mistakes in the semantics of the code. This means that the compiler cannot convert the source code into an executable program due to errors in the code.

- **Garbage collector**: It is a component of many programming languages ​​that is responsible for managing the memory used by a program. Its main function is to free memory that is no longer being used by the program, which helps prevent memory leaks and makes programs more efficient in using resources. When a program creates objects or variables in memory, the garbage collector is responsible for monitoring which of these elements are no longer accessible from the program, either because they are out of scope or because they are no longer needed. Once it determines that certain elements are not reachable, the garbage collector is responsible for freeing the memory occupied by these elements, allowing it to be reused by the program for other purposes.

- **Just-In-Time(JIT) compilation**: It is an approach in which the source code is compiled at runtime, that is, just before it is executed. Instead of compiling all of a program's code before running it (as in the case of static compilation), JIT compiles parts of the code as they are needed during program execution. This can lead to more efficient program execution as the compiled code adapts to the conditions of the execution environment in real time.

- **Compile time** refers to the process in which source code written by the programmer is converted into code executable by the computer. During compilation, the compiler checks the syntax and structure of the code for errors before producing the executable program. In short, it is the process of translating source code into a format that the machine can understand and execute.

- **Runtime** refers to the period in which the compiled program is running and performing its functions on the computer. During this time, the program interacts with the operating system, hardware, and other programs in real time. This is where the actual behavior of the program is observed and logical or other errors may arise.

- **Reflection**: Refers to the ability of a program to examine and modify its own structure and behavior during runtime. This means that a program can inspect and manipulate its own classes, methods, attributes, and other components at run time. This opens the door to a series of advanced functionalities, such as the dynamic creation of class instances, the dynamic invocation of methods, the inspection of the structure of objects, the manipulation of attributes, among others.

- **Cross-compilation**: It is the process of compiling a program so that it runs on a different platform than the one on which the compilation is being performed. This means that the code is compiled on a different architecture or operating system than the one that will be used to run the resulting program.

- **Dependencies and Libraries**: Dependencies are the set of external components necessary for a project to work, while libraries are sets of code that provide specific functionality and that can be used by a project to simplify development and programming.

- **Makefiles**: These are configuration files used in build systems to automate the software compilation process. A Makefile contains rules that specify how to combine source files to produce executable programs or other files.

- **Construction systems**: These are tools that facilitate the automation of the software construction process. These systems manage dependencies between different software components, such as source files and libraries, and ensure that files are compiled in the correct order.

---
## 2- General concepts
- **Scope**: Refers to the scope or visibility that a variable has within a program. Defines where in the code a variable can be used and accessed. The scope of a variable can be global, meaning that it can be accessed from anywhere in the program, or local, meaning that it can only be accessed within a specific portion of the code, such as a function or a block of code. 

- **Mutability**: Refers to the ability of an object to change or modify its state after its creation.

- **Parameter by reference**: It is a type of parameter in programming that allows a function to directly access and modify the value of a variable in memory, instead of operating on a copy of the value. This means that any modification made to the parameter by reference inside the function will directly affect the original value of the variable outside the function.

- **Parameter by value** : When a parameter by value is passed to a function, a copy of the actual value is passed to the function parameter. This means that any modifications made to the parameter inside the function will not affect the original value outside the function.

- **Serialization**: Refers to the process of converting an object or data structure into a format that can be stored or transmitted, and then reconstructed. It allows you to convert complex data into a form that can be saved or sent efficiently, and then restore it to its original form when necessary.

- **Enumerable**: Refers to a collection of elements that can be enumerated or counted. In many programming languages, enumerables are used to represent collections of elements such as lists, sets, or sequences.

- **Iterable**: Refers to an object that can be traversed sequentially. In other words, an iterable is a data structure that allows its elements to be accessed one by one in a certain order.

- **Iterable vs Enumerable**: An iterable is simply something that can be iterated, while an enumerable is something more specific that can not only be iterated, but can also generate a sequence of elements in an ordered manner

- **Generator**: Allows you to generate a sequence of values ​​lazily, that is, one at a time, instead of generating and storing all the values ​​in the sequence at once. This means that a generator does not calculate all the values ​​in the sequence beforehand, which saves memory and is useful when working with large data sets. Generators are created using the yield keyword instead of return within a function. When a generator is called, it returns an iterator object that can be used to retrieve the values ​​generated by the function.

- **Guard Clauses or Early Returns**: They are control structures used in programming to improve the readability and maintainability of the code. It consists of using early return statements to handle special cases or exceptional conditions at the beginning of a function or method. The main purpose of guard clauses is to reduce code complexity by avoiding excessive nesting of conditionals (if-else) and by handling special cases explicitly at the beginning of the function. This makes the program flow clearer and easier to understand.

- **Record**: Refers to an immutable data structure, which means that once it is created, it cannot be changed. However, this may vary depending on the programming language you are using. It is used to store a fixed set of data that represents a specific entity. They can be created using immutable classes or using special data types. They are commonly used to model immutable entities, that is, to represent data that should not change once it is created.

- **Partial**: It is a keyword used to divide the definition of a class, structure, interface or method between two or more files. This means that you can have multiple files that contain parts of the code from a single entity and that all of those parts are automatically combined into a single entity when the program is compiled.

- **Final**: It is a keyword used to declare constants, make objects immutable, or to indicate that a variable, method, or class cannot be overridden. If applied to a method, it means that method cannot be overridden by subclasses. And if applied to a class, it indicates that the class cannot have subclasses.

- **Pointers**: These are variables that store memory addresses instead of direct values. In other words, a pointer "points" to the location in memory where some data is stored. They allow you to directly manipulate the system memory. This can be useful for working with complex data structures, accessing specific memory locations, and for optimizing the performance of certain operations.

- **References**: They are aliases or nicknames of an object in memory. It is used to access an object without making a copy of that object. Instead of holding the value of the object directly, a reference simply "points" to the original object in memory.

- **Narrowing**: It is a term used in the context of data type conversion. It refers to the conversion from a larger data type to a smaller one, which may result in loss of information or precision. In many programming languages, when we convert a larger data type (such as a long integer) to a smaller one (such as a short integer), there is a possibility that some of the information will be "narrowed" during the conversion, which can result in a loss of precision.

- **Type Guard**: is a feature in programming languages ​​that allows you to refine the type of a variable within a block of code if certain conditions are met. This is useful when you are working with union types (type unions) or generic types. You can use a type guard to check if a variable is of a certain type and then make use of that type information safely.


---
## 3- Object Oriented Programming
- **Generics**: Allow you to write code (classes, functions, interfaces) that can work with any type of data. Instead of specifying a specific data type, you can use a generic type that will be replaced by an actual type when the code is used. This makes the code more flexible and reusable. Ex: getitem and setitem in python allow the same behavior although generics do not exist as such.

- **Overloading**: Refers to the ability to have multiple methods or functions with the same name in the same class, but with different parameters. This means that you can have the same function with different behaviors depending on the parameters it receives.

- **Overriding**: Refers to the ability of a subclass (a class that inherits from another) to provide a specific implementation for a method that already exists in the base class. This means that the subclass can "replace" or "augment" or "override" the implementation of the method in the base class with its own implementation.

- **Abstraction**: It consists of identifying the main characteristics and behaviors of a real-world object and representing them in the code through a class.

- **Encapsulation**: It consists of hiding the internal details of an object and exposing only the operations or methods that can be used by other objects. This is accomplished by using access modifiers, such as public, protected, and private, which control the visibility of an object's attributes and methods.

- **Inheritance**: Allowing one class (called a child class or subclass) to inherit characteristics (attributes) and behaviors (methods) from another class (called a parent class or superclass).

- **Polymorphism**: It means that an object can take many forms. Allows an object to be treated as if it were a different type. It allows different objects to respond uniquely to the same messages.

- **Overloading polymorphism**: Refers to the ability of different classes to have methods with the same name but different implementations. When you call a method with a particular name, the compiler determines which method to execute based on the number and type of the arguments provided. In python it does not exist.

- **Inclusion polymorphism**: Refers to the ability of a base class to be used as if it were an instance of its derived classes. This means that an object of a base class can be treated as an object of any of its derived classes.

- **Abstract classes**: These are classes that cannot be instantiated directly, that is, objects cannot be created from them. Instead, they are used as templates for other classes that inherit from them. Abstract classes can contain normal methods (with implementation) and abstract methods (without implementation). Abstract methods must be implemented by subclasses that inherit from the abstract class.

- **Interfaces**: Defines a set of methods that a class must implement. Basically, an interface establishes a contract that classes must fulfill if they want to be considered the type of that interface.

- **Interaces vs Abstract Classes**: The main difference between an abstract class and an interface is that an abstract class can contain implementations of methods, while an interface cannot contain implementations and defines a set of methods that a concrete class must implement.

- **Protocols**: They are a set of rules that define an interface, but do not provide an implementation. Instead, protocols serve as a contract that classes must adhere to.

- **Static methods**: Also known as class methods, these are functions that belong to the class itself rather than to individual instances of the class. This means that you can call a static method without creating an instance of the class.

- **Descriptors**: Used in various programming languages ​​to control or intercept access to an object's attributes, allowing custom logic to be implemented when accessing, setting, or clearing an attribute. The basic idea of ​​a descriptor is that an object (the descriptor) can be associated with an attribute in a class, and this object defines how the get, assign, and delete operations of the attribute are handled. Descriptors are primarily used to implement calculated properties, data validation, attribute management, and other custom data access behaviors. In Python where the concept of descriptors is more prominent they are implemented through the special methods __get__, __set__ and __delete__, which allow the descriptor to control access to attributes.

- **Virtual methods**: Also known as polymorphic methods, they are functions that can be overridden in derived classes (subclasses). In other terms, virtual methods allow a base class to provide an interface for derived classes to implement their own version of the method.

- **Non-virtual methods**: These are functions that cannot be replaced or overwritten in child classes or subclasses.

- **Mutator methods**: This type of method is used to change the internal state of an object, which means that it modifies the values ​​of the attributes of that object. In other words, a mutator method is responsible for changing the state of an object in some specific way based on logic defined within that method.

- **Class attribute**: It is a variable that belongs to the class itself, rather than belonging to a specific instance of the class. This means that the class variable is shared by all instances of the class.

- **Class method**: It is a function that is associated with a class. These methods are invoked on the class itself, rather than on a particular instance of the class.

- **Composition**: Refers to the technique in which objects are combined to form a more complex object. Instead of inheriting properties and behaviors from a parent class, an object can contain other objects as part of its internal structure. It is the creation of complex classes by combining simpler objects.

- **Enumerator**: It is a data type in some programming languages ​​that allows defining a set of constants with descriptive names. These constants are associated with integer values ​​that increase automatically, starting from 0 or any other specified initial value.

- **Iterator**: It is an object that allows you to traverse a collection of elements, such as a list or a set, and access each of them sequentially. Basically, it provides a mechanism to loop through the elements of a data structure one by one, usually using a while or for loop.


---
## 4- Functional programming
- **Pure functions**: They are functions that have two important properties: ***"Determinism"***: given the same set of inputs, a pure function will always return the same result, no matter how many times it is called and ***"Absence of side effects"***: a pure function does not produce side effects outside of its scope, meaning that It does not modify any variable outside the function, nor does it perform actions that affect the state of the program.

- **Impure functions**: These are those that, in addition to depending solely on their arguments, also make modifications to the external state.

- **Lambda expressions**: These are anonymous functions that can be created on the fly. In essence, they are unnamed functions that can be defined and used wherever they are needed.

- **First class functions**: These are those that can be treated like any other variable in a programming language. This means that first-class functions can be assigned to variables, passed as arguments to other functions, returned as values ​​from other functions, and stored in data structures.

- **Higher order functions**: These are those that meet at least one of the following criteria: 1- They accept one or more functions as arguments. 2- They return a function as a result. (map, reduce, filter)

- **Closures**: They refer to functions that capture variables from their surrounding environment, that is, variables defined outside the function in which they are located. These captured variables can be used within the function, even after the function has left the scope in which they were defined, causing the closure to "enclose" or "capture" the state of the variables.

- **Recursion**: Refers to the ability of a function to call itself directly or indirectly. In other words, a recursive function is one that, when executed, can invoke itself to perform a specific task. It is used to solve complex problems by dividing them into simpler subproblems. However, it is important to note that recursion must have a base case (or base cases) defined to prevent the function from being called indefinitely, which would cause a stack overflow.

- **Function composition**: It consists of combining two or more functions to create a new function, where the result of one function becomes the input of another.

- **Monoid**: It is an algebraic structure consisting of a set and a binary operation, which satisfies two key properties: lockability and the existence of a neutral element.
    - **Lock**: For any pair of elements in the set, the binary operation produces another element of the same set. In other words, the combined operation of two elements within the set always produces a valid element within the same set.

    - **Neutral element**: There is a special element in the set, called neutral element, which when combined with any other element using binary operation, produces the same other element.

- **Functor**: It is a structure that allows applying a function to the values ​​encapsulated within that structure, maintaining the original structure. It is an abstraction that allows us to perform operations in a specific context.

- **Endofunctor**: It is a type class that maps objects into the same category. In simpler terms, an endofunctor is a structure that acts on objects within the same category, transforming them in some way and returning objects of the same type.

- **Controlled side effects**: These refer to the controlled or limited management of changes in the state of the system outside of the pure function. The management of controlled side effects is achieved using techniques such as data immutability, the use of pure functions and the isolation of side effects in certain parts of the code, such as so-called side effects. This allows you to write more predictable code that is easier to reason with and test.

- **Monads**: These are monoids in the domain of endofunctors. These are used to manage stones with side effects in a safe and controlled manner. It is a generic type that represents a value along with some type of associated context or effect, such as exception handling, asynchronous computations, or state handling. They provide a way to chain operations with side effects transparently and manage complexity in a controlled way. Additionally, they allow side-effect handling to be separated from the main flow of programming logic, which improves the readability and maintainability of the code.

- **Maybe Monad**: Used to chain operations on values ​​that may be null, so that if a null value is encountered at any point, subsequent operations are skipped and the final result is also null.

- **Referential transparency**: It means that a function can be replaced by its value without changing the result of the program. In other words, if a function always returns the same result for the same arguments, then we can replace the call to that function with its value without affecting the behavior of the program.

- **Lazy evaluation**: It means delaying the evaluation of an expression until its value is actually needed, expressions are not evaluated immediately. When the value of a lazy expression is needed, it is evaluated at that time and its result is stored for future use. If the value is never needed, the expression is never evaluated, which can result in a performance optimization. It allows you to work with potentially infinite data structures, since only the elements that are really needed are calculated. This can be useful in situations where you do not need to process all the information at once, which can save time and computational resources.


---
## 5- Asynchronous and concurrent programming
- **Concurrency**: Refers to the ability of a program to perform multiple tasks seemingly simultaneously. In a concurrent environment, tasks can progress in an overlapping manner, giving the impression that they are running at the same time. This is useful for improving the efficiency and responsiveness of a program.

- **Parallelism**: Involves the actual simultaneous execution of multiple tasks, either on systems with multiple processor cores or on multiple networked systems. Parallelism is especially useful for speeding up the processing of intensive tasks, as it allows the workload to be distributed among multiple resources effectively.

- **Concurrency vs parallelism**: Concurrency refers to the coordination of multiple tasks for better overall performance, while parallelism involves the actual simultaneous execution of such tasks.

- **Async/Await**: Allows you to write asynchronous code in a clearer and more readable way, making it appear synchronous. The async keyword is used before a function to indicate that that function returns a promise. The await keyword is used within an async function to wait for a promise to resolve before continuing to execute the code.

- **Asynchronous functions**: These are functions that can be executed asynchronously, meaning that they can perform operations that could take time without blocking the main execution flow of the program.

- **Callbacks**: These are functions that are passed as arguments to other functions. These functions are then invoked or "called back" by the receiving function at some point during their execution.

- **Promises or Futures**: It is an object that represents the eventual result of an asynchronous operation. It is in one of three states: pending, fulfilled, or rejected. Once a promise has been fulfilled or rejected, it locks its state and its resulting value will not change.

- **Chained Promises**: They are a way to handle multiple asynchronous operations sequentially. Instead of nesting multiple asynchronous function calls, chained promises allow you to chain multiple asynchronous operations so that each one executes after the previous one has completed its work.

- **Event loop**: It is a mechanism that allows a program to perform multiple tasks concurrently, without having to wait for one task to complete before starting the next. When an asynchronous task starts, the event loop adds that task to an event queue. The event loop then continually checks for pending events in the queue and manages the execution of each of them. This allows the program to continue running efficiently, handling multiple asynchronous operations without blocking the main flow of the program.

- **Timeouts**: These refer to the maximum duration allowed for an asynchronous operation to complete. If the operation is not completed within this time limit, a timeout occurs, and the operation is considered failed. These are important to prevent indefinite blocking or excessive delays in asynchronous applications. By using them appropriately, you can control the behavior of the application in situations where the asynchronous operation does not respond within a reasonable time. It is common to handle timeouts by setting timers and catching exceptions or events that indicate that the timeout has expired. This allows the application to continue execution in a controlled manner, rather than being stuck waiting indefinitely.

- **Streams**: These are sequences of continuous data that can be processed individually or in batches as they arrive, rather than having to wait for all the data to be available before starting to process it. They provide a convenient way to handle inputs and outputs in real time. They are especially useful when working with large amounts of data or real-time data sources.

- **Coroutines**: They are a special type of routine that can be suspended and resumed at specific points. This allows for cooperative execution, where one coroutine can relinquish control to another and then resume execution at a given point.

- **Threading**: Refers to the creation of threads within a single process. These threads share the same memory and can access the same data directly. It is the process of running multiple threads within a program to perform tasks concurrently. Threads are independent sequences of execution that can run simultaneously, allowing a program to perform multiple tasks at the same time. Threads are used to perform background operations, execute tasks that may block the main program, or to improve performance by performing intensive calculations in parallel.

- **Multiprocessing**: Involves the creation of multiple independent processes. Each process has its own memory space and does not share memory directly with other processes.

- **Threading vs Multiprocessing**: Multiprocessing uses processes instead of threads like threading. Unlike threading, where multiple threads share the same memory space, multiprocessing creates separate processes that execute independently.


---
## 6- Design Principles
### SOLID
**S - Single Responsibility Principle**: This principle states that a class must have a single reason to change. In other words, each class should have only one responsibility in the system.

**O - Open/Closed Principle**: This principle postulates that software entities, such as classes, modules and functions, should be open for extension but closed for modification. This means that new functionality must be able to be added without changing existing code.

**L - Liskov Substitution Principle**: This principle states that the objects of a program must be replaceable by instances of their subtypes without altering the correctness of the program. In short, a base class should be able to be overridden by any of its derived classes without affecting the expected behavior.

**I - Interface Segregation Principle**: This principle suggests that clients should not be forced to depend on interfaces that they do not use. Instead of having large, general interfaces, it is better to have smaller, specific interfaces.

**D - Dependency Inversion Principle**: This principle indicates that high-level modules should not depend on low-level modules, both should depend on abstractions. Furthermore, abstractions should not depend on details, but the other way around.

### KISS (Keep It Simple, Stupid) 
- Avoid including unnecessary features in the software.
- Preferring clarity and simplicity of code over unnecessary complexity.
- Focusing on solving the problem directly and without adding elements that could unnecessarily complicate the system.

### GRASP (General Responsibility Assignment Software Patterns)
These are a set of design patterns that help assign responsibilities to classes and objects in a software system. These principles are useful for designing software systems with a focus on clear and consistent assignment of responsibilities.

- Information Expert Pattern: This pattern suggests assigning a responsibility to the class that has the information necessary to carry out that responsibility.

- Controller Pattern: It proposes assigning the responsibility of receiving and handling system requests and events to a controller class.

- Creator Pattern: It focuses on assigning the responsibility of creating class instances to a specific class or a set of classes.

- Low Coupling Pattern: It suggests reducing dependencies between different classes, thus promoting a more flexible design and less subject to change.

- High Cohesion Pattern: This pattern indicates that responsibilities within a class must be closely related and unified around a specific function or task.

- Polymorphism Pattern: It proposes using polymorphism to assign behaviors to classes without needing to know in advance which subclass it is.

- Protected Variations Pattern: It suggests encapsulating the variabilities of the system to protect other parts of the system from possible changes.

- Pure Fabrication: This pattern indicates that in some cases it may be useful to introduce a purely fabricated class that does not represent a domain entity, but that fulfills a specific function.

### DRY (Don't Repeat Yourself)
It is a principle that emphasizes the importance of writing and maintaining code so that it is not repeated. This means that instead of duplicating logic or functionality in multiple places, the code should be modular and reusable.

### YAGNI (You Ain't Gonna Need It)
This principle is part of the agile software development methodology and is intended to guide developers in making decisions about what functionality to implement in a system. It focuses on the idea of ​​not adding unnecessary functionality or complexity to a system, especially when those functionalities are not currently needed. Instead of anticipating and developing features that "might" be useful in the future, developers follow this principle to focus on implementing only what is needed at the present moment.