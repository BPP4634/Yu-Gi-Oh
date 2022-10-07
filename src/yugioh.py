import csv
from datetime import datetime
from collections import namedtuple
Carta = namedtuple('Carta','Name,Type,Level,Race,Attribute,ATK,DEF,LCK,Date,Monster')

def intear(num):
    try:
        return int(num)
    except ValueError:
        return None

def lee_cartas(archivo):
    cartas = []
    with open(archivo, encoding='utf-8') as f:
        lector=csv.reader(f)
        next(lector)
        for nombre,tipo,nivel,raza,atributo,ataque,defensa,suerte,fecha in lector:
            nivel = intear(nivel)
            ataque = intear(ataque)
            defensa = intear(defensa)
            suerte = float(suerte)
            fecha = datetime.strptime(fecha,'%d/%m/%Y')
            if ataque!= None:
                monstruo = True
            else:
                monstruo = False
            carta = Carta(nombre,tipo,nivel,raza,atributo,ataque,defensa,suerte,fecha,monstruo)
            cartas.append(carta)
        return cartas