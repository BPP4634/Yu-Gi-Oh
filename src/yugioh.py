from yugioh_support import *
import csv
from datetime import datetime
from collections import namedtuple,Counter,defaultdict
from matplotlib import pyplot as plt

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

def valor_maximo_defensa(cartas):
    #Obtiene la mayor defensa
    maxd = max(cartas, key=lambda d : d.DEF).DEF
    #Devuelve las cartas con dicha defensa
    return [c for c in cartas if c.DEF==maxd]

def calcula_n_cartas_maximas_suertes_de_raza(cartas,raza,n=3):
    #Añade a la lista "result" cartas cuya raza sea la misma que la dada
    result = [carta for carta in cartas if carta.Race == raza]
    #Ordena las cartas de dicha lista de mayor a menor suerte
    result = sorted(result, key=lambda lc : lc.LCK, reverse=True)
    #Devuelve los n primeros elementos de la lista
    return result[:n]

def contar_cartas_por_anyo(cartas):
    #Crea una lista "anyos" formada por todos los años de lanzamiento de cartas
    anyos=[c.Date.year for c in cartas]
    #La función cuenta cuantas veces aparece cada año y devuelve el resultado (en orden cronológico)
    return dict(sorted(Counter(anyos).items()))

def min_cartas_anyo(cartas):
    #La función devuelve el año en el que se han lanzado menos cartas y el número de estas.
    #Para ello, busca el valor mínimo en el resultado de la función "contar_cartas_por_anyo"
    return min(contar_cartas_por_anyo(cartas).items(),key=lambda x:x[1])

def max_ataque_por_tipo(cartas):
    #Se crea el diccionario "aux", un defaultdict de tipo lista, cuyas claves serán los tipos de las
    #cartas y cuyos valores serán las cartas con el tipo de la clave
    aux=defaultdict(list)
    for c in cartas:
        aux[c.Type].append(c)
    #Se crea un diccionario cuyas claves son las de aux y cuyos valores son la carta con el ataque más alto
    #entre todas las de su tipo. La función devuelve dicho diccionario
    return {a:max(aux[a], key=lambda c:c.ATK) for a in aux}

def cartas_mas_defensa_por_nivel(cartas,n=3):
    #Se crea el diccionario "aux", un defaultdict de tipo lista, cuyas claves serán los niveles de las
    #cartas y cuyos valores serán las cartas con el nivel de la clave.
    #También creamos el diccionario vacío "result"
    aux=defaultdict(list)
    result={}
    for c in cartas:
        aux[c.Level].append(c)
    #Ordenamos los niveles de menor a mayor para una mejor visualización del resultado
    aux=dict(sorted(aux.items()))
    #Se añaden a "result" las claves de "aux", siendo sus valores una lista de tuplas con los nombres y
    #las defensas de las n cartas con las defensas más alta de entre todas las de su nivel
    for a in aux:
        result[a]=[(c.Name,c.DEF) for c in sorted(aux[a], key=lambda c:c.DEF, reverse=True)][:n]
    #La función devuelve "result"
    return result

def agrupar_por_rareza(cartas):
    #Se crea un defaultdict de tipo lista cuyas claves serán la rareza de cartas y cuyos valores serán las
    #las cartas de la rareza indicada en la clave
    result=defaultdict(list)
    for c in cartas:
        result[c.Rare]+=[c]
    #La función devuelve dicho diccionario
    return result

def grafica_cartas_por_anyo(cartas):
    #Usando la función "agrupar_por_rareza", se obtiene una lista con todas las cartas raras y otra con todas
    #las comunes a partir de la lista de cartas dada. Las tres se pasan individualmente por la función 
    #"contar_cartas_por_anyo"
    aux=agrupar_por_rareza(cartas)
    carr,carc=aux[True],aux[False]
    cart,carr,carc = contar_cartas_por_anyo(cartas),contar_cartas_por_anyo(carr),contar_cartas_por_anyo(carc)
    #Usando los resultados de "contar_cartas_por_anyo", se toman las claves (años) para determinar la
    #posición de los puntos en el eje x, y los valores (número de cartas por año) para determinar la posición
    #en el eje y
    plt.plot(cart.keys(), cart.values(),'g',label='Todas')
    plt.plot(carr.keys(), carr.values(),'r',label='Raras')
    plt.plot(carc.keys(), carc.values(),'b',label='Comunes')
    plt.title("Cartas lanzadas a lo largo de los años")
    plt.legend()
    plt.show()