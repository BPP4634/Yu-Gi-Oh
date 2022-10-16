from yugioh import *

def main():
      Cartas = test_lee_cartas('./data/card_data_FULL.csv')
      test_numero_de_atributos(Cartas)
      test_existe_cartas_mayores_que_ataque_dado(Cartas,4000)
      test_valor_maximo_defensa_en_atributos_dados(Cartas, ('DARK','EART','FIRE'))
      test_calcula_n_cartas_maximas_suertes_de_raza(Cartas,'Zombie')

# Test de la función lee_cartas
def test_lee_cartas(archivo):
      Cartas = lee_cartas(archivo)
      print(len(Cartas))
      print(Cartas[:3])
      print(Cartas[-3:])
      return Cartas

# Test de la función numero_de_atributos
def test_numero_de_atributos(Cartas):
      att = numero_de_atributos(Cartas)
      print('Existen', att[1], 'atributos, los cuales son:', att[0])

# Test de la función existe_cartas_mayores_que_ataque_dado
def test_existe_cartas_mayores_que_ataque_dado(Cartas, atk):
      tecmqad = existe_cartas_mayores_que_ataque_dado(Cartas,atk)
      print('¿Existen cartas con un ataque mayor que ' + str(atk) + '?', tecmqad)

# Test de la función valor_maximo_defensa_en_atributos_dados
def test_valor_maximo_defensa_en_atributos_dados(Cartas, atributos):
      vmdead = valor_maximo_defensa_en_atributos_dados(Cartas, atributos)
      print('El valor máximo del ataque de una carta de los atributos propuestos es ' + str(vmdead[0]) + ', de la carta ' + vmdead[1] + ', cuyo atributo es', vmdead[2])

# Test de la función calcula_n_cartas_maximas_suertes_de_raza
def test_calcula_n_cartas_maximas_suertes_de_raza(Cartas,raza,n=10):
      cmsdr = calcula_n_cartas_maximas_suertes_de_raza(Cartas,raza)
      print('Las', n, 'cartas de raza', raza, 'con mas suerte son:', cmsdr[:n])

if __name__ == '__main__':
      main()