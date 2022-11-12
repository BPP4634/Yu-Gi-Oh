def intear(num):
    try:
        return int(num)
    except ValueError:
        return 0

def stringear(cad):
    if cad == '':
        cad='NONE'
    return cad

def media(valores):
    return sum([v for v in valores])/len(valores)