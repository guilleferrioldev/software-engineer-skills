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

• Generador: Es una función especial que puede pausar su ejecución y luego reanudarla desde el mismo punto en el que se detuvo.
             Esto permite la generación de una secuencia de valores de manera eficiente, ya que los valores se calculan bajo demanda 
             en lugar de generarse todos a la vez. Los generadores se crean utilizando la palabra clave yield en lugar de return dentro
             de una función. Cuando se llama a un generador, este devuelve un objeto iterador que puede utilizarse para recuperar los
             valores generados por la función.
             

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


## 5- DEvOps:
• CI / CD es un enfoque que busca automatizar el proceso de construcción, prueba y despliegue de software, lo que conlleva
          a una liberación más rápida, frecuente y confiable de aplicaciones.

• La Integración Continua (CI) es una práctica de desarrollo de software en la que los desarrolladores combinan su trabajo con 
                             frecuencia, generalmente varias veces al día. Cada integración se verifica automáticamente con pruebas 
                             para detectar errores lo antes posible. Esto permite una detección temprana de problemas y una rápida 
                             corrección, lo que a su vez ayuda a reducir los conflictos de integración

• La Entrega Continua (CD) se refiere a la práctica de entregar de manera automática y confiable las versiones de software a través
                           de distintos entornos de prueba y producción. El objetivo es asegurar que el software esté siempre en un
                          estado desplegable, lo que permite reducir el tiempo entre la escritura del código y su despliegue en producción


