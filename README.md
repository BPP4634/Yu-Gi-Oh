# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso 21/22)
Autor/a: Beatriz Gutiérrez Arazo   uvus: BPP4634

El objetivo de este proyecto consiste en trabajar con un dataset sobre cartas de Yu-Gi-Oh (descargado de Kaggle en https://www.kaggle.com/datasets/tathor/yugioh-trading-cards-dataset). El dataset original constaba de 7 columnas: 4 con datos de tipo string y 3 con datos de tipo int. Por ello, han sido añadidas tres nuevas columnas, generadas de forma aleatoria: una de tipo float ("LCK"), otra de tipo datetime ("Release date") y otra de tipo boolean ("Rare").

## Estructura de las carpetas del proyecto

* **/src**: Contiene los diferentes módulos de Python que conforman el proyecto.
  * **yugioh.py**: Contiene funciones que trabajan con los datos de las cartas de Yu-Gi-Oh!.
  * **yugioh_test**: Contiene las invocaciones a las funciones escritas en "yugioh.py", con el fin de ejecutarlas y comprobar que funcionen.
* **/data**: Contiene el dataset o datasets del proyecto.
  * **card_data.csv**: Es el dataset original (descargado de Kaggle). A pesar de que contiene datos sobre las cartas de Yu-Gi-Oh!, no es el dataset con el que se trabajará en este proyecto.
  * **card_data_FULL.csv**: Se trata del dataset anterior con tres nuevas columnas añadidas para que cumpla el requisito de la variedad de tipos. Esta es la versión definitiva, y por tanto serán sus datos los que serán utilizados en el proyecto.
  
## Estructura del *dataset*

En el dataset, cada fila representan los datos de cada carta. Está compuesto por 9 columnas, con la siguiente descripción:

* **Name**: de tipo string, representa el nombre de la carta.
* **Type**: de tipo string, representa el tipo de carta.
* **Level**: de tipo int, representa el nivel del monstruo invocado con la carta.
* **Race**: de tipo string, representa la raza del monstruo invocado con la carta.
* **Attribute**: de tipo string, representa los atributos del monstruo invocado con la carta.
* **ATK**: de tipo int, representa los puntos de ataque del monstruo invocado con la carta.
* **DEF**: de tipo int, representa los puntos de defensa del monstruo invocado con la carta.
* **LCK**: de tipo float, representa los puntos de suerte del monstruo invocado con la carta (de ahí su nombre, que es una abreviatura de "Luck"). Su valor tiene dos decimales y se encuentra entre el 0 y el 10, ambos incluídos.
* **Release_date**: de tipo datetime, representa la fecha de lanzamiento de la carta. La fecha puede ser una entre 1999 (año de lanzamiento de las primeras cartas) y el 2020, ambos incluídos.
* **Rare**: de tipo boolean, representa si una carta es rara (es decir, no es fácil de conseguir) o no.

## Tipos implementados

Para el proyecto, ha sido definida una tupla con nombre:
'Carta = namedtuple('Carta','Name,Type,Level,Race,Attribute,ATK,DEF,LCK,Date,Rare')'

Y los tipos de los campos son, respectivamente: string, string, int, string, string, int, int, float, datetime.date y boolean.

## Funciones implementadas

A continuación, se mostrarán las funciones implementadas al código, clasificadas según el módulo en el que aparecen.

### Módulo yugioh

#### Entrega 1
* **lee_cartas(archivo)**: lee los datos del dataset y devuelve una lista de tuplas conteniéndolos. Esta función hace uso de la función 'intear(num)' a su vez, la cual se encuentran en el módulo 'yugioh_support.py'.
#### Entrega 2
* **numero_de_atributos(Cartas)**: dada una lista de tuplas de tipo Cartas, devuelve el número de atributos que existen y un conjunto que los contenga.
* **existe_cartas_mayores_que_ataque_dado(Cartas, ataque)**: dada una lista de tuplas de tipo Cartas y un número, devuelve un valor booleano que será True si el ataque de alguna carta es mayor que el número dado y False en el caso contrario.
* **valor_maximo_defensa_en_atributos_dados(Cartas, atributos)**: dada una lista de tuplas de tipo Cartas y una lista de atributos, devuelve el nombre de la carta con la mayor defensa, el valor de dicha defensa y su atributo.
* **calcula_n_cartas_maximas_suertes_de_raza(Cartas,raza,n=10)**: dada una lista de tuplas de tipo Cartas, una raza y un número "n", devuelve las n cartas con más suerte de la raza dada. Si no se introduce un número, "n" tomará por defecto el valor 10.

### Módulo yugioh_test

#### Entrega 1
* **main()**: función que invoca a todas las funciones que deban ser probadas:
  * **test_lee_cartas(archivo)**: test de la función 'lee_cartas(archivo)'.
#### Entrega 2
  * **test_numero_de_atributos(Cartas)**: test de la función 'numero_de_atributos(Cartas)'.
  * **test_existe_cartas_mayores_que_ataque_dado(Cartas, ataque)**: test de la función 'existe_cartas_mayores_que_ataque_dado(Cartas, ataque)'.
  * **test_valor_maximo_defensa_en_atributos_dados(Cartas, atributos)**: test de la función 'valor_maximo_defensa_en_atributos_dados(Cartas, atributos)'.
  * **test_calcula_n_cartas_maximas_suertes_de_raza(Cartas,raza,n)**: test de la función 'calcula_n_cartas_maximas_suertes_de_raza(Cartas,raza,n=10)'.

### Módulo yugioh_support

Este módulo contiene funciones auxiliares (como, por ejemplo, parsers).
#### Entrega 1
* **intear(num)**: tras introducirse una cadena, la transforma en un objeto de tipo int. En el caso de que la carta no disponga de dicho dato, le dará el valor "None".