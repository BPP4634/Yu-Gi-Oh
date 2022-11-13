# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso 22/23)
Autor/a: Beatriz Gutiérrez Arazo. UVUS: BPP4634

El objetivo de este proyecto consiste en trabajar con un dataset sobre cartas de Yu-Gi-Oh (descargado de Kaggle en https://www.kaggle.com/datasets/tathor/yugioh-trading-cards-dataset). El dataset original constaba de 7 columnas: 4 con datos de tipo string y 3 con datos de tipo int. Por ello, han sido añadidas tres nuevas columnas, generadas de forma aleatoria: una de tipo float ("LCK"), otra de tipo datetime ("Release date") y otra de tipo boolean ("Rare").

## Estructura de las carpetas del proyecto

* **/src**: Contiene los diferentes módulos de Python que conforman el proyecto.
  * **yugioh.py**: Contiene funciones que trabajan con los datos de las cartas de Yu-Gi-Oh!.
  * **yugioh_test**: Contiene las invocaciones a las funciones escritas en "yugioh.py", con el fin de ejecutarlas y comprobar que funcionen.
* **/data**: Contiene el dataset o datasets del proyecto.
  * **card_data.csv**: Es el dataset original (descargado de Kaggle). A pesar de que contiene datos sobre las cartas de Yu-Gi-Oh!, no es el dataset con el que se trabajará en este proyecto.
  * **card_data_FULL.csv**: Se trata del dataset anterior con tres nuevas columnas añadidas para que cumpla el requisito de la variedad de tipos. Esta es la versión definitiva, y por tanto serán sus datos los que serán utilizados en el proyecto.
  
## Estructura del *dataset*

En el dataset, cada fila representan los datos de cada carta. Está compuesto por 10 columnas, con la siguiente descripción:

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

A continuación, se mostrarán las funciones implementadas al código, clasificadas según el módulo en el que aparecen y en que entrega fueran creadas.

### Módulo yugioh

#### Entrega 1
* **lee_cartas(archivo)**: lee los datos del dataset y devuelve una lista de tuplas de tipo Carta conteniéndolos. Esta función hace uso de 'int_parser(num)' y 'string_parser(cad)', localizadas en el módulo 'yugioh_support.py'.
#### Entrega 2
* **numero_de_atributos(cartas)**: dada una lista de tuplas de tipo Carta, devuelve el número de atributos que existen y un conjunto que los contenga.
* **calcular_media_ataque_nivel(cartas,nivel=3)**: dada una lista de tuplas de tipo Carta y un nivel, devuelve la media del ataque de las cartas del nivel indicado. Si no se indica el nivel, tomará el valor 3 por defecto. Esta función hace uso de 'media(valores)', localizada en el módulo 'yugioh_support.py'.
* **valor_maximo_defensa(cartas)**: dada una lista de tuplas de tipo Carta, devuelve las cartas con el valor máximo de la defensa.
* **calcula_n_cartas_maximas_suertes_de_raza(cartas,raza,n=3)**: dada una lista de tuplas de tipo Carta, una raza y un número "n", devuelve las n cartas con más suerte de la raza dada. Si no se introduce un número, "n" tomará por defecto el valor 3.

### Módulo yugioh_test

#### Entrega 1
* **main()**: función que invoca a todas las funciones que deban ser probadas:
  * **test_lee_cartas(archivo)**: test de la función 'lee_cartas(archivo)'.
#### Entrega 2
  * **test_numero_de_atributos(cartas)**: test de la función 'numero_de_atributos(cartas)'.
  * **test_calcular_media_ataque_nivel(cartas,nivel=3)**: test de la función 'calcular_media_ataque_nivel(cartas,nivel)'.
  * **test_valor_maximo_defensa(cartas)**: test de la función 'valor_maximo_defensa(cartas)'.
  * **test_calcula_n_cartas_maximas_suertes_de_raza(cartas,raza,n=3)**: test de la función 'calcula_n_cartas_maximas_suertes_de_raza(cartas,raza,n)'.

### Módulo yugioh_support

Este módulo contiene funciones auxiliares (como, por ejemplo, parsers).
#### Entrega 1
* **int_parser(num)**: tras introducirse una cadena de caracteres, la transforma en un objeto de tipo int. En el caso de que la carta no disponga de dicho dato, le dará el valor 0.
#### Entrega 2
* **string_parser(cad)**: tras introducirse una cadena de caracteres, si esta es un espacio en blanco, le dará el valor 'None', y si no, la transforma dejando en mayúscula la primera letra y pasando a minúsculas todas las demás. Es usada únicamente para los atributos, con el objetivo de evitar posibles errores y confusiones en la ejecución de ciertas funciones.
* **media(valores)**: tras introducirse una lista con números, la función calculará la media de estos y devolverá el resultado.