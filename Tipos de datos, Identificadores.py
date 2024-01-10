#En este caso, crearé un programa que calcula el área de un círculo ingresando el radio.
#Este programa utiliza diferentes tipos de datos (float para el radio, str para la entrada del usuario)
import math

# Comentario que describe la funcionalidad del programa
# Este programa calcula el área de un círculo dados su radio.

def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo.

    :param radio: El radio del círculo.
    :return: El área del círculo.
    """
    if radio < 0:
        print("Error: El radio no puede ser negativo.")
        return None

    area = math.pi * radio**2
    return area

# Prueba del programa
if __name__ == "__main__":
    # Entrada de usuario para obtener el radio del círculo
    radio_usuario = float(input("Ingrese el radio del círculo: "))

    # Llamada a la función para calcular el área del círculo
    area_circulo = calcular_area_circulo(radio_usuario)

    # Imprimir el resultado si no hay errores
    if area_circulo is not None:
        print(f"El área del círculo con radio {radio_usuario} es: {area_circulo}")