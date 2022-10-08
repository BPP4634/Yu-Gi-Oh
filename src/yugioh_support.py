def monster(atk):
    if atk != None:
        return True
    else:
        return False

def intear(num):
    try:
        return int(num)
    except ValueError:
        return None