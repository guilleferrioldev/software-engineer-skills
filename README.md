# Software Engineer Skills

### Algorithms, Data Structures and Design Patterns implemented in Python. Programming concepts.

---
#### 1- Programming languages:
#####  Basic concepts
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

##### Typing
- **Typing**: Refers to the concept of assigning data types to variables, function parameters, expressions, among other elements in a programming language.

- **Static typing**: Refers to the declaration and verification of data types at compile time. This means that in a statically typed programming language, data types must be specified before using a variable or function, and the compiler will check whether they are being used according to their declared types. If there are any type errors, the compiler will detect them before the program is executed.

- **Dynamic typing**: Refers to the ability of a language to automatically determine the data type of a variable at run time. In a dynamically typed language, it is not necessary to explicitly declare the type of a variable before using it, since the type is automatically inferred based on the value assigned to it.

- **Strong typing**: Refers to restricting operations between different types of data in a programming language. In a strongly typed language, conversions between data types are not done implicitly, which means that operations between incompatible types generate errors. This helps prevent errors and ensures that operations are performed only between compatible data types.

- **Weak typing**: Refers to the flexibility to perform operations between different types of data in a programming language. In a weakly typed language, implicit data type conversions can be performed, which means that operations between incompatible types can be performed without errors, as the language will attempt to automatically convert data types as necessary, resulting in which can lead to unexpected results if you are not careful.

- **Type inference**: It is a process in which a programming language automatically deduces the type of an expression rather than requiring the programmer to specify it explicitly.

- **Duck typing**: "If it walks like a duck and quacks like a duck, then it must be a duck" sums up the concept well. In programming terms, this means that if an object has specific methods or behaviors, it can be treated as if it belongs to a certain interface or type, even if it does not explicitly inherit from that type. The idea is that if an object behaves in a certain way, then it can be treated as if it were of a particular type, regardless of its actual type.

##### Compilation
- **Compiler**: A compiler is a tool that translates the source code of a programming language into object code in the target language. The compiler performs lexical analysis, syntactic analysis, semantic analysis, code optimization, and code generation as part of this process. During lexical analysis, the compiler breaks the code into tokens such as identifiers, keywords, operators, etc. Grammatical analysis checks whether the program structure follows the syntactic rules of the language. Semantic analysis verifies that the language rules are followed and makes certain optimizations to improve the performance of the code. Finally, the compiler generates machine code based on the result of all these analyzes

- **Compiled language**: It is a type of programming language whose source code is directly translated into executable code before execution.

- **Interpreter**: It is a computer program that reads and executes instructions written in a high-level programming language. It works by reading the source code line by line and translating it into a low-level executable format. Unlike a compiler, which translates the entire program at once, an interpreter performs the translation and execution of instructions in real time. The interpreter usually includes a runtime environment that facilitates interaction with the source code, error handling, and system resource management.

- **Interpreted language**: is a type of programming language whose source code is not compiled directly into executable code, but is instead interpreted and executed line by line by an interpreter. In other words, instead of compiling the code into an executable file, the interpreter reads the source code and executes it directly.

- **Linker**: It is a compilation process tool in programming that is used to combine multiple object files generated during compilation into a single executable program. This involves resolving references to functions, variables, and other symbols defined in separate modules and binding them to specific memory addresses in the final program. It is responsible for taking all the previously compiled code fragments and assembling them into a single executable that can be loaded and executed by the operating system.

- **Compilation errors**: These are problems found during the process of translating source code into machine code. These errors occur when the compiler encounters instructions that violate the syntax of the programming language or when there are mistakes in the semantics of the code. This means that the compiler cannot convert the source code into an executable program due to errors in the code.

- **Just-In-Time(JIT) compilation**: It is an approach in which the source code is compiled at runtime, that is, just before it is executed. Instead of compiling all of a program's code before running it (as in the case of static compilation), JIT compiles parts of the code as they are needed during program execution. This can lead to more efficient program execution as the compiled code adapts to the conditions of the execution environment in real time.

- **Compile time** refers to the process in which source code written by the programmer is converted into code executable by the computer. During compilation, the compiler checks the syntax and structure of the code for errors before producing the executable program. In short, it is the process of translating source code into a format that the machine can understand and execute.

- **Runtime** refers to the period in which the compiled program is running and performing its functions on the computer. During this time, the program interacts with the operating system, hardware, and other programs in real time. This is where the actual behavior of the program is observed and logical or other errors may arise.

- **Cross-compilation**: It is the process of compiling a program so that it runs on a different platform than the one on which the compilation is being performed. This means that the code is compiled on a different architecture or operating system than the one that will be used to run the resulting program.

- **Dependencies and Libraries**: Dependencies are the set of external components necessary for a project to work, while libraries are sets of code that provide specific functionality and that can be used by a project to simplify development and programming.

- **Makefiles**: These are configuration files used in build systems to automate the software compilation process. A Makefile contains rules that specify how to combine source files to produce executable programs or other files.

- **Construction systems**: These are tools that facilitate the automation of the software construction process. These systems manage dependencies between different software components, such as source files and libraries, and ensure that files are compiled in the correct order.

---
#### 2- General concepts:
- **Scope**: Refers to the scope or visibility that a variable has within a program. Defines where in the code a variable can be used and accessed. The scope of a variable can be global, meaning that it can be accessed from anywhere in the program, or local, meaning that it can only be accessed within a specific portion of the code, such as a function or a block of code. 

- **Mutability**: Refers to the ability of an object to change or modify its state after its creation.

- **Parameter by reference**: It is a type of parameter in programming that allows a function to directly access and modify the value of a variable in memory, instead of operating on a copy of the value. This means that any modification made to the parameter by reference inside the function will directly affect the original value of the variable outside the function.

- **Parameter by value** : When a parameter by value is passed to a function, a copy of the actual value is passed to the function parameter. This means that any modifications made to the parameter inside the function will not affect the original value outside the function.

- **Serialization**: Refers to the process of converting an object or data structure into a format that can be stored or transmitted, and then reconstructed. It allows you to convert complex data into a form that can be saved or sent efficiently, and then restore it to its original form when necessary.

- **Enumerable**: Refers to a collection of elements that can be enumerated or counted. In many programming languages, enumerables are used to represent collections of elements such as lists, sets, or sequences.

- **Iterable**: Refers to an object that can be traversed sequentially. In other words, an iterable is a data structure that allows its elements to be accessed one by one in a certain order.

- **Iterable vs Enumerable**: An iterable is simply something that can be iterated, while an enumerable is something more specific that can not only be iterated, but can also generate a sequence of elements in an ordered manner

- **Generator**: It is a special function that can pause its execution and then resume it from the same point where it stopped. This allows the generation of a sequence of values ​​efficiently, as the values ​​are calculated on demand rather than being generated all at once. Generators are created using the yield keyword instead of return within a function. When a generator is called, it returns an iterator object that can be used to retrieve the values ​​generated by the function.

---
#### 3- OOP:
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
#### 4- Functional programming: 

---
#### 5- DevOps:
- **CI/CD** is an approach that seeks to automate the process of building, testing, and deploying software, leading to faster, more frequent, and more reliable releases of applications.

- **Continuous Integration (CI)** is a software development practice in which developers combine their work frequently, usually several times a day. Each integration is automatically verified with tests to detect errors as early as possible. This enables early problem detection and rapid remediation, which in turn helps reduce integration conflicts.

- **Continuous Delivery (CD)** refers to the practice of automatically and reliably delivering software releases across various test and production environments. The goal is to ensure that the software is always in a deployable state, reducing the time between writing the code and deploying it to production.