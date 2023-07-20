def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("El número debe ser un entero positivo.")
    
    if n > 12:
        raise ValueError("El número debe ser menor que 12.")
    resultado = 1
    
    for i in range(1, n + 1):
        resultado *= i
    return resultado

