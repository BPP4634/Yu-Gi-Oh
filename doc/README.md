# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso  \<XX\>/\<YY\>)
Autor/a: Beatriz Gutiérrez Arazo   uvus:BPP4634

El objetivo de este proyecto consiste en trabajar con un dataset sobre cartas de Yu-Gi-Oh (descargado de Kaggle en https://www.kaggle.com/datasets/tathor/yugioh-trading-cards-dataset). El dataset original constaba de 7 columnas: 4 con datos de tipo string y 3 con datos de tipo int. Por ello, han sido añadidas dos nuevas columnas: una de tipo float ("LCK", que vendría de "Luck" y representaría puntos de suerte para cada carta) y la otra de tipo datetime ("Release date", la cual representaría la fecha de lanzamiento de la carta). Ambas han sido generados de forma aleatoria, en el caso de "LCK" son floats de dos decimales entre 0 y 10, y en el caso de "Release date" son fechas desde el 1 de enero de 1999 (año de lanzamiento de las primeras cartas) hasta el 2020.


## Estructura de las carpetas del proyecto

* **/src**: Contiene los diferentes módulos de Python que conforman el proyecto.
  * **\yugioh.py**: Contiene funciones que trabajan con los datos de las cartas de Yu-Gi-Oh!
  * **yugioh_test**: Contiene las invocaciones a las funciones escritas en "yugioh.py", con el fin de ejecutarlas y comprobar que funcionen.
  * **\<modulo2.py\>**: Añade descripciones para el resto de módulos que pueda tener tu proyecto. Por ejemplo, sería conveniente tener un módulo separado con funciones genéricas para dibujar gráficas y/o otro con funciones genéricas de conversión de tipos. 
* **/data**: Contiene el dataset o datasets del proyecto
    * **\<dataset1.csv\>**: Añade una descripción genérica del dataset.
    * **\<dataset2.csv\>**: Añade una descripción del resto de datasets que puedas tener.
    
## Estructura del *dataset*

En el dataset, cada fila representan los datos de cada carta. Está compuesto por 9 columnas, con la siguiente descripción:

* **Name**: de tipo string, representa el nombre de la carta.
* **Type**: de tipo tring, representa el tipo de carta.
* **Level**: de tipo int, representa el nivel del monstruo invocado con la carta.
* **Race**: de tipo string, representa la raza del monstruo invocado con la carta.
* **Attribute**: de tipo string, representa los atributos del monstruo invocado con la carta.
* **Atk**: de tipo int, representa los puntos de ataque del monstruo invocado con la carta.
* **Def**: de tipo int, representa los puntos de defensa del monstruo invocado con la carta.
* **Lck**: de tipo float, representa los puntos de suerte del monstruo invocado con la carta.
* **Release_date**: de tipo datetime, representa la fecha de lanzamiento de la carta.

## Tipos implementados

Para el proyecto, ha sido definida una tupla con nombre:


## Funciones implementadas
Añade aquí descripciones genéricas de las funciones, que luego debes acompañar con comentarios de tipo documentación en el código

### \<modulo 1\>

* **<funcion 1>**: Descripción de la función 1.
* **<funcion 2>**: Descripción de la función 2.
* ...

### \<test modulo 1\>

* **<test funcion 1>**: Descripción de las pruebas realizadas a la función 1.
* **<test funcion 2>**: Descripción de las pruebas realizadas a la función 2.
* ...
* 
### \<modulo 2\>

* **<funcion 1>**: Descripción de la función 1.
* **<funcion 2>**: Descripción de la función 2.
* ...
