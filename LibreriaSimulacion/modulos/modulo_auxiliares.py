
def validar_int(valor, minimo=None, maximo=None):
    try:
        valor = int(valor)
        if valor <= 0 or (minimo is not None and valor < minimo) or (maximo is not None and valor > maximo):
            raise ValueError("El numero debe ser positivo")
        return valor
    except ValueError:
        return None

def validar_float(valor, minimo=None, maximo=None):
    try:
        valor = float(valor)
        if valor <= 0 or (minimo is not None and valor < minimo) or (maximo is not None and valor > maximo):
            raise ValueError("El numero debe ser positivo")
        return valor
    except ValueError:
        return None

def input_numero(msg, tipo, min=None, max=None):

    valor = validar_int(input(msg), minimo=min, maximo=max) if tipo == "int" else validar_float(input(msg), minimo=min, maximo=max)

    while valor is None:
        print("Valor no valido, ingrese un numero valido")
        valor = validar_int(input(msg), minimo=min, maximo=max) if tipo == "int" else validar_float(input(msg), minimo=min, maximo=max)

    return valor
