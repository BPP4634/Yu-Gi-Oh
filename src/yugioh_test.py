from yugioh import *

def main():
      CARTAS = test_lee_cartas('./data/card_data_FULL.csv')
      test_numero_de_atributos(CARTAS)
      test_calcular_media_ataque_nivel(CARTAS,5)
      test_calcular_media_ataque_nivel(CARTAS)
      test_valor_maximo_defensa_en_atributos_dados(CARTAS, ['Fire','Wind','Water'])
      test_valor_maximo_defensa_en_atributos_dados(CARTAS, ['Dark','Earth'])
      test_calcula_n_cartas_maximas_suertes_de_raza(CARTAS,'Zombie',5)
      test_calcula_n_cartas_maximas_suertes_de_raza(CARTAS,'Warrior')

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

# Test de la función calcular_media_ataque_nivel
def test_calcular_media_ataque_nivel(cartas,nivel=3):
      meat = calcular_media_ataque_nivel(cartas,nivel)
      print(f'La media de ataque de las cartas de nivel {nivel} es {meat}.')

# Test de la función valor_maximo_defensa_en_atributos_dados
def test_valor_maximo_defensa_en_atributos_dados(cartas, atributos):
      vmdead = valor_maximo_defensa_en_atributos_dados(cartas, atributos)
      if len(vmdead)==1:
            print('El valor máximo de la defensa de una carta de los atributos propuestos es {}, de la carta\
 {}, cuyo atributo es {}.'.format(*vmdead[0]))
      else:
            print(f'El valor máximo de la defensa de una carta de los atributos propuestos es {vmdead[0][0]},\
 de las cartas {[v[1] for v in vmdead]}, cuyos atributos son, respectivamente, {[v[2] for v in vmdead]}.')

# Test de la función calcula_n_cartas_maximas_suertes_de_raza
def test_calcula_n_cartas_maximas_suertes_de_raza(cartas,raza,n=3):
      cmsdr = calcula_n_cartas_maximas_suertes_de_raza(cartas,raza,n)
      print(f'Las {n} cartas de raza {raza} con mas suerte son: {cmsdr}')

if __name__ == '__main__':
      main()