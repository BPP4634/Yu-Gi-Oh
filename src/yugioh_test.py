from yugioh import *

def main():
      CARTAS = test_lee_cartas('./data/card_data_FULL.csv')
      test_numero_de_atributos(CARTAS)
      test_calcular_media_ataque_nivel(CARTAS,5)
      test_calcular_media_ataque_nivel(CARTAS)
      test_valor_maximo_defensa(CARTAS)
      test_calcula_n_cartas_maximas_suertes_de_raza(CARTAS,'Zombie',5)
      test_calcula_n_cartas_maximas_suertes_de_raza(CARTAS,'Warrior')
      test_contar_cartas_por_anyo(CARTAS)
      test_min_cartas_anyo(CARTAS)
      test_max_ataque_por_tipo(CARTAS)
      test_cartas_mas_defensa_por_nivel(CARTAS,2)
      test_cartas_mas_defensa_por_nivel(CARTAS)
      test_agrupar_por_rareza(CARTAS,False,5)
      test_agrupar_por_rareza(CARTAS)
      grafica_cartas_por_anyo(CARTAS)

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

# Test de la función valor_maximo_defensa
def test_valor_maximo_defensa(cartas):
      vmdead = valor_maximo_defensa(cartas)
      print(f'El valor máximo de la defensa es {vmdead[0].DEF}, de las cartas: {vmdead}.')

# Test de la función calcula_n_cartas_maximas_suertes_de_raza
def test_calcula_n_cartas_maximas_suertes_de_raza(cartas,raza,n=3):
      cmsdr = calcula_n_cartas_maximas_suertes_de_raza(cartas,raza,n)
      print(f'Las {n} cartas de raza {raza} con mas suerte son: {cmsdr}')

# Test de la función contar_cartas_por_anyo
def test_contar_cartas_por_anyo(cartas):
      cont = contar_cartas_por_anyo(cartas)
      print('El número de cartas lanzadas cada año son:')
      for c in cont.items():
            print('En {}: {} cartas.'.format(*c))

# Test de la función min_cartas_anyo
def test_min_cartas_anyo(cartas):
      mintip = min_cartas_anyo(cartas)
      print('El año en el que se sacaron menos cartas fue en {}, siendo lanzadas solo {} cartas.'.format(*mintip))

# Test de la función max_ataque_por_tipo
def test_max_ataque_por_tipo(cartas):
      maxat = max_ataque_por_tipo(cartas)
      print('Las cartas con mayor ataque de cada tipo son:')
      for m in maxat.items():
            print('{}: {}'.format(*m))

# Test de la función cartas_mas_defensa_por_nivel
def test_cartas_mas_defensa_por_nivel(cartas,n=3):
      masnian=cartas_mas_defensa_por_nivel(cartas,n)
      print('Las',n,'cartas con mayor defensa de cada nivel son:')
      for m in masnian.items():
            print('Nivel {}: {}'.format(*m))

# Test de la función agrupar_por_rareza
def test_agrupar_por_rareza(cartas,rar=True,n=3):
      apr = agrupar_por_rareza(cartas)
      if rar==True:
            print(f"Mostrando {n} cartas raras: {apr[rar][:n]}")
      else:
            print(f"Mostrando {n} cartas comunes: {apr[rar][:n]}")

if __name__ == '__main__':
      main()