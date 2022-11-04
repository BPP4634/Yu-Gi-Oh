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
    #Se añade el atributo de cada carta a un conjunto llamado "atributos", de forma que no habrá elementos repetidos
    for carta in Cartas:
            atributos.add(carta.Attribute)
    #Se borra " " del conjunto, ya que ha sido añadido porque algunas cartas no tienen dicho valor
    atributos.remove('')
    #Como resultado, la función devuelve cuantos atributos hay y cuales son.
    return len(atributos),atributos

def existe_cartas_mayores_que_ataque_dado(Cartas, ataque):
    #Se comprueba si existe alguna carta con un ataque mayor que el dado
    for carta in Cartas:
        if carta.ATK > ataque:
            #Devuelve True si existe
            return True
    #Devuelve False en el caso contrario
    return False

def valor_maximo_defensa_en_atributos_dados(Cartas, atributos):
    result = []
    #Añade cartas a la lista "cartasatributo" cuyo atributo sea igual a uno de los atributos dados
    for carta in Cartas:
        if carta.Attribute in atributos:
            result.append(carta)
    #Ordena las cartas de dicha lista de mayor a menor defensa
    result = max(result, key=lambda at : at[6])
    #Devuelve la defensa, el nombre y el atributo de la primera carta
    return (result[6],result[0],result[4])

def calcula_n_cartas_maximas_suertes_de_raza(Cartas,raza):
    result = []
    #Añade a la lista "carmaxsuer" cartas cuya raza sea la misma que la dada
    for carta in Cartas:
        if carta.Race == raza:
            result.append(carta)
    #Ordena las cartas de dicha lista de mayor a menor suerte
    result = sorted(result, key=lambda lc : lc[7], reverse=True)
    #Devuelve la lista
    return result