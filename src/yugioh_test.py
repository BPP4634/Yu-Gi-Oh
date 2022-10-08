from yugioh import *

def main():
      test_lee_cartas('./data/card_data_FULL.csv')

# Test de la función lee_cartas
def test_lee_cartas(archivo):
      Cartas = lee_cartas(archivo)
      print(len(Cartas))
      print(Cartas[:3])
      print(Cartas[-3:])

if __name__ == '__main__':
      main()