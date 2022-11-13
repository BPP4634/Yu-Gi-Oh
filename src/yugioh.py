from yugioh_support import *
import csv
from datetime import datetime
from collections import namedtuple

Carta = namedtuple('Carta','Name,Type,Level,Race,Attribute,ATK,DEF,LCK,Date,Rare')

def lee_cartas(archivo):
    #Creación de la lista que contendrá las tuplas con los datos de las cartas
    cartas = []
    #Se abre el archivo, con la codificación correcta
    with open(archivo, encoding='utf-8') as f:
        #Las lineas del fichero se almacenan en 'lector' mediante la función 'csv.reader'
        lector=csv.reader(f)
        #Se salta la primera línea, la cual no contiene datos de ninguna carta
        next(lector)
        #Asignación de las variables de cada línea del fichero
        for nombre,tipo,nivel,raza,atributo,ataque,defensa,suerte,fecha,rareza in lector:
            #Transformación de cada variable al tipo correcto
            nivel = int_parser(nivel)
            atributo = string_parser(atributo)
            ataque = int_parser(ataque)
            defensa = int_parser(defensa)
            suerte = float(suerte)
            fecha = datetime.strptime(fecha,'%d/%m/%Y').date()
            rareza = bool(rareza=='True')
            #Agrupación de las variables en la namedtuple definida
            carta = Carta(nombre,tipo,nivel,raza,atributo,ataque,defensa,suerte,fecha,rareza)
            #Se añade la tupla a la lista 'cartas'
            cartas.append(carta)
        #Como resultado, la función devuelve dicha lista
        return cartas

def numero_de_atributos(cartas):
    #Se añade el atributo de cada carta a un conjunto llamado "atributos", de forma que no habrá elementos
    #repetidos en este
    atributos = {carta.Attribute for carta in cartas}
    #Como resultado, la función devuelve cuantos atributos hay y cuales son
    return len(atributos),atributos

def calcular_media_ataque_nivel(cartas,nivel=3):
    #Se crea una lista por comprensión con los valores de los ataques de las cartas cuyo nivel
    #coincide con el dado. Como resultado, la función devuelve la media de dichos valores
    return media([c.ATK for c in cartas if c.Level==nivel])

def valor_maximo_defensa_en_atributos_dados(cartas, atributos):
    #Añade cartas a la lista "result" cuyo atributo sea igual a uno de los atributos dados
    result = [carta for carta in cartas if carta.Attribute in atributos]
    #De dicha lista, obtiene la carta que tenga la mayor defensa
    maxd = max(result, key=lambda d : d.DEF)
    #Devuelve la defensa, el nombre y el atributo de la/s carta/s con dicha defensa
    return [(r.DEF,r.Name,r.Attribute) for r in result if r.DEF==maxd.DEF]

def calcula_n_cartas_maximas_suertes_de_raza(cartas,raza,n=3):
    #Añade a la lista "result" cartas cuya raza sea la misma que la dada
    result = [carta for carta in cartas if carta.Race == raza]
    #Ordena las cartas de dicha lista de mayor a menor suerte
    result = sorted(result, key=lambda lc : lc.LCK, reverse=True)
    #Devuelve los n primeros elementos de la lista
    return result[:n]