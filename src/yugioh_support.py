def intear(num):
    try:
        return int(num)
    except ValueError:
        return 0

def stringear(cad):
    if cad == '':
        cad='NONE'
    return cad