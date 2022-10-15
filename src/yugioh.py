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
    cartasatributo = sorted(cartasatributo, key=lambda at : at[5], reverse=True)
    return cartasatributo[0]

def calcula_n_cartas_maximas_suertes_de_raza(Cartas,raza):
    carmaxsuer = []
    for carta in Cartas:
        if carta.Race == raza:
            carmaxsuer.append(carta)
    carmaxsuer = sorted(carmaxsuer, key=lambda lc : lc[7], reverse=True)
    return carmaxsuer