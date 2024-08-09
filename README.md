# Estructuras de datos y funciones (I)

Este compilado contiene tres proyectos que contemplan el uso de distintas propiedades
 que las estructuras de datos tienen para resolver problemáticas.
 
## 1- conversiones.py

Se crea un archivo conversiones.py y una estructura de datos apropiada que permita
 ingresar tasas de conversión. Las distintas tasas de conversión se deben ingresar
 mediante sys.argv en el siguiente orden: Sol, Peso Argentino, Dólar Americano.
 
### Descripción


 Para ello considere las siguientes tasas de conversión de Peso Chileno:
 ● aSolperuano: 0.0046
 ● aPesoArgentino: 0.093
 ● aDólarAmericano: 0.00013
 Además ingrese un 4to argumento que sea el valor en peso chileno a convertir. El programa
 debe devolver el valor en peso chileno convertido en las 3 divisas ingresadas.
 Al ejecutar el programa se espera el siguiente output:
 python conversiones.py 0.0046 0.093 0.0013 10000
 Respuesta esperada:
 Los 10000 pesos equivalen a:
 46.0 Soles
 930.0 Pesos Argentinos
 13.0 Dólares


## 2-  word_count.py

Este proyecto tiene la funcionalidad de analizar texto lorem ipsum, el cual es un texto de prueba que se utiliza para demostrar distintas
 tipografías además de usarse para rellenar espacios que requieran largos textos

### Descripcion

 ● Cuenta el número de palabras distintas que componen el texto ingresado.
 Para separar un texto por espacios utiliza el método .split("").
 
 Para importar texto en python adapta el siguiente código:
 with open(“texto.txt”, "r") as file:
 texto=file.read()
 donde “texto.txt” corresponde a la ruta del archivo a importar.
 
 Para comprobar el correcto funcionamiento del código se provee el archivo lorem_ipsum.txt.
 Para ejecutar el programa se utiliza a el siguiente output.
 
 python word_count.py lorem_ipsum.txt
 
 Respuesta esperada:
 El número de caracteres distintos es: 40
 El número de palabras distintas es: 243
 
## recordatorios.py  

Proyecto recordatorios.py incluye una serie de eventos que
 quieren ser recordados. El formato de estos recordatorios son una fecha
 (año-mes-día), una hora y una descripción del evento.
 
### Descripcion

Los eventos se editan de tal manera que mantengan su
 orden en el tiempo. codigo se ejecuta de acurdo a lo siguiente:
 
 1. Agregua un evento el 2 de Enero de 2021 a las 6 de la mañana para
 “Empezar el Año”.
 2. Al revisar los eventos, nota un error, ya que el 15 de Julio no es feriado. Se edita
 de tal manera que sea el 16 de Julio.
 3. Lamentablemente le tocará trabajar el día del trabajo. Se elimina el evento del
 día del trabajo.
 4. Se agrega una cena deNavidad y de Año Nuevo. Ambas a
 las 22 hrs.

 Para ejecutar el programa se requiere el siguiente output:
 python recordatorios.py
 
-------------Lista final de recordatorios:
['2021-01-01', '11:00', 'Levantarse y ejercitar']
['2021-01-02', '06:00', 'Empezar el Año']
['2021-07-16', '13:00', 'Día del trabajo (corregido)']
['2021-09-18', '16:00', 'Ramadas']
['2021-12-24', '22:00', 'Cena de Navidad']
['2021-12-25', '00:00', 'Navidad']
['2021-12-31', '22:00', 'Cena de Año Nuevo']

## Prerrequisitos o Dependencias

Sistema Operativo Windows, Linux, MacOS
Lenguaje de programación Python 3.12

## Instalación del Proyecto

Clonar el repositorio
```bash
git clone git@github.com:vanemn/desafio_modulo3_clase12.git


Elegir el programa a usar 


## Autor

- [Vanessa Morales](https://github.com/vanemn)
- [Benjamin Pardo](https://github.com/bpardo02)
- [Andres Gallardo](https://github.com/AndresGallardo95)
- [Camila riquelme](https://github.com/camilariquelme)
- [Nicole Pinilla](https://github.com/Npinilla19)
