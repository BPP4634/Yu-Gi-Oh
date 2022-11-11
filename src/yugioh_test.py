from yugioh import *

def main():
      CARTAS = test_lee_cartas('./data/card_data_FULL.csv')
      test_numero_de_atributos(CARTAS)
      test_existe_cartas_mayores_que_ataque_dado(CARTAS,4500)
      test_valor_maximo_defensa_en_atributos_dados(CARTAS, ['FIRE','WIND','WATER'])
      test_calcula_n_cartas_maximas_suertes_de_raza(CARTAS,'Zombie',5)

# Test de la función lee_cartas
def test_lee_cartas(archivo):
      cartas = lee_cartas(archivo)
      print("Hay información de", len(cartas), 'cartas en el dataset.')
      print("Las tres primeras son:", cartas[:3])
      print("Las tres últimas son:", cartas[-3:])
      return cartas

# Test de la función numero_de_atributos
def test_numero_de_atributos(cartas):
      att = numero_de_atributos(cartas)
      print('Existen {} atributos, los cuales son: {}'.format(*att))

# Test de la función existe_cartas_mayores_que_ataque_dado
def test_existe_cartas_mayores_que_ataque_dado(cartas, atk):
      tecmqad = existe_cartas_mayores_que_ataque_dado(cartas,atk)
      print(f'¿Existen cartas con un ataque mayor que {atk}? {tecmqad}')

# Test de la función valor_maximo_defensa_en_atributos_dados
def test_valor_maximo_defensa_en_atributos_dados(cartas, atributos):
      vmdead = valor_maximo_defensa_en_atributos_dados(cartas, atributos)
      print('El valor máximo de la defensa de una carta de los atributos propuestos es {}, de la carta {},\
 cuyo atributo es {}'.format(*vmdead))

# Test de la función calcula_n_cartas_maximas_suertes_de_raza
def test_calcula_n_cartas_maximas_suertes_de_raza(cartas,raza,n):
      cmsdr = calcula_n_cartas_maximas_suertes_de_raza(cartas,raza,n)
      #'cmsdr' almacena todas las cartas, pero solo mostrará las 'n' primeras
      print(f'Las {n} cartas de raza {raza} con mas suerte son: {cmsdr}')

if __name__ == '__main__':
      main()