from yugioh import *

def main():
      Cartas = test_lee_cartas('./data/card_data_FULL.csv')
      test_numero_de_atributos(Cartas)
      test_existe_cartas_mayores_que_ataque_dado(Cartas,4000)

# Test de la función lee_cartas
def test_lee_cartas(archivo):
      Cartas = lee_cartas(archivo)
      print(len(Cartas))
      print(Cartas[:3])
      print(Cartas[-3:])
      return Cartas

def test_numero_de_atributos(Cartas):
      att = numero_de_atributos(Cartas)
      print(att[0])
      print(att[1])

def test_numero_de_atributos(Cartas):
      att = numero_de_atributos(Cartas)
      print(att[0])
      print(att[1])

def test_existe_cartas_mayores_que_ataque_dado(Cartas, atk):
      tecmqad = existe_cartas_mayores_que_ataque_dado(Cartas,atk)
      print(tecmqad)


if __name__ == '__main__':
      main()