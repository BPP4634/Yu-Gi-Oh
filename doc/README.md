# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso  \<XX\>/\<YY\>)
Autor/a: Beatriz Gutiérrez Arazo   uvus:BPP4634

El objetivo de este proyecto consiste en trabajar con un dataset sobre cartas de Yu-Gi-Oh (descargado de Kaggle en https://www.kaggle.com/datasets/tathor/yugioh-trading-cards-dataset). El dataset original constaba de 7 columnas: 4 con datos de tipo string y 3 con datos de tipo int. Por ello, han sido añadidas dos nuevas columnas, generadas de forma aleatoria: una de tipo float ("LCK") y la otra de tipo datetime ("Release date"). También se ha implementado una función que obtendrá y asignará a cada carta un valor de tipo boolean ("Monster").

## Estructura de las carpetas del proyecto

* **/src**: Contiene los diferentes módulos de Python que conforman el proyecto.
  * **yugioh.py**: Contiene funciones que trabajan con los datos de las cartas de Yu-Gi-Oh!.
  * **yugioh_test**: Contiene las invocaciones a las funciones escritas en "yugioh.py", con el fin de ejecutarlas y comprobar que funcionen.
* **/data**: Contiene el dataset o datasets del proyecto.
    * **card_data.csv**: Es el dataset original (descargado de Kaggle). A pesar de que contiene datos sobre las cartas de Yu-Gi-Oh!, no es el dataset con el que se trabajará en este proyecto.
    * **card_data_FULL.csv**: Se trata del dataset anterior con dos nuevas columnas añadidas para que cumpla el requisito de la variedad de tipos. Esta es la versión definitiva, y por tanto serán sus datos los que serán utilizados en el proyecto.
* **/doc**: Contiene documentos relacionados con el proyecto.
    * **README.md**: Es este documento, el cual contiene información sobre el proyecto.
  
## Estructura del *dataset*

En el dataset, cada fila representan los datos de cada carta. Está compuesto por 9 columnas, con la siguiente descripción:

* **Name**: de tipo string, representa el nombre de la carta.
* **Type**: de tipo tring, representa el tipo de carta.
* **Level**: de tipo int, representa el nivel del monstruo invocado con la carta.
* **Race**: de tipo string, representa la raza del monstruo invocado con la carta.
* **Attribute**: de tipo string, representa los atributos del monstruo invocado con la carta.
* **ATK**: de tipo int, representa los puntos de ataque del monstruo invocado con la carta.
* **DEF**: de tipo int, representa los puntos de defensa del monstruo invocado con la carta.
* **LCK**: de tipo float, representa los puntos de suerte del monstruo invocado con la carta. Su nombre es una abreviatura de "Luck", que en inglés signfica "suerte". Su valor tiene dos decimales y se encuentra entre el 0 y el 10, ambos incluídos.
* **Release_date**: de tipo datetime, representa la fecha de lanzamiento de la carta. La fecha puede ser una entre 1999 (año de lanzamiento de las primeras cartas) y el 2020, ambos incluídos.

No todas las cartas disponen de todos los datos mostrados. Las cartas de tipo monstruo (sean normales o especiales) tienen nivel, ataque y defensa, mientras que las demás (las mágicas y las de trampa) no. Esta distinción servirá para definir un nuevo valor:

* **Monster**, de tipo boolean. Representa si una carta es de tipo monstruo o no.

## Tipos implementados

Para el proyecto, ha sido definida una tupla con nombre:
'Carta = namedtuple('Carta','Name,Type,Level,Race,Attribute,ATK,DEF,LCK,Date,Monster')'

Y los tipos de los campos son, respectivamente: string, string, int, string, string, int, int, float, datetime.date y boolean.

## Funciones implementadas

A continuación, se mostrarán las funciones implementadas al código, clasificadas según el módulo en el que aparecen.

### Módulo yugioh

* **lee_cartas(archivo)**: lee los datos del dataset y devuelve una lista de tuplas conteniéndolos. Esta función hace uso de otras funciones a su vez, las cuales se encuentran en el módulo 'yugioh_support.py'.

### Módulo yugioh_test

* **main()**: función que invoca a todas las funciones que deban ser probadas:
  * **test_lee_cartas(archivo)**: test de la función 'lee_cartas(archivo)'.

### Módulo yugioh_support

Este módulo contiene funciones auxiliares (como, por ejemplo, parsers).

* **monster(atk)**: En función de si la carta tiene puntos de ataque o no, determinará si es una carta de tipo monstruo o no (respectivamente).*
* **intear(num)**: tras introducirse una cadena, la transforma en un objeto de tipo int. En el caso de que la carta no disponga de dicho dato, le dará el valor "None".

*Si bien es cierto que lo lógico sería hacer una función que busque si la palabra "monster" se encuentra en el dato "type", es más sencillo comprobar si el ataque es igual o distinto de 0 (el cual es uno de los tres datos que, como se mencionó anteriormente, solo tienen los monstruos).
