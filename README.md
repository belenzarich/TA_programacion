# TA\_programacion

Trabajo Aplicado para la materia de programación

Integrantes: Juana Bibiloni, Emma Pyfrom, Belén Zarich

Este trabajo aplicado recibe una base de datos con mediciones de ECG y las analiza para mostrar varias métricas (máximo, mínimo, frecuencia cardíaca, etc.)



##### **Errores y Validaciones**



A continuación se detallan los errores identificados en nuestras funciones y cómo se pueden manejar: 



*Funcion: cargar\_datos(archivo)*

* Los posibles errores que encontramos:

  * El archivo no puede ser encontrado
  * Hay un error al abrir el archivo
  * Las líneas contienen un formato incorrecto



Nuestro manejo:

Se utiliza un try/except al abrir el archivo:

* Si el archivo no se encuentra salta un mensaje y devuelve una lista vacia: FileNotFoundError 
* Si hay otro tipo de error salta un mensaje general indicandolo: Exception 



Cada línea se procesa dentro de un try/except

* Si una línea es inválida se muestra un mensaje: Exception
* Se utiliza continue para seguir con el resto



\----

*Función: parsear\_linea(linea)*

* Los posibles errores que encontramos:

  * Cantidad incorrecta de columnas
  * Error en la conversión de los datos 
  * Error si se ingresa un valor invalido para el campo “hit”



Nuestro manejo:

Se valida la cantidad de columnas:

* Si la cantidad de columnas no es 6: raise ValueError

Se usa try/except para conversiones:

* Si ingresaron el tipo de dato incorrecto: raise ValueError

Se usa un raise para el valor hit:

* Si el valor es invalido para el campo hit: raise ValueError



\----

*Funcion: filtrar\_por\_participante(datos, id\_participante)*

* Los posibles errores que encontramos: 

  * Que la lista esté vacía
  * Que el participante no exista 



Nuestro manejo:

* No utilizamos excepciones simplemente hicimos que salte un mensaje indicando que la lista está vacía si el largo de la lista era 0.  



\----

*Función: calcular\_senal\_promedio(lista)*

* Los posibles errores que encontramos:

  * Que la lista vacía 



Nuestro manejo:

* Si la lista se encontraba vacía utilizamos un raise ValueError indicando que la lista no puede estar vacía. 



\----

*Funciones: calcular\_maximo\_senal(lista) / calcular\_minimo\_senal(lista)*

* Errores posibles:

  * Que la lista se encuentre vacía 



Nuestro manejo:

* Si la lista se encontraba vacía utilizamos un raise ValueError indicando que la lista esta vacía.



\----

*Función: calcular\_frecuencia\_cardiaca(picos)*

* Los posibles errores que encontramos:

  * No se pueda calcular los intervalos si hay menos de 2 picos 
  * Que los valores utilizados no sean numéricos 



Nuestro manejo:

* Utilizamos un raise ValueError indicando que no hay suficientes picos para calcular la frecuencia
* Utilizamos un try donde tratamos de convertir los valores y si no funciona se lanza un ValueError indicando que los picos deben ser números



\----

*Función: calcular\_fc\_desde\_datos(datos)*

* Los posibles errores que encontramos: 

  * Datos estén vacíos
  * Hay un fallo en la detección de los picos



Nuestro manejo:

* Se basa en funciones previas que ya validan estos errores



