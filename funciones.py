def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):  # Solo revisamos hasta la raíz cuadrada
        if numero % i == 0:
            return False
    return True
