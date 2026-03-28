# type: ignore
class Persona:
    developer = "Jaime Vilorio"

    @staticmethod
    def hablar(mensaje):
        print("La persona dice lo siguiente: " + mensaje)

    @staticmethod
    def pensar(pensamiento):
        print("La persona está pensando lo siguiente: " + pensamiento)

# Persona.hablar("Hola Mundo")
# Persona.pensar("Tengo hambre")
# Persona.hablar("Estoy aprendiendo POO")
# Persona.pensar("Esto es fácil")

# Herencia

class Estudiante(Persona):
    matricula = "ABC-123"

    def cursar_materia(materia):
        print("El estudiante está cursando la siguiente materia: " + materia)


Estudiante.pensar("Este estudiante está pensando en POO")
Estudiante.cursar_materia("Lenguaje de programación I")

# ----

class Persona_2:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def hablar(self, mensaje):
        print(f"{self.nombre} {self.apellido} dice: {mensaje}")

class Estudiante_2(Persona_2):
    def __init__(self, nombre, apellido):
        super().__init__(nombre, apellido)

    def examinarse(self):
        print("Me estoy preparando para el examen.")

persona_1 = Persona_2("Juan", "Santana")
persona_1.hablar("Hola, qué tal?")

persona_2 = Persona_2("Pedro", "Rodríguez")
persona_2.hablar("Tengo mucho sueño")

estudiante_1 = Estudiante_2("Mario", "Rosario")
estudiante_1.hablar("Estudiar es importante")
estudiante_1.examinarse()
