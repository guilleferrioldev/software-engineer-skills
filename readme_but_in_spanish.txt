# Conceptos generales: 
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


# Conceptos de OOP
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
                    acceso, como público, protegido y privado, que controlan la visibilidad de los atributos y métodos 
                    de un objeto.

• Herencia: Permitir que una clase (llamada clase hija o subclase) herede características (atributos) y comportamientos
             (métodos) de otra clase (llamada clase padre o superclase).

• Polimorfismo: Hace que un objeto pueda tomar muchas formas. Permite que un objeto pueda ser tratado como si fuera
                de un tipo diferente.  Permite que diferentes objetos respondan de manera única a los mismos mensajes.

• Polimorfismo de sobrecarga: Se refiere a la capacidad de diferentes clases de tener métodos con el mismo nombre pero 
                              con diferentes implementaciones. Cuando llamas a un método con un nombre en particular, 
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