# type:ignore
class Vendedor:
    """Esta es la clase que define a un vendedor de carro"""

    def __init__(self, nombre, apellido) -> None:
        self.nombre = nombre
        self.apellido = apellido

    def vendiendo_carro(self, marca_carro):
        """Muestra el nombre y el apellido del vendedor mas el carro que está vendiendo"""
        print(
            f"El vendedor {self.nombre} {self.apellido} está vendiendo un {marca_carro}")


class Carro:
    """Este es la clase que define un carro del delear"""

    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def acelerar(self):
        print("Acelerando..." + self.marca)

    def frenar(self):
        print("Frenando..." + self.modelo)

    def abrir_ventana(self):
        print("Abriendo ventana..." + str(self.anio))

carro_1 = Carro("Honda", "Civic", 2018)  # Instancia de la clase

vendedor_1 = Vendedor("Juan", "Pérez")
vendedor_1.vendiendo_carro(carro_1.marca)
