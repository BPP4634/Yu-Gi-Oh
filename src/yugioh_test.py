from yugioh import *

def main():
      CARTAS = test_lee_cartas('./data/card_data_FULL.csv')
      test_numero_de_atributos(CARTAS)
      test_existe_cartas_mayores_que_ataque_dado(CARTAS,4000)
      test_valor_maximo_defensa_en_atributos_dados(CARTAS, ['FIRE','WIND','WATER'])
      test_calcula_n_cartas_maximas_suertes_de_raza(CARTAS,'Zombie',5)

# Test de la función lee_cartas
def test_lee_cartas(archivo):
      Cartas = lee_cartas(archivo)
      print("Hay información de", len(Cartas), 'cartas en el dataset.')
      print("Las tres primeras son:", Cartas[:3])
      print("Las tres últimas son:", Cartas[-3:])
      return Cartas

# Test de la función numero_de_atributos
def test_numero_de_atributos(Cartas):
      att = numero_de_atributos(Cartas)
      print('Existen {} atributos, los cuales son: {}'.format(*att))

# Test de la función existe_cartas_mayores_que_ataque_dado
def test_existe_cartas_mayores_que_ataque_dado(Cartas, atk):
      tecmqad = existe_cartas_mayores_que_ataque_dado(Cartas,atk)
      print('¿Existen cartas con un ataque mayor que {}? {}'.format(atk,tecmqad))

# Test de la función valor_maximo_defensa_en_atributos_dados
def test_valor_maximo_defensa_en_atributos_dados(Cartas, atributos):
      vmdead = valor_maximo_defensa_en_atributos_dados(Cartas, atributos)
      print('El valor máximo de la defensa de una carta de los atributos propuestos es {}, de la carta {},\
 cuyo atributo es {}'.format(*vmdead))

# Test de la función calcula_n_cartas_maximas_suertes_de_raza
def test_calcula_n_cartas_maximas_suertes_de_raza(Cartas,raza,n=3):
      cmsdr = calcula_n_cartas_maximas_suertes_de_raza(Cartas,raza)
      print('Las {} cartas de raza {} con mas suerte son: {}'.format(n,raza,cmsdr[:n]))

if __name__ == '__main__':
      main()