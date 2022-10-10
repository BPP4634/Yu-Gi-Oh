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