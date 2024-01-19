## 1- Lenguajes de programación:
# Básico
• Sintaxis: La sintaxis se refiere a las reglas y estructuras gramaticales del lenguaje que definen cómo se deben escribir las 
            instrucciones en el código.

• Semántica: La semántica se refiere al significado de las instrucciones escritas en el código. 

• Tipos de datos: Los lenguajes de programación tienen diferentes tipos de datos, como enteros, flotantes, cadenas, booleanos, etc.

• Estructuras de control: Las estructuras de control, como bucles y condicionales, permiten controlar el flujo de ejecución del programa.

• Funciones: Las funciones permiten encapsular un conjunto de instrucciones para que puedan ser reutilizadas en diferentes partes
             del programa.

• Estructuras de datos: Los lenguajes de programación ofrecen diversas estructuras de datos, como arrays, listas, diccionarios, conjuntos, 
                        entre otros, que permiten organizar y manipular datos de forma eficiente.

• Variables y asignación: Las variables permiten almacenar y manipular datos en el código. La asignación se refiere a la acción de 
                          asignar un valor a una variable.

• Operadores: Los operadores son símbolos especiales que realizan operaciones sobre los datos. Estos incluyen operadores aritméticos
              (suma, resta, multiplicación, división), operadores de comparación (igualdad, mayor que, menor que), operadores lógicos
              (AND, OR, NOT), entre otros

• Manejo de errores: Los lenguajes de programación permiten controlar y manejar errores mediante el uso de mecanismos como excepciones,
                     try-catch, o manejo de errores de forma más controlada.

• Entrada / Salida: Cómo el lenguaje maneja la entrada de datos desde el usuario o desde un archivo, y la salida de datos hacia la 
                    pantalla o un archivo.

• Conteo de referencias: Se refiere al número de veces que una determinada entidad (como un objeto, una variable o una pieza de 
                        información) es referenciada en un determinado contexto. En el contexto de la programación, el conteo de 
                        referencias puede aplicarse a variables, objetos u otros elementos dentro del código.


# Tipado
• Tipado: Se refiere al concepto de asignar tipos de datos a variables, parámetros de funciones, expresiones, entre otros elementos 
          en un lenguaje de programación.

• Tipado estático: Se refiere a la declaración y verificación de tipos de datos en tiempo de compilación. Esto significa que, en un
                    lenguaje de programación con tipado estático, se deben especificar los tipos de datos antes de utilizar una 
                    variable o una función, y el compilador verificará si se están utilizando de acuerdo con sus tipos declarados.
                    Si hay algún error de tipo, el compilador lo detectará antes de la ejecución del programa.
                    
• Tipado dinámico: Se refiere a la capacidad de un lenguaje para determinar automáticamente el tipo de datos de una variable en 
                  tiempo de ejecución. En un lenguaje con tipado dinámico, no es necesario declarar explícitamente el tipo de una
                  variable antes de usarla, ya que el tipo se infiere automáticamente según el valor que se le asigna.

• Tipado fuerte: Se refiere a la restricción de operaciones entre diferentes tipos de datos en un lenguaje de programación. 
                 En un lenguaje con tipado fuerte, las conversiones entre tipos de datos no se realizan implícitamente, lo
                 que significa que las operaciones entre tipos incompatibles generan errores. Esto ayuda a prevenir errores 
                 y asegura que las operaciones se realicen solo entre tipos de datos compatibles.

• Tipado débil: Se refiere a la flexibilidad para realizar operaciones entre diferentes tipos de datos en un lenguaje de
                programación. En un lenguaje con tipado débil, se pueden realizar conversiones implícitas de tipos de datos, 
                lo que significa que las operaciones entre tipos incompatibles pueden llevarse a cabo sin generar errores,
                ya que el lenguaje intentará convertir automáticamente los tipos de datos según sea necesario,  lo que puede 
                conducir a resultados inesperados si no se tiene cuidado.

• Inferencia de tipos: Es un proceso en el que un lenguaje de programación deduce automáticamente el tipo de una expresión en
                     lugar de exigir al programador que lo especifique explícitamente. 

• Duck Typing: "Si camina como un pato y grazna como un pato, entonces debe ser un pato" resume bien el concepto. En términos de
                programación, esto significa que si un objeto tiene métodos o comportamientos específicos, puede ser tratado como 
                si perteneciera a una determinada interfaz o tipo, incluso si no hereda explícitamente de ese tipo. La idea es que
                si un objeto se comporta de  cierta manera, entonces puede ser tratado como si fuera de un tipo particular, 
                independientemente de su tipo real.




# Compilación                     
• Compilador: Un compilador es una herramienta que traduce el código fuente de un lenguaje de programación a código objeto
              en el lenguaje objetivo. El compilador realiza análisis léxico, análisis sintáctico, análisis semántico, 
              optimización de código y generación de código como parte de este proceso. Durante el análisis léxico, el compilador
              divide el código en tokens como identificadores, palabras clave, operadores, etc. El análisis gramatical verifica si 
              la estructura del programa sigue las reglas sintácticas del lenguaje. El análisis semántico verifica que las reglas
              del lenguaje se cumplan y hace ciertas optimizaciones para mejorar el rendimiento del código. Finalmente, el 
              compilador genera código de máquina en función del resultado de todos estos análisis

• Lenguaje compilado: Es un tipo de lenguaje de programación cuyo código fuente es traducido directamente a un código ejecutable 
                      antes de su ejecución. 

• Intérprete: Es un programa informático que lee y ejecuta instrucciones escritas en un lenguaje de programación de alto nivel.
              Funciona leyendo el código fuente línea por línea y traduciéndolo a un formato ejecutable de bajo nivel. A diferencia 
              de un compilador, que traduce todo el programa de una vez, un intérprete realiza la traducción y ejecución de las 
              instrucciones en tiempo real. El intérprete generalmente incluye un entorno de ejecución que facilita la interacción
              con el código fuente, el manejo de errores y la gestión de recursos del sistema.

• Lenguaje interpretado: Es un tipo de lenguaje de programación cuyo código fuente no se compila directamente a un código ejecutable,
                         sino que se interpreta y ejecuta línea por línea por un intérprete. En otras palabras, en lugar de compilar 
                         el código en un archivo ejecutable, el intérprete lee el código fuente y lo ejecuta directamente.

• El enlazador: Es una herramienta del proceso de compilación en programación que se utiliza para combinar múltiples archivos de 
                objeto generados durante la compilación en un solo programa ejecutable. Esto implica resolver referencias a funciones,
                variables y otros símbolos definidos en módulos separados y vincularlos a direcciones de memoria específicas en el
                programa final. Es responsable de tomar todos los fragmentos de código compilados previamente y ensamblarlos en
                un solo ejecutable que puede ser cargado y ejecutado por el sistema operativo.

• Errores de compilación: Son problemas que se encuentran durante el proceso de traducción de código fuente a código máquina.
                          Estos errores ocurren cuando el compilador encuentra instrucciones que violan la sintaxis del lenguaje de
                          programación o cuando hay faltas en la semántica del código. Esto significa que el compilador no puede 
                          convertir el código fuente en un programa ejecutable debido a errores en el código

• Recolector de basura: Es un componente de muchos lenguajes de programación que se encarga de gestionar la memoria utilizada por un 
                        programa. Su principal función es liberar la memoria que ya no está siendo utilizada por el programa, lo que
                        ayuda a prevenir fugas de memoria y hace que los programas sean más eficientes en el uso de recursos. Cuando un
                        programa crea objetos o variables en la memoria, el recolector de basura se encarga de monitorear cuáles de 
                        estos elementos ya no son accesibles desde el programa, ya sea porque están fuera de alcance o porque ya no 
                        son necesarios. Una vez que determina que ciertos elementos no son alcanzables, el recolector de basura se 
                        encarga de liberar la memoria ocupada por estos elementos, permitiendo que sea reutilizada por el programa 
                        para otros fines.

• Compilación Just-In-Time (JIT):  Es un enfoque en el que el código fuente se compila en tiempo de ejecución, es decir, justo antes 
                                  de que se ejecute. En lugar de compilar todo el código de un programa antes de ejecutarlo (como en 
                                  el caso de la compilación estática), JIT compila partes del código a medida que son necesarias durante
                                  la ejecución del programa. Esto puede conducir a una ejecución más eficiente del programa ya que el
                                  código compilado se adapta a las condiciones del entorno de ejecución en tiempo real. 

• El "tiempo de compilación" se refiere al proceso en el cual el código fuente escrito por el programador se convierte en código ejecutable 
                             por la computadora. Durante la compilación, el compilador revisa la sintaxis y la estructura del código para 
                             detectar errores antes de producir el programa ejecutable. En resumen, es el proceso de traducir el código 
                             fuente a un formato que la máquina pueda entender y ejecutar.

• El "tiempo de ejecución" se refiere al período en el que el programa compilado se está ejecutando y realizando sus funciones en la 
                            computadora. Durante este tiempo, el programa interactúa con el sistema operativo, el hardware y otros
                            programas en tiempo real. Aquí es donde se observa el comportamiento real del programa y pueden surgir 
                            errores lógicos o de otro tipo.

• Reflexión: Se refiere a la capacidad de un programa para examinar y modificar su propia estructura y comportamiento durante el tiempo de
             ejecución. Esto significa que un programa puede inspeccionar y manipular sus propias clases, métodos, atributos y demás 
             componentes en tiempo de ejecución. Esta abre la puerta a una serie de funcionalidades avanzadas, como la creación dinámica de
             instancias de clases, la invocación dinámica de métodos, la inspección de la estructura de los objetos, la manipulación de
             atributos, entre otros.

• Cross-compilación: Es el proceso de compilar un programa para que se ejecute en una plataforma diferente a aquella en la que se está 
                    realizando la compilación. Esto significa que el código se compila en una arquitectura o sistema operativo distinto 
                    al que será utilizado para ejecutar el programa resultante.

• Dependencias y Bibliotecas: Las dependencias son el conjunto de componentes externos necesarios para que un proyecto funcione, mientras
                              que las bibliotecas son conjuntos de código que proporcionan funcionalidades específicas y que pueden ser 
                              utilizadas por un proyecto para simplificar el desarrollo y la programación.

• Makefiles : Son archivos de configuración utilizados en sistemas de construcción para automatizar el proceso de compilación de software. 
             Un Makefile contiene reglas que especifican cómo combinar archivos fuente para producir programas ejecutables u otros archivos

• Los sistemas de construcción: Son herramientas que facilitan la automatización del proceso de construcción de software. Estos sistemas 
                                gestionan las dependencias entre los diferentes componentes del software, como archivos fuente y bibliotecas, 
                                y aseguran que los archivos se compilen en el orden correcto.





## 2- Conceptos generales: 
• Ámbito: Se refiere al alcance o la visibilidad que tiene una variable dentro de un programa.
          Define en qué partes del código una variable puede ser utilizada y accedida. El ámbito de una 
          variable puede ser global, lo que significa que puede ser accedida desde cualquier parte del 
          programa, o local, lo que significa que solo puede ser accedida dentro de una porción específica
          del código, como una función o un bloque de código.

• Mutabilidad: Se refiere a la capacidad de un objeto de cambiar o modificar su estado después de su creación

• Parámetro por referencia: Es un tipo de parámetro en programación que permite que una función
                            acceda y modifique directamente el valor de una variable en la memoria,
                            en lugar de operar sobre una copia del valor. Esto significa que cualquier 
                            modificación realizada en el parámetro por referencia dentro de la función
                            afectará directamente al valor original de la variable fuera de la función.

• Parámetro por valor : Cuando se pasa un parámetro por valor a una función, se pasa una copia del valor 
                        real al parámetro de la función. Esto significa que cualquier modificación hecha al
                        parámetro dentro de la función no afectará el valor original fuera de la función.

• Serialización: Se refiere al proceso de convertir un objeto o una estructura de datos en un formato que 
                pueda ser almacenado o transmitido, para luego poder ser reconstruido. Permite convertir 
                datos complejos en una forma que puede ser guardada o enviada de manera eficiente, y luego 
                restaurarla a su forma original cuando sea necesario.

• Enumerable: Se refiere a una colección de elementos que pueden ser enumerados o contados.En muchos lenguajes de programación,
              los enumerables se utilizan para representar colecciones de elementos como listas, conjuntos o secuencias.

• Iterable: Se refiere a un objeto que puede ser recorrido secuencialmente. En otras palabras, un iterable es una estructura de 
            datos que permite acceder a sus elementos uno por uno en un orden determinado.

• Iterable vs Enumerable: Un iterable es simplemente algo que puede ser iterado, mientras que un enumerable es algo más específico
                         que no solo puede ser iterado, sino que también puede generar una secuencia de elementos de manera ordenada

• Generador: Permite generar una secuencia de valores de manera perezosa, es decir, uno a la vez, en lugar de generar y almacenar todos
             los valores de la secuencia de una vez. Esto significa que un generador no calcula todos los valores de la secuencia de 
             antemano, lo que ahorra memoria y es útil cuando trabajamos con conjuntos de datos grandes. Los generadores se crean 
             utilizando la palabra clave yield en lugar de return dentro de una función. Cuando se llama a un generador, este devuelve
             un objeto iterador que puede utilizarse para recuperar los valores generados por la función.

• Guard clauses or Early Returns: Son estructuras de control utilizadas en programación para mejorar la legibilidad y mantenibilidad
                                  del código. Consista en utilizar declaraciones de retorno temprano para manejar casos especiales o 
                                  condiciones excepcionales al principio de una función o método. El propósito principal de las cláusulas
                                  de guardia es reducir la complejidad del código al evitar la anidación excesiva de condicionales
                                 (if-else) y al manejar casos especiales de manera explícita al principio de la función. Esto hace que el
                                 flujo del programa sea más claro y fácil de entender.

• Record: Se refiere a una estructura de datos inmutable, lo que significa que una vez que se crea, no se puede cambiar. Sin embargo,
          esto puede variar según el lenguaje de programación que estés utilizando. Se utiliza para almacenar un conjunto fijo de datos
          que representa una entidad específica. Se pueden crear usando clases inmutables o utilizando tipos de datos especiales. Se usan
        comúnmente para modelar entidades inmutables, es decir, para representar datos que no deben cambiar una vez que se crean.

• Partial: Es una palabra clave que se utiliza para dividir la definición de una clase, estructura, interfaz o método entre dos o más
           archivos. Esto significa que puedes tener múltiples archivos que contienen partes del código de una sola entidad y que todas 
           esas partes se combinan automáticamente en una sola entidad cuando se compila el programa.

• Final: Es una palabra clave que see usa para declarar constantes, hacer que los objetos sean inmutables o para indicar que una variable,
        método o clase no puede ser sobrescrita. Si se aplica a un método, significa que dicho método no puede ser sobreescrito por las 
        subclases. Y si se  aplica a una clase, indica que la clase no puede tener subclases.

• Punteros: Son variables que almacenan direcciones de memoria en lugar de valores directos. En otras palabras, un puntero "apunta" a la 
            ubicación en la memoria donde se almacena algún dato. Permiten manipular directamente la memoria del sistema. Esto puede ser 
            útil para trabajar con estructuras de datos complejas, acceder a ubicaciones específicas de memoria, y para optimizar el 
            rendimiento de ciertas operaciones

• Referencias: Son alias o apodos de un objeto en memoria. Se utiliza para acceder a un objeto sin realizar una copia de ese objeto. En 
              lugar de contener el valor del objeto directamente, una referencia simplemente "apunta" al objeto original en la memoria.

• Narrowing: Es un término que se utiliza en el contexto de la conversión de tipos de datos. Se refiere a la conversión de un tipo de 
             datos más grande a uno más pequeño, lo cual puede resultar en la pérdida de información o precisión. En muchos lenguajes de
             programación, cuando convertimos un tipo de datos más grande (como un número entero largo) a uno más pequeño (como un número
             entero corto), existe la posibilidad de que parte de la información se "estreche" durante la conversión, lo que puede resultar
             en una pérdida de precisión.

• Type Guard: Es una característica en lenguajes de programación que te permite refinar el tipo de una variable dentro de un bloque de 
             código si se cumplen ciertas condiciones. Esto es útil cuando estás trabajando con tipos uniones (uniones de tipos) o tipos 
             genéricos. Puedes usar un type guard para comprobar si una variable es de un cierto tipo y luego hacer uso de esa información
             de tipo de manera segura. 

## 3- Conceptos de OOP:
• Generics: Permiten escribir código (clases, funciones, interfaces) que pueden funcionar con cualquier tipo de
            datos. En lugar de especificar un tipo de dato concreto, puedes usar un tipo genérico que se 
            reemplazará por un tipo real cuando se use el código. Esto hace que el código sea más flexible y 
            reutilizable. Ej: getitem y setitem en python permiten el mismo comportamiento aunque no existen 
            como tal los generics.

• Sobrecarga: Se refiere a la capacidad de tener múltiples métodos o funciones con el mismo nombre en una misma
              clase, pero con diferentes parámetros. Esto significa que se puede tener una misma función con
              diferentes comportamientos dependiendo de los parámetros que reciba.

• Sobreescritura: Se refiere a la capacidad de una subclase (una clase que hereda de otra) de proporcionar una 
                  implementación específica para un método que ya existe en la clase base. Esto significa que 
                  la subclase puede "reemplazar" o "aumenta" o "anular" la implementación del método en la clase
                  base con su propia implementación.

• Abstracción: Consiste en identificar las principales características y comportamientos de un objeto del mundo 
               real y representarlas en el código a través de una clase.

• Encapsulamiento: Consiste en ocultar los detalles internos de un objeto y exponer solo las operaciones o métodos 
                    que pueden ser utilizados por otros objetos. Esto se logra mediante el uso de modificadores de 
                    acceso, como público, protegido y privado, que controlan la visibilidad de los atributos y 
                    métodos de un objeto.

• Herencia: Permitir que una clase (llamada clase hija o subclase) herede características (atributos) y 
            comportamientos (métodos) de otra clase (llamada clase padre o superclase).

• Polimorfismo: Hace que un objeto pueda tomar muchas formas. Permite que un objeto pueda ser tratado como si 
                fuera de un tipo diferente.  Permite que diferentes objetos respondan de manera única a los mismos mensajes.

• Polimorfismo de sobrecarga: Se refiere a la capacidad de diferentes clases de tener métodos con el mismo nombre
                             pero con diferentes implementaciones. Cuando llamas a un método con un nombre en particular, 
                             el compilador determina cuál método ejecutar en función del número y tipo de los argumentos 
                              proporcionados. En python no existe.

• Polimorfismo de inclusión: Se refiere a la capacidad de una clase base de ser utilizada como si fuera una instancia de
                             sus clases derivadas. Esto significa que un objeto de una clase base puede ser tratado como un 
                             objeto de cualquiera de sus clases derivadas.

• Clases abstractas: Son clases que no se pueden instanciar directamente, es decir, no se pueden crear objetos a partir de 
                     ellas. En su lugar, se utilizan como plantillas para otras clases que heredan de ellas. Las clases 
                     abstractas pueden contener métodos normales (con implementación) y métodos abstractos (sin implementación).
                     Los métodos abstractos deben ser implementados por las subclases que heredan de la clase abstracta.

• Interfaces: Define un conjunto de métodos que una clase debe implementar. Básicamente, una interfaz establece un contrato que
              las clases deben cumplir si quieren ser consideradas del tipo de esa interfaz.

• Interaces vs Clases abstractas: La principal diferencia entre una clase abstracta y una interfaz es que una clase abstracta 
                                 puede contener implementaciones de métodos, mientras que una interfaz no puede contener 
                                 implementaciones y define un conjunto de métodos que una clase concreta debe implementar

• Protocolos: Son un conjunto de reglas que definen una interfaz, pero no proporcionan una implementación. En lugar de ello,
              los protocolos sirven como un contrato que las clases deben cumplir.          

• Métodos estáticos: También conocidos como métodos de clase, son funciones que pertenecen a la clase en sí misma en lugar 
                     de pertenecer a las instancias individuales de la clase. Esto significa que puedes llamar a un método 
                     estático sin necesidad de crear una instancia de la clase.

• Descriptores: Se utilizan en varios lenguajes de programación para controlar o interceptar el acceso a los atributos de un 
                objeto, lo que permite implementar la lógica personalizada al acceder, establecer o borrar un atributo. La idea
                básica de un descriptor es que un objeto (el descriptor) puede ser asociado con un atributo en una clase, y este
                objeto define cómo se manejan las operaciones de obtención, asignación y eliminación del atributo. Los descriptores
                se utilizan principalmente para implementar propiedades calculadas, validación de datos, gestión de atributos y 
                otros comportamientos personalizados del acceso a los datos. En Python  donde el concepto de descriptores es más
                prominente son implementados a través de los métodos especiales __get__, __set__ y __delete__, que permiten al descriptor 

• Métodos virtuales: También conocidos como métodos polimórficos, son funciones que se pueden sobreescribir en clases derivadas 
                    (subclases). En otros términos, los métodos virtuales permiten que una clase base proporcione una interfaz 
                    para que las clases derivadas implementen su propia versión del método.

• Métodos no virtuales: Son funciones que no pueden ser reemplazadas ni sobrescritas en clases hijas o subclases.

• Métodos mutadores: Este tipo de método se utiliza para cambiar el estado interno de un objeto, lo que significa que modifica 
                    los valores de los atributos de ese objeto. En otras palabras, un método mutador es responsable de cambiar
                    el estado de un objeto de alguna manera específica según la lógica definida dentro de ese método.

• Atributo de clase: Es una variable que pertenece a la clase en sí misma, en lugar de pertenecer a una instancia específica de
                     la clase. Esto significa que la variable de clase es compartida por todas las instancias de la clase.

• Método de clase: Es una función que está asociada a una clase. Estos métodos son invocados en la clase misma, en lugar de en 
                   una instancia particular de la clase.

• Composición: Se refiere a la técnica en la que los objetos se combinan para formar un objeto más complejo. En lugar de heredar
               propiedades y comportamientos de una clase padre, un objeto puede contener otros objetos como parte de su estructura 
               interna. Es la creación de clases complejas combinando objetos más simples.

• Enumerator: Es un tipo de dato en algunos lenguajes de programación que permite definir un conjunto de constantes con nombres 
              descriptivos. Estas constantes están asociadas con valores enteros que aumentan de forma automática, comenzando desde
              0 o cualquier otro valor inicial especificado.

• Iterator: Es un objeto que permite recorrer una colección de elementos, como una lista o un conjunto, y acceder a cada uno de ellos 
            de forma secuencial. Básicamente, proporciona un mecanismo para recorrer los elementos de una estructura de datos uno por 
            uno, normalmente utilizando un bucle while o for.


## 4- Programación Funcional
• Funciones puras: Son funciones que tienen dos propiedades importantes; "determinismo": dado el mismo conjunto de entradas, una 
                  función pura siempre devolverá el mismo resultado, sin importar cuántas veces se llame y "ausencia de efectos 
                  secundarios": una función pura no produce efectos secundarios fuera de su ámbito, lo que significa que no modifica
                  ninguna variable fuera de la función, ni realiza acciones que afecten el estado del programa.

• Funciones impuras: Son aquellas que, además de depender únicamente de sus argumentos, también realizan modificaciones en el estado externo.

• Expresiones lambda: Son funciones anónimas que se pueden crear sobre la marcha. En esencia, son funciones sin nombre que pueden ser
                      definidas y utilizadas en el lugar en el que se necesiten.

• Funciones de primera clase: Son aquellas que pueden tratarse como cualquier otra variable en un lenguaje de programación. Esto
                              significa que las funciones de primera clase pueden ser asignadas a variables, pasadas como argumentos
                            a otras funciones, devueltas como valores de otras funciones y almacenadas en estructuras de datos.

• Funciones de orden superior : Son aquellas que cumplen con al menos uno de los siguientes criterios: 1- Aceptan una o más funciones
                                como argumentos. 2- Devuelven una función como resultado. (map, reduce, filter)

• Closures : Se refieren a funciones que capturan variables de su entorno circundante, es decir, variables definidas fuera de la función 
            en la que se encuentran. Estas variables capturadas pueden ser utilizadas dentro de la función, incluso después de que la 
            función haya salido del alcance en el que fueron definidas, lo que hace que el cierre "encierra" o "captura" el estado de 
            las variables.

• Recursión: Se refiere a la capacidad de una función para llamarse a sí misma directa o indirectamente. En otras palabras, una función
             recursiva es aquella que, al ejecutarse, puede invocarse a sí misma para realizar una tarea específica. Se utiliza para 
             resolver problemas complejos dividiéndolos en subproblemas más simples. Sin embargo, es importante tener en cuenta que la 
             recursión debe tener un caso base (o casos base) definido(s) para evitar que la función se llame indefinidamente, lo que
            provocaría un desbordamiento de pila (stack overflow).

• Composición de funciones: Consiste en combinar dos o más funciones para crear una nueva función, donde el resultado de una función 
                            se convierte en la entrada de otra.

• Monoid: Es una estructura algebraica que consta de un conjunto y una operación binaria, que satisface dos propiedades clave: la cerradura
         y la existencia de un elemento neutro.

        - Cerradura: Para cualquier par de elementos del conjunto, la operación binaria produce otro elemento del mismo conjunto. En otras 
                    palabras, la operación combinada de dos elementos dentro del conjunto siempre produce un elemento válido dentro del mismo
                     conjunto.
        
        - Elemento neutro: Existe un elemento especial en el conjunto, llamado elemento neutro, que cuando se combina con cualquier otro 
                          elemento utilizando la operación binaria, produce el mismo otro elemento.

• Functor: Es una estructura que permite aplicar una función a los valores encapsulados dentro de esa estructura, manteniendo la estructura
          original. Es una abstracción que nos permite realizar operaciones en un contexto específico. 

• Endofuntor: Es una clase de tipo que mapea objetos en la misma categoría. En términos más simples, un endofuntor es una estructura que
             actúa sobre objetos dentro de la misma categoría, transformándolos de alguna manera y devolviendo objetos del mismo tipo.

• Efectos secundarios controlados: Se refieren a la gestión controlada o limitada de cambios en el estado del sistema fuera de la
                                 función pura. La gestión de los efectos secundarios controlados se logra utilizando técnicas como 
                                 la inmutabilidad de datos, el uso de funciones puras y el aislamiento de efectos secundarios en 
                                 ciertas partes del código, como en los llamados efectos colaterales. Esto permite escribir código
                                 más predecible, fácil de razonar y probar

• Monads : Se utiliza para manejar cálculos con efectos secundarios de manera segura y controlada. Es un tipo genérico que representa 
          un valor junto con algún tipo de contexto o efecto asociado, como el manejo de excepciones, computaciones asincrónicas, o 
          manejo de estados. Proporcionan una forma de encadenar operaciones con efectos secundarios de manera transparente y gestionar 
          la complejidad de forma controlada. Además, permiten separar el manejo de efectos secundarios del flujo principal de la lógica
          de programación, lo que mejora la legibilidad y mantenibilidad del código.

• Maybe Monad: Se utiliza para encadenar operaciones en valores que pueden ser nulos, de manera que si en algún punto se encuentra un 
              valor nulo, las operaciones posteriores se omiten y el resultado final también es nulo.

• Transparencia referencial: Se refiere a que una función puede ser reemplazada por su valor sin cambiar el resultado del programa. 
                            En otras palabras, si una función devuelve siempre el mismo resultado para los mismos argumentos, 
                            entonces podemos reemplazar la llamada a esa función por su valor sin afectar el comportamiento del programa. 

• Evaluación perezosa: Significa retrasar la evaluación de una expresión hasta que su valor sea realmente necesario, las expresiones no 
                        se evalúan inmediatamente.Cuando se necesita el valor de una expresión perezosa, se evalúa en ese momento y su 
                        resultado se almacena para futuros usos. Si el valor nunca es necesario, la expresión nunca se evalúa, lo que 
                        puede resultar en una optimización del rendimiento. Permite trabajar con estructuras de datos potencialmente 
                        infinitas, ya que solo se calculan los elementos que realmente se necesitan. Esto puede ser útil en situaciones
                        en las que no se necesita procesar toda la información de una vez, lo que puede ahorrar tiempo y recursos
                        computacionales.





## 5- Programación asíncrona
• Concurrencia: Se refiere a la capacidad de un programa para realizar múltiples tareas de manera aparentemente simultánea. En un 
                entorno concurrente, las tareas pueden avanzar de forma solapada, lo que da la impresión de que se ejecutan al mismo
                 tiempo. Esto es útil para mejorar la eficiencia y la capacidad de respuesta de un programa.

• Paralelismo: Implica la ejecución real simultánea de múltiples tareas, ya sea en sistemas con múltiples núcleos de procesador o en
               varios sistemas conectados en red. El paralelismo es especialmente útil para acelerar el procesamiento de tareas intensivas,
               ya que permite distribuir la carga de trabajo entre varios recursos de manera efectiva.

• Concurrencia vs Paralelismo: La concurrencia se refiere a la coordinación de múltiples tareas para un mejor rendimiento general,
                              mientras que el paralelismo implica la ejecución real simultánea de dichas tareas.

• Async/Await: Permite escribir código asíncrono de una manera más clara y legible, haciéndolo parecer síncrono. La palabra clave async se 
              utiliza antes de una función para indicar que esa función devuelve una promesa. La palabra clave await se utiliza dentro de una 
              función async para esperar a que una promesa se resuelva antes de continuar con la ejecución del código.

• Funciones asincrónicas: Son funciones que pueden ejecutarse de forma asíncrona, lo que significa que pueden realizar operaciones 
                          que podrían tomar tiempo sin bloquear el flujo de ejecución principal del programa.

• Callbacks: Son funciones que se pasan como argumentos a otras funciones. Estas funciones son luego invocadas o "llamadas de vuelta" 
             por la función que las recibe en algún punto durante su ejecución.

• Promesas o Futuros: Es un objeto que representa el resultado eventual de una operación asincrónica. Está en uno de tres estados: pendiente, 
                    cumplida o rechazada. Una vez que una promesa se ha cumplido o rechazado, ésta bloquea su estado y su valor resultante 
                    no cambiará.

• Promesas encadenadas: Son una forma de manejar múltiples operaciones asincrónicas de manera secuencial. En lugar de anidar múltiples 
                        llamadas a funciones asincrónicas, las promesas encadenadas permiten encadenar varias operaciones asincrónicas 
                        de forma que cada una se ejecute después de que la anterior haya completado su trabajo.

• Event loop:  Es un mecanismo que permite que un programa pueda realizar múltiples tareas de forma concurrente, sin necesidad de esperar
               a que una tarea se complete antes de comenzar la siguiente. Cuando una tarea asíncrona se inicia, el event loop agrega esa 
               tarea a una cola de eventos. Luego, el event loop continuamente verifica si hay eventos pendientes en la cola y administra 
               la ejecución de cada uno de ellos. Esto permite que el programa continúe funcionando de forma eficiente, manejando múltiples 
               operaciones asíncronas sin bloquear el flujo principal del programa.

• Timeouts: Se refieren a la duración máxima permitida para que una operación asincrónica se complete. Si la operación no se completa dentro 
            de este límite de tiempo, se produce un "timeout", y la operación se considera fallida. Estos son importantes para prevenir bloqueos
            indefinidos o retrasos excesivos en aplicaciones asincrónicas. Al utilizarlos apropiadamente, se puede controlar el comportamiento 
            de la aplicación en situaciones donde la operación asincrónica no responde dentro de un tiempo razonable. Es común manejar los 
            timeouts mediante la configuración de temporizadores y la captura de excepciones o eventos que indiquen que el tiempo límite se
            ha agotado. Esto permite que la aplicación continúe su ejecución de manera controlada, en lugar de quedar atrapada esperando 
            indefinidamente.
• Streams: Son secuencias de datos continuos que se pueden procesar de manera individual o en lotes a medida que llegan, en lugar de tener
        que esperar a que todos los datos estén disponibles antes de comenzar a procesarlos. Proporcionan una forma conveniente de manejar
        entradas y salidas en tiempo real. Son especialmente útiles cuando se trabaja con grandes cantidades de datos o con fuentes de datos
        en tiempo real.

• Corrutinas: Son un tipo especial de rutina que pueden suspenderse y reanudarse en puntos específicos. Esto permite la ejecución cooperativa,
            donde una corrutina puede ceder el control a otra y luego reanudar su ejecución en un punto determinado. 

• Threading: Se refiere a la creación de subprocesos dentro de un único proceso. Estos subprocesos comparten la misma memoria y pueden acceder
             a los mismos datos directamente. Es el proceso de ejecutar múltiples hilos dentro de un programa para realizar tareas de forma concurrente.
             Los hilos son secuencias independientes de ejecución que pueden ejecutarse simultáneamente, lo que permite que un programa realice varias
             tareas al mismo tiempo. Los hilos se utilizan para realizar operaciones en segundo plano, ejecutar tareas que pueden bloquear el programa 
             principal, o para mejorar el rendimiento al realizar cálculos intensivos de forma paralela.

• Multiprocessing: Implica la creación de múltiples procesos independientes. Cada proceso tiene su propio espacio de memoria y no comparte 
                   memoria directamente con otros procesos.

• Threading vs multiprocessing:  multiprocessing utiliza procesos en lugar de subprocesos como threading. A diferencia del threading, donde
                                 múltiples hilos comparten el mismo espacio de memoria, el multiprocessing crea procesos separados que se 
                                 ejecutan de forma independiente.





## 6- DEvOps:
• CI / CD es un enfoque que busca automatizar el proceso de construcción, prueba y despliegue de software, lo que conlleva
          a una liberación más rápida, frecuente y confiable de aplicaciones.

• La Integración Continua (CI) es una práctica de desarrollo de software en la que los desarrolladores combinan su trabajo con 
                             frecuencia, generalmente varias veces al día. Cada integración se verifica automáticamente con pruebas 
                             para detectar errores lo antes posible. Esto permite una detección temprana de problemas y una rápida 
                             corrección, lo que a su vez ayuda a reducir los conflictos de integración

• La Entrega Continua (CD) se refiere a la práctica de entregar de manera automática y confiable las versiones de software a través
                           de distintos entornos de prueba y producción. El objetivo es asegurar que el software esté siempre en un
                          estado desplegable, lo que permite reducir el tiempo entre la escritura del código y su despliegue en producción


## 7- Métodos de resolucion de problemas de programacion
• Divide y vencerás : Este enfoque consiste en dividir un problema en subproblemas más pequeños que puedan resolverse de manera independiente.
                      Posteriormente, se combinan las soluciones de los subproblemas para obtener la solución del problema original.

• Dos punteros: Es una técnica comúnmente utilizada para resolver problemas de algoritmos donde se necesita buscar un par de elementos en un
                conjunto que cumplan con ciertas condiciones. En esencia, consiste en utilizar dos punteros o índices para explorar el arreglo 
                desde diferentes posiciones y moverlos de manera estratégica para encontrar la solución al problema.

• Programación dinámica : Se utiliza para resolver problemas que pueden dividirse en subproblemas solapados, es decir, donde se repiten cálculos.
                         En lugar de resolver cada subproblema repetidamente, la programación dinámica almacena las soluciones de los subproblemas
                         en una tabla para su reutilización.

• Algoritmos voraces : En este enfoque, se toman decisiones secuenciales según una regla específica en cada paso. Estas decisiones suelen ser las
                         óptimas localmente, con la esperanza de que el resultado global sea óptimo.

• Backtracking: Es útil para resolver problemas en los que se necesita probar todas las posibles combinaciones para encontrar una solución.


## 8- Estructuras de datos y algoritmos
• 



## 9- Patrones de Diseño
# Creacionales
• Factory: Se utiliza para crear objetos de un tipo específico sin exponer la lógica de creación al cliente, sin especificar la clase exacta 
           del objeto que se creará. En esencia, proporciona una interfaz para crear instancias de una clase, pero permite a las subclases 
           alterar el tipo de objetos que se crearán. Se centra en la creación de una instancia de una clase específica, delegando la 
           implementación a las subclases.
    1 . **Producto:** Es la interfaz o clase base de los objetos que el patrón Factory puede crear.

    2. **Productor:** Es la clase que contiene el método de fábrica. Este método es responsable de instanciar el objeto concreto basado en
                      ciertos criterios.

    3. **Producto concreto:** Son las clases reales que implementan la interfaz del Producto y son creadas por el Productor.


• Abstract Factory: Proporciona una interfaz para crear familias de objetos relacionados o dependientes sin especificar sus clases concretas.
                     Esto significa que el cliente no necesita preocuparse por cómo se crean los objetos, sino que simplemente interactúa con 
                     la interfaz proporcionada por la fábrica abstracta.
    1. **Abstract Factory**: Define una interfaz para crear distintos tipos de objetos dentro de una familia de productos. 

    2. **Fábricas concretas**: Implementan la interfaz de la Abstract Factory para crear objetos concretos de la familia de productos.

    3. **Productos abstractos**: Son las interfaces para distintos tipos de productos que serán creados por la fábrica abstracta.

    4. **Productos concretos**: Son las implementaciones concretas de los productos abstractos definidos. Cada familia de productos 
    tiene sus propias implementaciones de productos concretos.


• Builder: Se utiliza para construir un objeto complejo paso a paso. Permite la creación de diferentes variantes de un objeto sin necesidad
             de exponer su representación interna. En lugar de utilizar un constructor con un gran número de parámetros, el patrón Builder 
            utiliza un objeto builder para construir el objeto paso a paso y después devolver el producto final
    1. Product: Es el objeto complejo que se está construyendo. En el contexto del patrón Builder, este es el producto final que se obtiene
                 después de aplicar todas las construcciones y configuraciones.

    2. Builder: Es una interfaz o una clase abstracta que define los pasos necesarios para construir el producto. Esta interfaz o clase 
                proporciona métodos para construir las diferentes partes del producto.

    3. ConcreteBuilder: Esta es una implementación concreta de la interfaz del Builder. La clase ConcreteBuilder implementa los métodos 
                        definidos en la interfaz Builder para construir y ensamblar las diferentes partes del producto.

    4. Director: Opcionalmente, un Director puede ser utilizado para supervisar el proceso de construcción, proporcionando un flujo específico 
                 para construir el producto.

    5. Client: Es el código que utiliza el patrón Builder para construir el producto. El cliente interactúa con el Builder y, opcionalmente,
                el Director para construir el objeto complejo.


• Singleton: Garantiza que una clase tenga una sola instancia y proporciona un punto de acceso global a esa instancia.
    Se compone de los siguientes elementos:
    1. Clase Singleton: Es la clase para la cual se garantiza que solo haya una instancia. Esta clase generalmente proporciona un método 
                        estático para obtener la instancia única, y el constructor de la clase generalmente es privado para evitar la creación
                        de instancias adicionales.

    2. Instancia única: Es la única instancia de la clase Singleton que el patrón garantiza. Esta instancia es compartida por todos los clientes
                         que la soliciten.

    3. Punto de acceso global: El método estático proporcionado por la clase Singleton que permite a los clientes obtener la instancia única de
                             la clase.


• Prototipo: Se utiliza para crear nuevos objetos duplicando un objeto existente, conocido como prototipo. Este patrón se centra en crear nuevos
             objetos mediante la clonación de objetos existentes, lo que evita la creación de objetos mediante un constructor

    1. Prototipo: Es la interfaz que declara el método de clonación. Puede ser una interfaz o una clase abstracta que define el método 
                    clonar o duplicar.

    2. Clase Concreta Prototipo: Implementa la interfaz Prototipo y proporciona la implementación para el método de clonación.

    3. Cliente: Utiliza el prototipo para crear nuevos objetos invocando el método de clonación. Este cliente puede ser parte de la aplicación
                 que necesita crear nuevos objetos basados en prototipos existentes.


# Estructurales 
• Adapter: Permite que interfaces incompatibles trabajen juntas.
    1. Target (Objetivo): Define la interfaz específica del dominio que usa el cliente. En otras palabras, es la interfaz a la que el cliente 
                            espera que el adaptador se adapte.

    2. Client (Cliente): Es el que utiliza la interfaz del Target para interactuar con el objeto adaptador.

    3. Adaptee (Adaptado): Es la interfaz existente que necesita ser adaptada para funcionar con el cliente. En general, el cliente no puede 
                            usar directamente esta interfaz debido a incompatibilidades.

    4. Adapter (Adaptador): Implementa la interfaz del "Target" y mantiene una referencia al objeto del "Adaptado". Actúa como un intermediario
                             que traduce las llamadas del cliente a las operaciones correspondientes en el adaptado.

• Bridge: Separa una abstracción de su implementación para que puedan variar independientemente. 
    1. Abstraction (Abstracción): Define la interfaz de alto nivel que el cliente utiliza para interactuar. Esta interfaz contiene referencias a
                                 objetos de tipo Implementor y es independiente de la implementación concreta.

    2. RefinedAbstraction (Abstracción refinada): Extiende la interfaz de Abstraction definiendo comportamientos más refinados.

    3. Implementor (Implementador): Define la interfaz para la implementación de las clases de implementación concretas. Esta interfaz no tiene
                                     que coincidir con la interfaz de Abstraction. En lugar de eso, ambas interfaces pueden diferir y, por lo tanto,
                                     separan completamente la abstracción de la implementación.

    4. ConcreteImplementor (Implementador concreto): Implementa la interfaz de Implementor y proporciona una implementación concreta de la interfaz.


• Composite: Combina objetos en estructuras de árbol para representar jerarquías parte-todo. Permite a los clientes tratar de manera uniforme tanto 
            a los objetos individuales como a las composiciones de objetos.
    1. Componente: Define la interfaz para los objetos simples y compuestos en la estructura. Puede ser una interfaz o una clase abstracta que 
                    declara operaciones comunes a todos los elementos en la estructura.

    2. Hoja (Leaf): Representa los nodos finales en la estructura. Implementa la interfaz del componente y no tiene hijos.

    3. Compuesto (Composite): Representa los nodos internos en la estructura. Contiene hojas y/o otros composites. Implementa la interfaz del componen

• Decorator: Permite agregar comportamiento adicional a objetos individualmente, de manera dinámica y transparente para el cliente.
    1. Componente: Define la interfaz para los objetos que pueden recibir decoraciones.

    2. Objeto Concreto (Concrete Component): Implementa la interfaz del componente y define el objeto base al que se pueden agregar decoraciones.

    3. Decorador (Decorator): Es una clase abstracta que también implementa la interfaz del componente. Contiene una referencia a un objeto del 
                            componente. Esta clase tiene la capacidad de envolver o anidar una operación con un comportamiento adicional antes 
                            o después de la llamada al componente envuelto.

    4. Decorador Concreto (Concrete Decorator): Extiende el decorador y agrega comportamiento adicional a los objetos.
• Facade: Proporciona una interfaz unificada para un conjunto de interfaces de un subsistema. Esto facilita el uso del subsistema al proporcionar
          una interfaz de más alto nivel.
    1. Fachada (Facade): Proporciona una interfaz unificada para un conjunto de interfaces en un subsistema. Esta fachada conoce qué clases del
                         subsistema son responsables de realizar una petición y delega la solicitud al objeto correspondiente del subsistema.

    2. Subsistema (Subsystem): Consiste en una o más clases que implementan funcionalidad específica. La fachada no implementa directamente la 
                               funcionalidad, sino que delega las peticiones a los objetos del subsistema.

• Flyweight: Se usa cuando necesitamos minimizar el uso de memoria o de procesamiento al manejar un gran número de objetos que comparten 
            características idénticas.
    1. Flyweight: Es una interfaz o clase abstracta que define las operaciones que pueden ser compartidas. Los objetos flyweight representan las 
            características intrínsecas del objeto (compartidas).

    2. Concrete Flyweight: Implementa la interfaz flyweight y almacena la parte del estado intrínseco. Este objeto debe ser compartido y reutilizado.

    3. Flyweight Factory: Es una fábrica que gestiona los objetos flyweight. Se asegura de que los flyweights se compartan de manera eficiente,
                         es decir, que cuando un cliente solicita un flyweight, el factory lo proporciona si ya existe, o crea uno nuevo si no.

    4. Cliente: Utiliza los objetos flyweight, pero también puede contener el estado extrínseco (es decir, la parte que no se comparte y es 
                específica de la instancia del cliente)

• Proxy: Introduce un intermediario o sustituto para controlar el acceso a un objeto, permitiendo agregar funcionalidad adicional, como la 
        gestión de la creación tardía, control de acceso, registro, entre otros:
    1. Sujeto (Subject): Define la interfaz común tanto para el objeto real como para el proxy, de manera que el proxy pueda utilizarse en cualquier
                     lugar donde se espere el objeto real.

    2. Proxy: Mantiene una referencia al objeto real para poder realizar tareas adicionales cuando se accede al objeto real. Implementa la misma
                 interfaz que el sujeto, lo que permite que sea utilizado en lugar del objeto real.

        - Proxy remoto (Remote Proxy): Gestiona la comunicación con un objeto remoto.
   
        - Proxy virtual (Virtual Proxy): Controla la creación tardía de un objeto pesado hasta que sea absolutamente necesario.
   
        - Proxy de protección (Protection Proxy): Controla el acceso al objeto real según los permisos o restricciones de acceso.

    3. Objeto real (Real Subject): Es el objeto original al que el proxy provee acceso controlado.


# De Comportamiento 
• Chain of Responsibility: Permite a múltiples objetos manejar una solicitud sin conocer explícitamente los detalles de la solicitud o los 
                            otros manejadores.
    1. Manejador (Handler): Define una interfaz para manejar las solicitudes y mantener una referencia al siguiente manejador en la cadena. 
                            Este puede ser una clase abstracta o una interfaz.

    2. Manejador Concreto (Concrete Handler): Implementa la interfaz del manejador y contiene la lógica para manejar la solicitud o pasa la 
                                                solicitud al siguiente manejador en la cadena.

    3. Solicitud (Request): Representa la solicitud a ser manejada por los manejadores.


• Command : Encapsula una solicitud como un objeto, lo que le permite parametrizar clientes con operaciones, encolar solicitudes, o realizar
             operaciones de registro.
    1. Comando (Command): Define una interfaz común para todos los comandos con un método ejecutar que ejecuta la acción asociada con el comando
                         y opcionalmente provee métodos para deshacer la acción.

    2. Comando Concreto (Concrete Command): Implementa la interfaz del comando y almacena la información necesaria para ejecutar la acción.
                                             Contiene una referencia a uno o más receptores (objetos que realizan la acción), y realiza la llamada
                                             a métodos del receptor cuando se ejecuta.

    3. Invocador (Invoker): Solicita que se ejecute un comando, desconociendo qué comando concreto se ejecutará. Mantiene una referencia al comando
                             y, opcionalmente, mantiene una lista de comandos ejecutados.

    4. Receptor (Receiver): Conoce cómo realizar la acción asociada con un comando. Realiza la acción cuando es llamado por el comando concreto.

    5. Cliente (Client): Crea un comando y asocia un receptor con ese comando antes de pasarlo al invocador para ser ejecutado.


• Iterator: Proporciona una forma de acceder secuencialmente a los elementos de una colección sin exponer su representación subyacente.
    1. Iterador (Iterator): Define una interfaz para acceder y recorrer los elementos de una colección.

    2. Iterador Concreto (Concrete Iterator): Implementa la interfaz del iterador y realiza el seguimiento del elemento actual en la colección
                                             durante el recorrido.

    3. Agregado (Aggregate): Define una interfaz para crear un iterador que permite recorrer los elementos de la colección.

    4. Agregado Concreto (Concrete Aggregate): Implementa la interfaz del agregado y devuelve una instancia del iterador concreto apropiado.

    5. Elemento (Element): Representa los elementos individuales dentro de la colección que se está recorriendo.


• Mediator: Es un patrón de comportamiento que se utiliza para reducir las conexiones directas entre los componentes de un sistema, promoviendo
             en su lugar un fuerte acoplamiento y permitiendo que los componentes se comuniquen a través de un objeto mediador central. Esto ayuda 
             a aumentar la reutilización del código y a simplificar la comunicación entre los componentes.

    1. Mediator (Mediador): Define una interfaz que los componentes utilizan para comunicarse entre sí. El mediador conoce y coordina las interacciones
                         entre los componentes.

    2. Concrete Mediator (Mediador Concreto): Implementa la interfaz del mediador y coordina las interacciones entre los componentes. Este mediador
                            concreto conoce los componentes específicos que debe coordinar.

    3. Colleague (Colega): Representa los componentes individuales del sistema que necesitan comunicarse entre sí, pero lo hacen a través del mediador
                         en lugar de comunicarse directamente entre ellos.

• Memento: Se utiliza para capturar el estado de un objeto en un determinado momento, de modo que sea posible restaurar el objeto a ese estado más
             tarde sin violar su encapsulación. Esto se logra a través de la captura y almacenamiento de instantáneas del estado interno del objeto,
              permitiendo así la reversión a un estado anterior si es necesario.
    1. Originator (Creador): Es el objeto cuyo estado se quiere preservar. El Originator crea un Memento que contiene una instantánea de su estado 
                             interno.

    2. Memento: Es un objeto que almacena el estado de un Originator en un momento dado. Suele contener todos los datos necesarios para restaurar
                 el estado del Originator a ese punto en el tiempo.

    3. Caretaker (Cuidador): Es responsable de mantener los Mementos, pero no los modifica ni accede a su contenido. El Caretaker actúa como una 
                            especie de caja de ahorros para los Mementos. También puede coordinar la interacción entre el Originator y el Memento,
                             aunque el Originator es el que realmente realiza la operación de guardado y restauración del estado.

• Observer: Se utiliza para definir una relación de uno a muchos entre objetos de manera que cuando un objeto cambia de estado, todos sus 
            dependientes son notificados y actualizados automáticamente. Esto ayuda a mantener la consistencia entre los objetos y a reducir el
             acoplamiento en el sistema.
    1. Sujeto (Subject): Define una interfaz para agregar, eliminar y notificar observadores. El Sujeto también mantiene una lista de observadores
                         a los que notifica sobre cualquier cambio.

    2. Observador (Observer): Define una interfaz para recibir notificaciones del Sujeto cuando su estado cambia. Los observadores se registran con 
                            el Sujeto para recibir notificaciones.

    3. Observador Concreto (Concrete Observer): Implementa la interfaz de Observador para recibir notificaciones y realizar acciones específicas 
                                                cuando el estado del Sujeto cambia.

    4. Sujeto Concreto (Concrete Subject): Implementa la interfaz del Sujeto y mantiene el estado actual. Además, notifica a los observadores cuando
                                         su estado cambia.

• State : Permite que un objeto cambie su comportamiento cuando su estado interno cambia. Esto se logra mediante la definición de distintas clases
         que representan los distintos estados posibles de un objeto, y delegando el comportamiento a un objeto que representa el estado actual.
    1. Contexto (Context): Define la interfaz que se utiliza para interactuar con el estado. Mantiene una referencia a una instancia de estado 
                            concreto que define el estado actual.

    2. Estado (State): Define una interfaz común para todos los estados concretos y encapsula el comportamiento asociado a un estado particular.

    3. Estados Concretos (Concrete States): Implementan la interfaz del estado y representan los distintos estados en los que puede encontrarse
                                            el contexto. Cada estado concreto proporciona la implementación de comportamiento asociada con ese
                                            estado particular.

• Strategy: Permite definir una familia de algoritmos, encapsular cada uno de ellos y hacerlos intercambiables. Esto permite que el algoritmo 
            pueda variar independientemente de los clientes que lo utilizan.
    1. Contexto (Context): Es el objeto que mantiene una referencia a un objeto Estrategia y lo utiliza para realizar una operación en particular.
                             El contexto delega la ejecución del algoritmo a la estrategia.

    2. Estrategia (Strategy): Define una interfaz común para todos los algoritmos soportados. Las estrategias encapsulan los algoritmos específicos
                             y hacen que sean intercambiables dentro del contexto.

    3. Estrategias Concretas (Concrete Strategies): Implementan la interfaz de Estrategia y proporcionan la implementación de algoritmos específicos.

• Template Method: Define la estructura de un algoritmo en una clase base, pero permite que las subclases redefinan ciertos pasos del algoritmo sin
                 cambiar su estructura general. Esto promueve la reutilización del código y permite compartir el comportamiento común entre las clases.

    1. Clase Abstracta (Abstract Class): Define un método plantilla que establece la estructura del algoritmo, incluyendo pasos comunes y pasos que
                                         pueden ser redefinidos por subclases.

    2. Método Plantilla (Template Method): Es un método definido en la clase abstracta que establece la secuencia de pasos del algoritmo. Este método
                                            hace uso de otros métodos, algunos de los cuales pueden ser abstractos o con opción de redefinición por
                                            las subclases.

    3. Métodos Concretos (Concrete Methods): Son métodos implementados en la clase abstracta o sus subclases que son utilizados por el método 
                                             plantilla para construir el algoritmo.

• Visitor: Se utiliza para separar algoritmos de la estructura de un objeto sobre el que operan. Permite definir un nuevo operador o método sin 
            cambiar las clases de los elementos en los que opera ese método.
    1. Visitante (Visitor): Define una interfaz que declara un método de visita para cada tipo de elemento.

    2. Elemento (Element): Define una interfaz que permite al visitante visitar el elemento. Normalmente, este elemento proporciona un método que 
                            acepta un visitante como parámetro.

    3. Elemento Concreto (Concrete Element): Implementa la interfaz de Element y define una implementación específica de aceptación de visitantes.

    4. Estructura de Objeto (Object Structure): Es una colección o estructura de elementos que pueden ser visitados por el visitante. Proporciona
                                                 una interfaz para acceder a sus elementos.




## 10- Principios de diseño
# SOLID
S - Principio de responsabilidad única (Single Responsibility Principle): Este principio establece que una clase debe tener una única razón para
    cambiar. En otras palabras, cada clase debe tener solo una responsabilidad en el sistema.

O - Principio de abierto/cerrado (Open/Closed Principle): Este principio postula que las entidades de software, como clases, módulos y funciones,
    deben estar abiertas para su extensión pero cerradas para su modificación. Esto significa que se deben poder agregar nuevas funcionalidades
    sin cambiar el código existente.

L - Principio de sustitución de Liskov (Liskov Substitution Principle): Este principio establece que los objetos de un programa deben ser 
    reemplazables por instancias de sus subtipos sin alterar la corrección del programa. En resumen, una clase base debe poder ser reemplazada
    por cualquiera de sus clases derivadas sin afectar el comportamiento esperado.

I - Principio de segregación de interfaz (Interface Segregation Principle): Este principio sugiere que los clientes no deben verse obligados a depender
     de interfaces que no utilicen. En lugar de tener interfaces grandes y generales, es mejor tener interfaces más pequeñas y específicas.

D - Principio de inversión de dependencia (Dependency Inversion Principle): Este principio indica que los módulos de alto nivel no deben
    depender de módulos de bajo nivel, ambos deben depender de abstracciones. Además, las abstracciones no deben depender de los detalles,
    sino al revés.

# KISS (Keep It Simple, Stupid) 
•  Evitar la inclusión de características innecesarias en el software.

• Prefiriendo la claridad y la simplicidad del código sobre la complejidad innecesaria.

• Enfocándose en resolver el problema de manera directa y sin agregar elementos que puedan complicar innecesariamente el sistema.

# GRASP
Son un conjunto de patrones de diseño que ayudan a asignar responsabilidades a clases y objetos en un sistema de software. Estos principios
son útiles para diseñar sistemas de software con un enfoque en la asignación clara y coherente de responsabilidades.

1. Patrón de Experto en Información (Information Expert): Este patrón sugiere asignar una responsabilidad a la clase que posee la información
     necesaria para llevar a cabo esa responsabilidad.

2. Patrón de Controlador (Controller): Propone asignar la responsabilidad de recibir y manejar peticiones y eventos del sistema a una clase
     controladora.

3. Patrón de Creador (Creator): Se centra en asignar la responsabilidad de crear instancias de clases a una clase específica o a un conjunto
     de clases.

4. Patrón de Bajo Acoplamiento (Low Coupling): Sugiere reducir las dependencias entre distintas clases, promoviendo así un diseño más flexible
     y menos sujeto a cambios.

5. Patrón de Alto Coherencia (High Cohesion): Este patrón indica que las responsabilidades dentro de una clase deben estar estrechamente
     relacionadas y unificadas en torno a una función o una tarea específica.

6. Patrón de Polimorfismo (Polymorphism): Propone utilizar el polimorfismo para asignar comportamientos a clases sin necesidad de saber de 
    antemano de qué subclase se trata.

7. Patrón de Protección de la Variabilidad (Protected Variations): Sugiere encapsular las variabilidades del sistema para proteger otras 
    partes del sistema de posibles cambios.

8. Patrón de Indirección (Pure Fabrication): Este patrón señala que en algunos casos puede ser útil introducir una clase puramente fabricada
     que no representa una entidad del dominio, pero que cumple una función específica.

# DRY (Don't Repeat Yourself)
 Es un principio de desarrollo de software que enfatiza la importancia de escribir y mantener código de manera que no se repita. Esto significa 
 que, en lugar de duplicar lógica o funcionalidad en múltiples lugares, el código debería ser modular y reutilizable

# YAGNI (You Ain't Gonna Need It)
Este principio es parte de la metodología de desarrollo de software ágil y está destinado a guiar a los desarrolladores en la toma de decisiones
sobre qué funcionalidades implementar en un sistema. Se centra en la idea de no agregar funcionalidades o complejidad innecesarias a un sistema,
especialmente cuando esas funcionalidades no se necesitan actualmente. En lugar de anticipar y desarrollar características que "podrían" ser
útiles en el futuro, los desarrolladores siguen este principio para concentrarse en implementar solo lo que se necesita en el momento presente.




## 11- Arquitectura de Software
# Conceptos generales
• Modularidad: Se refiere a la práctica de dividir un sistema en componentes más pequeños y autónomos, lo que permite que el sistema sea más 
              fácil de entender, mantener y escalar

• Cohesión: Se refiere a la medida en que los elementos de un módulo o componente de software están interrelacionados y trabajan juntos para 
            lograr un objetivo común. Un alto grado de cohesión significa que los componentes de un módulo están fuertemente relacionados entre
            sí en términos de funcionalidad y propósito. Por el contrario, la baja cohesión se refiere a un escaso vínculo entre las partes de
            un módulo, lo que puede indicar que podría ser ventajoso dividir el módulo en componentes más cohesivos.

• Acoplamiento: Se refiere al grado de interdependencia entre los diversos módulos, clases o componentes de un sistema. Un acoplamiento bajo 
                indica que las distintas partes del sistema están menos interconectadas, lo que facilita la modificación, extensión y reutilización
                del código. Por otro lado, un acoplamiento alto puede hacer que el sistema sea más difícil de mantener y actualizar, ya que los 
                cambios en una parte del sistema pueden tener efectos inesperados en otras partes. 
                
• Abstracción: Se refiere a la capacidad de enfocarse en el nivel de detalle adecuado para un determinado problema, ignorando los detalles
              innecesarios. La abstracción permite simplificar la complejidad del sistema, lo que facilita su comprensión y mantenimiento.

• Inestabilidad: Se refiere a la facilidad con la que un componente o módulo puede cambiar con el tiempo, ya sea debido a cambios en sus propias
                 características o a cambios en otros componentes con los que interactúa. Un alto nivel de inestabilidad puede llevar a una mayor
                 complejidad y dificultad para mantener y evolucionar el sistema de software. 

• Distancia de la secuencia principal: Este concepto se refiere a la medida en que un componente o módulo está conectado directa o indirectamente
                                       con la lógica central de la aplicación. 

• Connascence: Es una métrica de calidad del software que permite razonar sobre la complejidad causada por las relaciones de dependencia en el
               diseño orientado a objetos, de forma muy similar a como lo hizo el acoplamiento para el diseño estructurado. En ingeniería de 
               software, dos componentes son compatibles si un cambio en uno requeriría modificar el otro para mantener la corrección general 
               del sistema. 

    - Static Connascence: Es un tipo de acoplamiento o dependencia entre dos módulos o componentes de un sistema. Se refiere a la relación entre 
                          dos elementos en un programa que está determinada en tiempo de compilación
                          
    - Dynamic Connascence: Se refiere a la situación en la que dos o más partes del código deben cambiar simultáneamente debido a un cambio en 
                           una dependencia compartida.

# Atributos de calidad
1. Utilidad: Se refiere a la capacidad del software para satisfacer las necesidades de los usuarios y cumplir con los requisitos 
            especificados.

2. Confiabilidad: Se relaciona con la capacidad del software para mantener el funcionamiento correcto en condiciones normales y en
                  situaciones inesperadas.

3. Eficiencia: Hace referencia al uso eficiente de los recursos del sistema, como el uso de memoria, la capacidad de procesamiento y
              el tiempo de respuesta.

4. Mantenibilidad: Se refiere a la facilidad con la que el software puede ser modificado, corregido, mejorado o adaptado a nuevas 
situaciones.

5. Portabilidad: Hace alusión a la facilidad con la que el software puede ser transferido de un entorno a otro, manteniendo su funcionamiento
                 y desempeño.

6. Usabilidad: Se refiere a la facilidad de uso del software, incluyendo aspectos como la interfaz de usuario, la accesibilidad y la 
              experiencia del usuario.

7. Seguridad: Tiene que ver con la capacidad del software para proteger los datos y operaciones, así como para prevenir accesos no autorizados.

8. Escalabilidad: Hace referencia a la capacidad del software para adaptarse y manejar un crecimiento en el volumen de datos, usuarios o
                  transacciones sin comprometer su desempeño.

9. Interoperabilidad: Se refiere a la capacidad del software para interactuar con otros sistemas de manera eficiente y efectiva, incluyendo 
                      el intercambio de datos y la comunicación entre diferentes plataformas.

10. Adaptabilidad: Indica la capacidad del software para adaptarse a diferentes entornos y situaciones, incluyendo cambios en los requisitos
                  del usuario y en el ambiente tecnológico.

11. Tolerancia a fallos: Se relaciona con la capacidad del software para mantener su desempeño incluso en presencia de errores o fallas,
                         evitando fallos catastróficos.

12. Testeabilidad: Se refiere a la facilidad con la que el software puede ser probado para garantizar su correcto funcionamiento, identificar 
                  posibles fallos y verificar su conformidad con los requisitos.

13. Reusabilidad: Hace referencia a la capacidad de reutilizar componentes de software en diferentes contextos, lo que puede mejorar la
                 productividad y reducir los costos de desarrollo.

14. Documentación: Se refiere a la existencia de documentación clara y completa que describa el funcionamiento, diseño y uso del software,
                  lo que facilita su comprensión, mantenimiento y apoyo.

15. Modularidad: Se refiere a la capacidad del software para estar compuesto por módulos independientes, lo que facilita la comprensión,
                 el mantenimiento y la reutilización de componentes.

16. Extensibilidad: Indica la facilidad con la que el software puede ser extendido para incluir nuevas funcionalidades o características,
                    sin afectar el funcionamiento existente.

17. Adaptabilidad a los cambios: Este atributo se refiere a la capacidad del software para adaptarse de manera efectiva a los cambios en
                                 los requisitos, el entorno operativo y las condiciones comerciales, manteniendo su funcionalidad y desempeño
                                 a lo largo del tiempo.

18. Conformidad: Se refiere a la capacidad del software para cumplir con estándares, regulaciones y directrices específicas que son
                 aplicables a su dominio de aplicación. Esto puede incluir regulaciones de seguridad, estándares de accesibilidad, normas 
                 de la industria, entre otros.

# Preocupaciones transversales
1. Seguridad: La implementación de medidas de seguridad, como la autenticación, la autorización, la encriptación de datos, la gestión de sesiones,
              la prevención de ataques de seguridad, etc.

2. Logging y monitoreo: El registro de eventos, la generación de logs, la gestión de errores, el monitoreo del rendimiento y la salud del sistema,
                        entre otros aspectos relacionados con la trazabilidad y la gestión de información sobre el funcionamiento del software.

3. Transaccionalidad: El manejo de transacciones, la consistencia y la integridad de los datos en operaciones que involucran múltiples recursos
                      o entidades.

4. Gestión de configuraciones: La gestión de configuraciones en el software, como la parametrización, la gestión de entornos (development,
                               staging, production), la gestión de variables de entorno, entre otros.

5. Cache y almacenamiento: La gestión de caché, el acceso eficiente a datos, la gestión de la persistencia y la optimización del rendimiento
                           en la manipulación y acceso a datos.

6. Gestión de errores: Manejar y gestionar adecuadamente las excepciones y errores en la aplicación para garantizar una experiencia de usuario
                       fluida y evitar interrupciones inesperadas.

# Patrones de Arquitectura