from yugioh import *

if __name__ == '__main__':
# Test de la función lee_cartas
      Cartas = lee_cartas('./data/card_data_FULL.csv')
      print(Cartas[:-3])