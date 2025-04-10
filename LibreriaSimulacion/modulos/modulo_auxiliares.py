
def validar_int(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        return None

def validar_float(valor):
    try:
        valor = float(valor)
        return valor
    except ValueError:
        return None

def input_numero(msg, tipo):

    valor = validar_int(input(msg)) if tipo == "int" else validar_float(input(msg))
    # valor = validar_int(input(msg))

    while valor is None:
        print("Valor no valido, ingrese un numero valido")
        valor = validar_int(input(msg)) if tipo == "int" else validar_float(input(msg))

    return valor
