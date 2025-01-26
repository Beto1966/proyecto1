# Ejemplo de uso (example.py)
from cliente import Cliente

if __name__ == "__main__":
    # Crear un cliente
    cliente1 = Cliente("Juan Pérez", "juan.perez@example.com", 25)

    # Imprimir detalles del cliente
    print(cliente1)

    # Verificar si el cliente es mayor de edad
    if cliente1.es_mayor_de_edad():
        print(f"{cliente1.nombre} es mayor de edad.")
    else:
        print(f"{cliente1.nombre} no es mayor de edad.")

    # Cambiar el email del cliente
    print(cliente1.cambiar_email("nuevo.email@example.com"))

    # Imprimir detalles actualizados del cliente
    print(cliente1)
