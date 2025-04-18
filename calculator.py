def sumar(a, b):
    return a + b

def pedir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Por favor ingresa un número válido.")

if __name__ == "__main__":
    num1 = pedir_numero("Ingresa el primer número: ")
    num2 = pedir_numero("Ingresa el segundo número: ")

    resultado = sumar(num1, num2)
    print("La suma es:", resultado)

