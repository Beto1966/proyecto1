# cliente_paquete/cliente.py: lugar dentro de la estructura
class Cliente: #declaracion de la clase Cliente, con mayúscula
    tipo_usuario = "Regular" #puede haber otros tipos de cliente; atributo de clase

    def __init__(self, nombre, email, edad):#Iniciliza los atribuos de instancia
        self.nombre = nombre
        self.email = email
        self.edad = edad

    def __str__(self):#Representación en forma de cadena del objeto Cliente.
        return f"Cliente: {self.nombre} ({self.email})"

    def es_mayor_de_edad(self):#Verifica si el cliente es mayor de edad. return: True si el cliente tiene 18 o más años, False en caso contrario.
        return self.edad >= 18

    def cambiar_email(self, nuevo_email):#Cambia el correo electrónico del cliente. para nuevo_email: Nuevo correo lectrónico
        self.email = nuevo_email
        return f"El email de {self.nombre} ha sido actualizado a {self.email}."




