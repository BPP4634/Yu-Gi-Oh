def int_parser(num):
    try:
        return int(num)
    except ValueError:
        return 0

def string_parser(cad):
    if cad == '':
        return 'None'
    else:
        return cad.capitalize()

def media(valores):
    return sum([v for v in valores])/len(valores)