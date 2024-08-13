# Software Architecture

## General concepts
- **Modularity**: Refers to the practice of breaking a system into smaller, self-contained components, allowing the system to be easier to understand, maintain, and scale.

- **Cohesion**: Refers to the extent to which the elements of a software module or component are interrelated and work together to achieve a common goal. A high degree of cohesion means that the components of a module are strongly related to each other in terms of functionality and purpose. In contrast, low cohesion refers to a poor bond between the parts of a module, which may indicate that it might be advantageous to divide the module into more cohesive components.

- **Coupling**: Refers to the degree of interdependence between the various modules, classes or components of a system. Low coupling indicates that the different parts of the system are less interconnected, making it easier to modify, extend, and reuse the code. On the other hand, high coupling can make the system more difficult to maintain and update, since changes in one part of the system can have unexpected effects on other parts.
    - **Afferent coupling (AC)**: Refers to the degree to which a component depends on other components. (Inside)
    - **Efferent coupling (EC)**: Refers to the degree to which other components depend on this component. (Outside)

- **Abstraction**: Refers to the ability to focus on the level of detail appropriate for a given problem, ignoring unnecessary details. Abstraction allows the complexity of the system to be simplified, making it easier to understand and maintain.

- **Instability**: Refers to the ease with which a component or module can change over time, either due to changes in its own characteristics or changes in other components with which it interacts. A high level of instability can lead to greater complexity and difficulty in maintaining and evolving the software system.

- **Mainstream distance**: This concept refers to the extent to which a component or module is directly or indirectly connected to the core logic of the application.

- **Connascence**: It is a software quality metric to allow reasoning about the complexity caused by dependency relationships in object-oriented design much like coupling did for structured design. In software engineering, two components are connascent if a change in one would require the other to be modified in order to maintain the overall correctness of the system.Connascence: It is a software quality metric to allow reasoning about the complexity caused by dependency relationships in object-oriented design much like coupling did for structured design. In software engineering, two components are connascent if a change in one would require the other to be modified in order to maintain the overall correctness of the system.
    - **Static Connascence**: It is a type of coupling or dependency between two modules or components of a system. It refers to the relationship between two elements in a program that is determined at compile time.
    - **Dynamic Connascence**: Refers to the situation where two or more pieces of code must change simultaneously due to a change in a shared dependency.


## Software Quality Attributes
1. **Utility**: Refers to the ability of the software to meet the needs of users and meet specified requirements.

2. **Reliability**: Relates to the ability of the software to maintain correct operation under normal conditions and in unexpected situations.

3. **Efficiency**: Refers to the efficient use of system resources, such as memory usage, processing capacity, and response time.

4. **Maintainability**: Refers to the ease with which the software can be modified, corrected, improved or adapted to new situations.

5. **Portability**: Refers to the ease with which the software can be transferred from one environment to another, maintaining its operation and performance.

6. **Usability**: Refers to the ease of use of the software, including aspects such as user interface, accessibility and user experience.

7. **Security**: Has to do with the software's ability to protect data and operations, as well as prevent unauthorized access.

8. **Scalability**: Refers to the software's ability to adapt and handle growth in the volume of data, users or transactions without compromising its performance.

9. **Interoperability**: Refers to the ability of software to interact with other systems efficiently and effectively, including data exchange and communication between different platforms.

10. **Adaptability**: Indicates the ability of the software to adapt to different environments and situations, including changes in user requirements and the technological environment.

11. **Fault tolerance**: Relates to the software's ability to maintain its performance even in the presence of errors or failures, avoiding catastrophic failures.

12. **Testability**: Refers to the ease with which the software can be tested to ensure its correct operation, identify possible failures and verify its compliance with requirements.

13. **Reusability**: Refers to the ability to reuse software components in different contexts, which can improve productivity and reduce development costs.

14. **Documentation**: Refers to the existence of clear and complete documentation that describes the operation, design and use of the software, which facilitates its understanding, maintenance and support.

15. **Modularity**: Refers to the ability of software to be composed of independent modules, making it easier to understand, maintain, and reuse components.

16. **Extensibility**: Indicates the ease with which the software can be extended to include new functionalities or features, without affecting existing operation.

17. **Adaptability to change**: This attribute refers to the ability of the software to adapt effectively to changes in requirements, operating environment and business conditions, maintaining its functionality and performance over time.

18. **Conformity**: Refers to the ability of the software to comply with specific standards, regulations and guidelines that are applicable to its application domain. This may include safety regulations, accessibility standards, industry standards, among others.


## Cross-cutting Concerns
They refer to aspects of a program that affect multiple parts of the application. These aspects often cut across different modules and components of the system.

1. **Security**: The implementation of security measures, such as authentication, authorization, data encryption, session management, prevention of security attacks, etc.

2. **Logging and monitoring**: The recording of events, the generation of logs, error management, monitoring of system performance and health, among other aspects related to traceability and management of information on the operation of the software.

3. **Transactionality**: The handling of transactions, consistency and integrity of data in operations that involve multiple resources or entities.

4. **Configuration management**: The management of configurations in the software, such as parameterization, environment management (development, staging, production), management of environment variables, among others.

5. **Cache and storage**: Cache management, efficient data access, persistence management and performance optimization in data manipulation and access.

6. **Error Management**: Properly handle and manage exceptions and errors in the application to ensure a smooth user experience and avoid unexpected interruptions.


## Architectural Patterns
Architectural patterns are proven and recurring solutions to common problems in the design and implementation of software systems. These patterns provide a structured approach to organizing and building systems, allowing developers to leverage best practices and previous experiences.


