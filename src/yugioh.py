from yugioh_support import *
import csv
from datetime import datetime
from collections import namedtuple

Carta = namedtuple('Carta','Name,Type,Level,Race,Attribute,ATK,DEF,LCK,Date,Rare')

def lee_cartas(archivo):
    #Creación de la lista que contendrá las tuplas con los datos de las cartas:
    cartas = []
    #Se abre el archivo, con la codificación correcta:
    with open(archivo, encoding='utf-8') as f:
        #Las lineas del fichero se almacenan en 'lector' mediante la función 'csv.reader':
        lector=csv.reader(f)
        #Se salta la primera línea, la cual no contiene datos de ninguna carta:
        next(lector)
        #Asignación de las variables de cada línea del fichero:
        for nombre,tipo,nivel,raza,atributo,ataque,defensa,suerte,fecha,rareza in lector:
            #Transformación de cada variable al tipo correcto:
            nivel = intear(nivel)
            ataque = intear(ataque)
            defensa = intear(defensa)
            suerte = float(suerte)
            fecha = datetime.strptime(fecha,'%d/%m/%Y').date()
            rareza = bool(rareza=='True')
            #Agrupación de las variables en la namedtuple definida:
            carta = Carta(nombre,tipo,nivel,raza,atributo,ataque,defensa,suerte,fecha,rareza)
            #Se añade la tupla a la lista 'cartas':
            cartas.append(carta)
        #Como resultado, la función devuelve dicha lista.
        return cartas

def numero_de_atributos(Cartas):
    atributos= set()
    for carta in Cartas:
        if atributos!='':
            atributos.add(carta.Attribute)
    atributos.remove('')
    return atributos, len(atributos)

def existe_cartas_mayores_que_ataque_dado(Cartas, ataque):
    for carta in Cartas:
        if carta.ATK > ataque:
            return True
    return False

def valor_maximo_defensa_en_atributos_dados(Cartas, atributos):
    cartasatributo = []
    for carta in Cartas:
        for atributo in atributos:
            if carta.Attribute == atributo:
                cartasatributo.append(carta)
    cartasatributo = sorted(cartasatributo, key=lambda at : at[6], reverse=True)
    return cartasatributo[0]

def calcula_n_cartas_maximas_suertes_de_raza():
    pass
'''
    Bloque II: Implementar, documentar y probar DOS funciones que trabajen sobre el dataset y respondan a preguntas interesantes. La primera se debe escoger entre los tipos (5) y (6), la segunda debe ser de tipo (7) u (8):

7. Función que obtenga una lista con n tuplas ordenadas de mayor a menor (o de menor a mayor) por una
propiedad determinada de entre las que cumplan una condición. Ejemplo: calcula_n_registros_maximos_censos
de_pais
8. Función que devuelva un diccionario que permita agrupar por una propiedad, en el que los valores sean una
lista o un conjunto con las tuplas que tienen el mismo valor de esa propiedad. Ejemplos: agrupar_registros_por
pais.
             Modificar el test para comprobar la funcionalidad añadida.'''