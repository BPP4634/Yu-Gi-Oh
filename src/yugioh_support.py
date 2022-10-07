def monster(atk):
    if atk!= None:
        monstruo = True
        return monstruo
    else:
        monstruo = False
        return monstruo

def intear(num):
    try:
        return int(num)
    except ValueError:
        return None